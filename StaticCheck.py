#MSSV : 2110242
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce
class State:
     def __init__(self, ref_envs, funcs, built_ins, in_func = None, isInLoop = 0, implicit_func = [], func_params = [], typeInferred = None):
        self.ref_envs = ref_envs
        self.funcs = funcs
        self.built_ins = built_ins
        self.in_func = in_func
        self.isInLoop = isInLoop
        self.implicit_func = implicit_func
        self.func_params = func_params
        self.typeInferred = typeInferred
class ZCodeType:
    def __init__(self, starttype, rettype):
        self.starttype = starttype
        self.rettype = rettype
class Symbol:
    def __init__(self, name, type, value = None):
        self.name = name
        self.type = type
        self.value = value

def returnType(ast):
    if type(ast) is NumberType or type(ast) is NumberLiteral:
        return NumberType()
    if type(ast) is BoolType or type(ast) is BooleanLiteral:
        return BoolType()
    if type(ast) is StringType or type(ast) is StringLiteral:
        return StringType()
def checkDynaDecl(ast):
    if type(ast) is VarDecl:
        if str(ast.modifier) == 'dynamic':
            return True
    return False
def getType(ast):
    if type(ast) is VarDecl:
        if ast.varType:
            return ast.varType
        else:
            if str(ast.modifier) == 'var' :
                return returnType(ast.varInit)
            if str(ast.modifier) == 'dynamic' and ast.varInit is None:
                return None
    if type(ast) is FuncDecl:
        # FuncDecl have 3 case: 
        # Case 1: infer type from the return stmt if FuncDecl have only return stmt
        # Case 2: infer type from the return stmt in Block stmt of FuncDecl
        # Case 3: return voidType()
        if ast.body:
            if type(ast.body) is Block:
                if type(ast.body.stmt[-1]) is Return:
                    if ast.body.stmt[-1].expr:
                        return returnType(ast.body.stmt[-1].expr)
            elif type(ast.body) is Return:
                if ast.body.expr:
                    return getType(ast.body.expr)
        else:
            return VoidType()
    if type(ast) is NumberType or type(ast) is NumberLiteral:
        return NumberType()
    if type(ast) is BoolType or type(ast) is BooleanLiteral:
        return BoolType()
    if type(ast) is StringType or type(ast) is StringLiteral:
        return StringType()
    if type(ast) is ArrayType or type(ast) is ArrayLiteral:
        return ArrayType(ast.size,ast.eleType)
    return None
    
def setType(ast, typ):
    if type(ast) is VarDecl:
        ast.varType = typ
    if type(ast) is FuncDecl:
        # FuncDecl have 3 case: 
        # Case 1: infer type from the return stmt if FuncDecl have only return stmt
        # Case 2: infer type from the return stmt in Block stmt of FuncDecl
        # Case 3: return voidType()
        if ast.body:
            setType(ast.body, typ)
        else:
            return VoidType()

def updateTypeOfFunction(name,typ,env):
    for func in env:
        if func.name == name:
                func.type.rettype = typ
def updateTypeOfVariable(name,typ,env):
    for sym in env:
        if sym.name == name:
            sym.type = typ
def updateTypeoDynamicVariable(name,typ,env):
    for sym in env:
        if sym.name.name == name:
            sym.varType = typ
def getName(ast):
    if type(ast) is Id:
        return ast.name
    elif type(ast) is CallExpr:
        return ast.name.name
    return None

class StaticChecker(BaseVisitor, Utils):
    glob_env = [Symbol("readNumber",ZCodeType([],NumberType())),
                Symbol("writeNumber",ZCodeType([NumberType()],VoidType())),
                Symbol("readBool",ZCodeType([],BoolType())),
                Symbol("writeBool",ZCodeType([BoolType()],VoidType())),
                Symbol("readString",ZCodeType([], StringType())),
                Symbol("writeString",ZCodeType([StringType()],VoidType()))]
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast,self.glob_env)
    def visitProgram(self, ast: Program, context):
        self.glob_env = self.glob_env[0:6]
        context = State([[]],[],self.glob_env,None,0,[])
        hasEntry = False
        reduce(lambda acc,ele: self.visit(ele,acc), ast.decl, context)
               
        for func in context.funcs:
            if func.name.name == "main":
                if type(func.body) is Block:
                    if len(func.body.stmt) > 0:
                        if type(func.body.stmt[-1]) is Return:
                            if func.body.stmt[-1].expr:
                                raise NoEntryPoint()
                if type(func.body) is Return:
                    if func.body.expr:
                        raise NoEntryPoint()
                hasEntry = True
                break
        if not hasEntry:
            raise NoEntryPoint()
        for idx, func in enumerate(context.funcs):
            if not func.body:
                remaining_funcs = context.funcs[idx+1:]
                if func.name not in (f.name for f in remaining_funcs):
                    raise NoDefinition(func.name.name)
        return context
    def visitVarDecl(self, ast: VarDecl,context:State):
        context.in_func = ast
        for decl in context.ref_envs[0]:
            if type(decl) is VarDecl:
                if decl.name == ast.name:
                    raise Redeclared(Variable(),ast.name.name)
        for blt_in in context.built_ins[0:6]:
            if ast.name.name == blt_in.name:
                raise Redeclared(Variable(),ast.name.name)
        context.ref_envs[0][:0] = [ast]
        if len(context.ref_envs) == 1:
            self.glob_env.append(Symbol(ast.name.name, ast.varType,ast.varInit))
        if type(ast.varType) is ArrayType:
            context.typeInferred = ast.varType.eleType
        else:
            context.typeInferred = ast.varType  
        
        if ast.varInit:
            if not ast.modifier:
                initType = self.visit(ast.varInit,context)
                if type(ast.varInit) is ArrayCell:
                    initType = initType.eleType
                var_type = ast.varType
                if type(var_type) is ArrayType and type(initType) is ArrayType:
                    if len(var_type.size) != len(initType.size):
                        raise TypeMismatchInStatement(ast)
                    var_type = var_type.eleType
                if type(initType) is ArrayType:
                    if initType.eleType is not None:
                        initType = self.visit(initType.eleType,context)
                    else:
                        initType = initType.eleType
                elif initType is not None:
                    if type(initType) != type(var_type):
                        raise TypeMismatchInStatement(ast)      
                elif type(initType) != type(ast.varType):
                    raise TypeMismatchInStatement(ast)
                elif type(initType) is VoidType:
                    raise TypeMismatchInStatement(ast)
                elif initType is None and ast.varType is not None:
                    if type(ast.varInit) is CallExpr:
                        for func in context.implicit_func:
                            if ast.varInit.name == func.name and func.type.rettype is None:
                                func.type.rettype = ast.varType
            else:
                initType = self.visit(ast.varInit,context)
                if type(initType) is ArrayType:
                    if initType.eleType is None:
                        raise TypeCannotBeInferred(ast)
                if initType is None:
                    raise TypeCannotBeInferred(ast)
                if type(initType) is VoidType:
                    raise TypeMismatchInStatement(ast)
                ast.varType = initType
        return context
    def visitFuncDecl(self, ast: FuncDecl, context:State):
        if ast.name.name == "main":
            if ast.param:
                raise NoEntryPoint()
        isImplicit = False
        count_func = 0
        func_type = None
        for func in context.implicit_func:
            if func.name == ast.name.name:
                isImplicit = True
                func_type = func.type.rettype
                break
        if isImplicit == True:
            count_func = 1
        for func in context.funcs:
            if func.name.name == ast.name.name:
                count_func += 1
            if count_func >2 and isImplicit == True:
                raise Redeclared(Function(),ast.name.name)
            elif count_func == 1 and isImplicit == False:
                raise Redeclared(Function(),ast.name.name)
            elif count_func == 2 and isImplicit == True:
                if type(ast.body) is Return:
                    if ast.body.expr is None:
                        raise Redeclared(Function(),ast.name.name)
                if type(ast.body) is Block:
                    if len(ast.body.stmt) == 0:
                            raise Redeclared(Function(),ast.name.name)
            elif count_func == 1 and isImplicit == True:
                if type(ast.body) is Return:
                    if ast.body.expr is None:
                        raise Redeclared(Function(),ast.name.name)
                
        for blt_in in context.built_ins:
            if ast.name.name == blt_in.name:
               if isImplicit == False and type(blt_in.type) is ZCodeType:
                raise Redeclared(Function(),ast.name.name)
        param_env = []
        for param in ast.param:
            param_env.append(param)
        paramType = []
        for param in param_env:
            paramType.append(getType(param.varType))
        seen_names = []
        for param in param_env:
            if param.name.name in seen_names:
                raise Redeclared(Parameter(), param.name.name)
            seen_names.append(param.name.name)
        context.ref_envs[0] = [ast]
        context.func_params = param_env
        context.funcs = context.funcs + [ast]
        if ast.body:
            if type(ast.body) is Block: 
                if len(ast.body.stmt) > 0:
                    if isImplicit == True and func_type is not None and func_type is not VoidType():
                        if type(ast.body.stmt[-1]) is not Return:
                            raise TypeMismatchInStatement(ast)
                        elif ast.body.stmt[-1].expr is None:
                            raise TypeMismatchInStatement(ast)
                        self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,func_type),None))
                    else:
                        self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,VoidType()),None))
            elif type(ast.body) is Return:
                if ast.body.expr is not None:
                    if isImplicit == True and func_type is not None and func_type is not VoidType():
                        self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,func_type),None))
                self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,VoidType()),None))
            else:
                self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,VoidType()),None))
            self.visit(ast.body,State(context.ref_envs,context.funcs,context.built_ins,ast,0,context.implicit_func,param_env,context.typeInferred))

        #if this ast not have body
        elif not ast.body:
            context.implicit_func = context.implicit_func + [Symbol(ast.name.name,ZCodeType(paramType,None),None)]
        return context
    def visitBlock(self, ast: Block, context: State):
        context.in_func = ast
        in_params = []

        for stmt in ast.stmt:
            # Visit each stmt in block
            self.visit(stmt, State([in_params] + context.ref_envs, context.funcs, context.built_ins, context.in_func, context.isInLoop,context.implicit_func,context.func_params,context.typeInferred))
        return context   
    def visitBinaryOp(self, ast: BinaryOp,  context:State):
        lhs = self.visit(ast.left, context)
        rhs = self.visit(ast.right, context)
        lhs_name = getName(ast.left)
        rhs_name = getName(ast.right)
        ltype = getType(lhs)
        rtype = getType(rhs)
        if ltype is None:
            ltype = rtype
        elif rtype is None:
            rtype = ltype

        if type(ltype) is ArrayType:
            ltype = ltype.eleType
        if type(rtype) is ArrayType:
            rtype = rtype.eleType
        if ast.op in ["+", "-", "*", "/","%"]:
            if ltype is None and rtype is None:
                ltype = rtype = NumberType()
            if lhs_name:
                    if type(ast.left) is CallExpr:
                        updateTypeOfFunction(lhs_name,NumberType(),context.implicit_func)                    
                    if type(ast.left) is Id:
                        updateTypeOfVariable(lhs_name,ltype,self.glob_env)
                        updateTypeoDynamicVariable(lhs_name,ltype,context.ref_envs[0])
            if rhs_name:
                    if type(ast.right) is CallExpr:
                        updateTypeOfFunction(rhs_name,NumberType(),context.implicit_func)
                    if type(ast.right) is Id:
                        updateTypeOfVariable(rhs_name,NumberType(),self.glob_env)
                        updateTypeoDynamicVariable(rhs_name,NumberType(),context.ref_envs[0])
            if type(ltype) is not NumberType or type(rtype) is not NumberType:
                raise TypeMismatchInExpression(ast)
            else :
                return NumberType()
        if ast.op in ["<", "<=", ">", ">=", "!=", "="]:
            if ltype is None and rtype is None:
                ltype = rtype = NumberType()
            if lhs_name:
                    if type(ast.left) is CallExpr:
                        updateTypeOfFunction(lhs_name,NumberType(),context.implicit_func)
                    if type(ast.left) is Id:
                        updateTypeOfVariable(lhs_name,NumberType(),self.glob_env)
                        updateTypeoDynamicVariable(lhs_name,NumberType(),context.ref_envs[0])
            if rhs_name:
                    if type(ast.right) is CallExpr:
                        updateTypeOfFunction(rhs_name,NumberType(),self.glob_env)
                    if type(ast.right) is Id:
                        updateTypeOfVariable(rhs_name,NumberType(),self.glob_env)
                        updateTypeoDynamicVariable(rhs_name,NumberType(),context.ref_envs[0])
            if type(ltype) is not NumberType or type(rtype) is not NumberType:
                raise TypeMismatchInExpression(ast)
            else :
                return BoolType()
        if ast.op == "==":
            if ltype is None and rtype is None:
                ltype = rtype = StringType()
            if lhs_name:
                    if type(ast.left) is CallExpr:
                        updateTypeOfFunction(lhs_name,ltype,context.implicit_func)
                    if type(ast.left) is Id:
                        updateTypeOfVariable(lhs_name,StringType(),self.glob_env)
                        updateTypeoDynamicVariable(lhs_name,StringType(),context.ref_envs[0])
            if rhs_name:
                    if type(ast.right) is CallExpr:
                        updateTypeOfFunction(rhs_name,StringType(),context.implicit_func)
                    if type(ast.right) is Id:
                        updateTypeOfVariable(rhs_name,StringType(),self.glob_env)
                        updateTypeoDynamicVariable(rhs_name,StringType(),context.ref_envs[0])
            if type(ltype) is not StringType or type(rtype) is not StringType:
                raise TypeMismatchInExpression(ast)
            else :
                return BoolType()
        if ast.op  == "..." :
            if ltype is None and rtype is None:
                ltype = rtype = StringType()
            if lhs_name:
                    if type(ast.left) is CallExpr:
                        updateTypeOfFunction(lhs_name,StringType(),context.implicit_func)
                    if type(ast.left) is Id:
                        updateTypeOfVariable(lhs_name,StringType(),self.glob_env)
                        updateTypeoDynamicVariable(lhs_name,rtype,context.ref_envs[0])
            if rhs_name:
                    if type(ast.right) is CallExpr:
                        updateTypeOfFunction(rhs_name,StringType(),context.implicit_func)
                    if type(ast.right) is Id:
                        updateTypeOfVariable(rhs_name,StringType(),self.glob_env)
                        updateTypeoDynamicVariable(rhs_name,StringType(),context.ref_envs[0])
            if type(ltype) is not StringType or type(rtype) is not StringType:
                raise TypeMismatchInExpression(ast)
            else :
                return StringType()
        if ast.op in ["and","or"]:
            if ltype is None and rtype is None:
                ltype = rtype = BoolType()
            if lhs_name:
                    if type(ast.left) is CallExpr:
                        updateTypeOfFunction(lhs_name,BoolType(),context.implicit_func)
                    if type(ast.left) is Id:
                        updateTypeOfVariable(lhs_name,BoolType(),self.glob_env)
                        updateTypeoDynamicVariable(lhs_name,BoolType(),context.ref_envs[0])
            if rhs_name:
                    if type(ast.right) is CallExpr:
                        updateTypeOfFunction(rhs_name,BoolType(),context.implicit_func)
                    if type(ast.right) is Id:
                        updateTypeOfVariable(rhs_name,BoolType(),self.glob_env)
                        updateTypeoDynamicVariable(rhs_name,BoolType(),context.ref_envs[0])
            if type(ltype) is not BoolType or type(rtype) is not BoolType:
                raise TypeMismatchInExpression(ast)
            else :
                return BoolType()
            


    def visitUnaryOp(self, ast: UnaryOp, context:State):
        value = self.visit(ast.operand, context)
        name = getName(ast.operand)
            
        valType = getType(value)
        if ast.op == "not" :
            if valType is None:
                valType = BoolType()
                if name:
                    if type(ast.operand) is CallExpr:
                        updateTypeOfFunction(name,BoolType(),context.implicit_func)
                    if type(ast.operand) is Id:
                        updateTypeOfVariable(name,BoolType(),self.glob_env)
                        updateTypeoDynamicVariable(name,BoolType(),context.ref_envs[0])
            if type(valType) is not BoolType:
                raise TypeMismatchInExpression(ast)
            return BoolType()
        if ast.op == "-" :
            if valType is None:
                valType = NumberType()
                if name:
                    if type(ast.operand) is CallExpr:
                        updateTypeOfFunction(name,NumberType(),context.implicit_func)
                    if type(ast.operand) is Id:
                        updateTypeOfVariable(name,NumberType(),self.glob_env)
                        updateTypeoDynamicVariable(name,NumberType(),context.ref_envs[0])
            if type(valType) is not NumberType:
                raise TypeMismatchInExpression(ast)
            else :
                return NumberType()


    def visitCallExpr(self, ast: CallExpr,  context: State):
        arg_len = len(ast.args)
        for func in context.funcs:
            if func.name == ast.name:
                if func.param is None:
                    if arg_len != 0:
                        raise TypeMismatchInExpression(ast)
                if func.param is not None:

                    if len(func.param) != arg_len:
                        raise TypeMismatchInExpression(ast)
                    for i in range(arg_len):
                        func_param_type = getType(func.param[i])
                        arg_type = getType(self.visit(ast.args[i],context))
                        if type(func_param_type) is ArrayType:
                            func_param_type = func_param_type.eleType
                        if type(arg_type) is ArrayType:
                            arg_type = arg_type.eleType
                        if arg_type is None:
                            if type(ast.args[i]) is Id:
                                for ref_env in context.ref_envs:
                                    for id in ref_env:
                                        if id.name.name == ast.args[i].name:
                                            id.varType = func_param_type
                                            break
                            if type(ast.args[i]) is CallExpr:
                                for func in self.glob_env:
                                    if func.name == ast.args[i].name.name:
                                        func.type.rettype = func_param_type
                                        break
                                for func in context.implicit_func:
                                    if func.name == ast.args[i].name.name:
                                        func.type.rettype = func_param_type
                                        break
                            arg_type = func_param_type
                        if arg_type is VoidType:
                            raise TypeMismatchInExpression(ast)
                        if str(func_param_type) != str(arg_type):
                            raise TypeMismatchInExpression(ast)
        for func in self.glob_env:
            if func.name == ast.name.name:
                if type(func.type) is ZCodeType:
                    return func.type.rettype
        for func in context.implicit_func:
            if func.name == ast.name.name:
                if context.typeInferred is not None:
                    func.type.rettype = context.typeInferred
                return context.typeInferred
        raise Undeclared(Function(), ast.name.name)
        

    def visitId(self, ast: Id, context: State):
        for ref_env in context.ref_envs:
            for id in ref_env:
                if ast.name == id.name.name:
                    if type(id) is FuncDecl: raise Undeclared(Identifier(), ast.name)
                    return id.varType
        for id in context.funcs:
            if ast.name == id.name.name:
                raise Undeclared(Identifier(), ast.name)
        for id in context.func_params:
            if ast.name == id.name.name:
                if type(id) is ArrayType:
                    return id.eleType
                return id.varType
        for id in self.glob_env:
            if ast.name == id.name:
                if type(id) is ArrayType:
                    return id.eleType
                return id.type
        raise Undeclared(Identifier(), ast.name)   

    def visitArrayCell(self, ast: ArrayCell,context:State):
        # arr: Expr
        # idx: List[Expr]
        size = len(ast.idx)
        arr = self.visit(ast.arr, context)
        len_param = 0
        if type(arr) is CallExpr:
            len_param = len(arr.args)
        for ref_env in context.ref_envs:
            for id in ref_env:
                if ast.arr == id.name:
                    if id.varType is None:
                        raise TypeCannotBeInferred(context.in_func)
                    if type(id.varType) is not ArrayType:
                        raise TypeMismatchInExpression(ast)
                    if len(id.varType.size) < size:
                        raise TypeMismatchInExpression(ast)
        for id in context.func_params:
            if ast.arr.name == id.name.name:
                if type(id.varType) is not ArrayType:
                    raise TypeMismatchInExpression(ast)
                if len(id.varType.size) < size:
                    raise TypeMismatchInExpression(ast)
 
        for id in self.glob_env:
            if type(ast.arr) is Id:
                if ast.arr.name == id.name:
                    if id.type is None:
                        raise TypeCannotBeInferred(context.in_func)
                    if type(id.type) is ArrayType:
                        if len(id.type.size) < size:
                            raise TypeMismatchInExpression(ast)
            if type(ast.arr) is CallExpr:
                if ast.arr.name.name == id.name:
                    if id.type.rettype is VoidType:
                        raise TypeCannotBeInferred(context.in_func)
                    if type(id.type.rettype) is not ArrayType:
                        raise TypeMismatchInExpression(ast)
                    if type(id.type.rettype) is ArrayType:
                        if len(id.type.rettype.size) < size:
                            raise TypeMismatchInExpression(ast)
                    elif len(id.type.starttype) < len_param:
                        raise TypeMismatchInExpression(ast)
        
        type_arr = None
        for i in ast.idx:
            idx = self.visit(i, context)
            type_arr = getType(idx)
            if type(type_arr) is ArrayType:
                type_arr = type_arr.eleType
            if type(type_arr) is not NumberType:
                raise TypeMismatchInExpression(ast)
        if type_arr is None:
            raise TypeCannotBeInferred(context.in_func)
        return ArrayType([float(size)], type_arr)
    def visitIf(self, ast: If,  context):
        # expr: Expr
        # thenStmt: Stmt
        # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
        # elseStmt: Stmt = None  # None if there is no else branch
        context.in_func = ast
        context.typeInferred = BoolType()
        if_type = getType(self.visit(ast.expr, context))
        if if_type is None and type(ast.expr) is Id:

            for id in context.ref_envs[0]:
                if ast.expr.name == id.name.name:
                    id.varType = BoolType()
                    break
            for id in self.glob_env:
                if ast.expr.name == id.name:
                    id.type = BoolType()
                    break
            if_type = BoolType()           
        if type(if_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, context)
        if ast.elifStmt:
            for expr,stmt in ast.elifStmt:
                expr_type = getType(self.visit(expr, context))
                if type(expr_type) is not BoolType:
                    raise TypeMismatchInStatement(ast)
                self.visit(stmt, context)
        if ast.elseStmt:
            self.visit(ast.elseStmt, context)
        


    def visitFor(self, ast: For, context: State):
        """# name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt"""
        # Initialize loop variable
        context.in_func = ast
        id_type = getType(self.visit(ast.name, context))
        if id_type is None:
            id_type = NumberType()
            for ref_env in context.ref_envs:
                for id in ref_env:
                    if ast.name.name == id.name.name:
                        id.varType = id_type
                        break
        if type(id_type) is not NumberType: 
            raise TypeMismatchInStatement(ast) 
        # Check loop condition
        cond_type = getType(self.visit(ast.condExpr, context))
        if type(cond_type) is not BoolType:
            raise TypeMismatchInStatement(ast)
        upd_type = getType(self.visit(ast.updExpr, context))
        if type(upd_type) is not NumberType:
            raise TypeMismatchInStatement(ast)
        # Loop body
        new_context = State(context.ref_envs,context.funcs,context.built_ins,ast,1,context.implicit_func,context.func_params,context.typeInferred)
        self.visit(ast.body, new_context)
        
    def visitContinue(self, ast: Continue,  context):
        if context.isInLoop == 0:
            raise MustInLoop(ast)
        return context
        

    def visitBreak(self, ast: Break,  context):
        if context.isInLoop == 0:
            raise MustInLoop(ast)
        return context
    def visitReturn(self, ast: Return,  context: State):
        context.in_func = ast
        if ast.expr is None:
            return VoidType()
        rettype = getType(self.visit(ast.expr, State(context.ref_envs,context.funcs,context.built_ins,ast,0,context.implicit_func,context.func_params,context.typeInferred)))
        context.typeInferred = rettype
        if type(rettype) is ArrayType and type(ast.expr) is ArrayCell:
            rettype = rettype.eleType
        if len(context.ref_envs) > 1:
            for func in self.glob_env:
                if func.name == context.ref_envs[1][0].name.name:
                    if type(func.type.rettype) is not VoidType and str(rettype) != str(func.type.rettype):
                        raise TypeMismatchInStatement(ast)
            updateTypeOfFunction(context.ref_envs[1][0].name.name,rettype,self.glob_env)
        else:
            for func in self.glob_env:
                if func.name == context.ref_envs[0][0].name.name:
                    if type(func.type.rettype) is not VoidType and str(rettype) != str(func.type.rettype):
                        raise TypeMismatchInStatement(ast)
            updateTypeOfFunction(context.ref_envs[0][0].name.name,rettype,self.glob_env)
        if rettype is None :
            raise TypeCannotBeInferred(ast)
        if type(rettype) is ArrayType:
            if rettype.eleType is None:
                raise TypeCannotBeInferred(ast)
        return rettype

    def visitAssign(self, ast: Assign,  context: State):
        context.in_func = ast
        left_ast = ast.lhs
        right_ast = ast.rhs
        ltype = getType(self.visit(ast.lhs, context))
        rtype = getType(self.visit(ast.rhs, context))
        if ltype is None and rtype is None:
            raise TypeCannotBeInferred(ast)
        if ltype is None and type(rtype) is ArrayType:
            if rtype.eleType is None:
                raise TypeCannotBeInferred(ast) 
        if ltype is None:
            ltype = rtype
        elif rtype is None:
            rtype = ltype
 
        if type(left_ast) is Id:
            for ref_env in context.ref_envs:
                for id in ref_env:
                    if left_ast.name == id.name.name:
                        id.varType = ltype
            for id in self.glob_env:
                if left_ast.name == id.name:
                    id.type = ltype  
        if type (right_ast) is Id:
            for id in context.ref_envs[0]:
                if right_ast.name == id.name.name:
                    id.varType = ltype
            for id in self.glob_env:
                if right_ast.name == id.name:
                    id.type = ltype      
        if type(ltype) is ArrayType and type(rtype) is ArrayType:
            size = ltype.size
            if rtype.size != size:
                raise TypeMismatchInStatement(ast)
            if rtype.eleType is None:
                rtype.eleType = ltype.eleType
                context.typeInferred = ltype.eleType
            if str(ltype.eleType) != str(rtype.eleType):
                raise TypeMismatchInStatement(ast)
        if ltype is VoidType():
            raise TypeMismatchInStatement(ast)
        if type(ltype) is ArrayType and type(rtype) is not ArrayType and type(ast.lhs) is ArrayCell:
            ltype = ltype.eleType
        if type(ltype) is not ArrayType and type(rtype) is ArrayType and type(ast.rhs) is ArrayCell:
            rtype = rtype.eleType
        if str(ltype) != str(rtype):    
            raise TypeMismatchInStatement(ast)
        return context
        
    def visitCallStmt(self, ast: CallStmt,  context):
        arg_len = len(ast.args)
        for func in self.glob_env:
            if func.name == ast.name.name:
                if arg_len != len(func.type.starttype):
                    raise TypeMismatchInStatement(ast)
                if type(func.type.rettype) is not VoidType:
                    raise TypeMismatchInStatement(ast)
                for i in range(arg_len):
                    func_param_type = getType(func.type.starttype[i])
                    if type(func_param_type) is ArrayType:
                        func_param_type = func_param_type.eleType
                    arg_type = getType(self.visit(ast.args[i],context))

                    if type(arg_type) is ArrayType:
                        arg_type = arg_type.eleType
                    if arg_type is None:
                        for ref_env in context.ref_envs:
                            for id in ref_env:
                                if type(ast.args[i]) is Id:
                                    if ast.args[i].name == id.name.name:
                                        id.varType = func_param_type
                                        break
                        if type(ast.args[i]) is CallExpr:
                            for id in self.glob_env:
                                if ast.args[i].name.name == id.name:
                                    id.type.rettype = func_param_type
                                    break
                        arg_type = func_param_type
                    if type(arg_type) is VoidType:
                        raise TypeMismatchInStatement(ast)
                    if str(func_param_type) != str(arg_type):
                        raise TypeMismatchInStatement(ast)
                return context
                
        for func in context.implicit_func:
            if func.name == ast.name.name:
                return context
        raise Undeclared(Function(), ast.name.name)

    
    def visitNumberLiteral(self, ast, context):
        return NumberType()
    def visitNumberType(self, ast, context):
        return NumberType()
    
    def visitBooleanLiteral(self,ast, context):
        return BoolType()
    
    def visitBoolType(self, ast,  context):
        return BoolType()
    
    def visitStringLiteral(self, ast,  context):
        return StringType()

    def visitStringType(self, ast,  context):
        return StringType()
    
    def visitArrayLiteral(self, ast, context:State):
        # value: List[Expr]
        #check if every element in the array has the same type
        first_ele_type = getType(self.visit(ast.value[0],context))
        actual_type = None
        size = len(ast.value)
        actual_size = [float(size)]
        for i in range(1,len(ast.value)):
            index_ele_type = getType(self.visit(ast.value[i],context))
            #print("index",index_ele_type)
            if first_ele_type is None:
                first_ele_type = index_ele_type
            elif index_ele_type is None:
                index_ele_type = first_ele_type
            if type(ast.value[0]) is Id:
                for ref_env in context.ref_envs:
                    for id in ref_env:
                        if type(ast.value[0]) is Id:
                            if ast.value[0].name == id.name.name:
                                if context.typeInferred is not None and first_ele_type is None:
                                    id.varType = context.typeInferred
                                    break
                                id.varType = first_ele_type
                                break
                for id in self.glob_env:
                    if ast.value[0].name == id.name:
                        if context.typeInferred is not None and first_ele_type is None:
                                id.type = context.typeInferred
                                break
                        id.type = first_ele_type
                        break
            if type(ast.value[0]) is CallExpr:
                for id in self.glob_env:
                    if ast.value[0].name.name == id.name:
                        if context.typeInferred is not None and first_ele_type is None:
                                id.type.rettype = context.typeInferred
                                break
                        id.type.rettype = first_ele_type
                        break
            if type(ast.value[i]) is Id:
                for ref_env in context.ref_envs:
                    for id in ref_env:
                        if type(ast.value[i]) is Id:
                            if ast.value[i].name == id.name.name:
                                if context.typeInferred is not None and first_ele_type is None:
                                    id.varType = context.typeInferred
                                    break
                                id.varType = first_ele_type
                                break
                for id in self.glob_env:
                    if ast.value[i].name == id.name:
                        if context.typeInferred is not None and first_ele_type is None:
                                id.type = context.typeInferred
                                break
                        id.type = first_ele_type
                        break
            if type(ast.value[i]) is CallExpr:
                for id in self.glob_env:
                    if ast.value[i].name.name == id.name:
                        if context.typeInferred is not None and first_ele_type is None:
                                id.type.rettype = context.typeInferred
                                break
                        id.type.rettype = first_ele_type
                        break
            if str(first_ele_type) != str(index_ele_type):
                raise TypeMismatchInExpression(ast)
        if type(first_ele_type) is ArrayType:
            if first_ele_type.eleType is not None:
                actual_type = self.visit(first_ele_type.eleType,context)
                actual_size = actual_size + first_ele_type.size
            else:
                actual_size = actual_size + first_ele_type.size
                actual_type = first_ele_type.eleType
        else:
            actual_type = first_ele_type
        return ArrayType(actual_size,actual_type)
    def visitArrayType(self,ast: ArrayType,context):
        pass
   
    

    

    