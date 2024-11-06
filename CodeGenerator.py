#MSSV : 2110242
from Emitter import Emitter
from functools import reduce
from main.zcode.checker.StaticError import *
from Frame import Frame
from abc import ABC
from Visitor import *
from AST import *

##Global var -> static var
##function -> static method 
#local var, param -> local var
class ZCodeType:
    def __init__(self, starttype, rettype):
        self.starttype = starttype
        self.rettype = rettype
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
        return None
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
class Symbol:
    def __init__(self, name, type, value = None,isDynamic = False, out = None):
        self.name = name
        self.type = type
        self.value = value
        self.isDynamic = isDynamic
        self.out = out
class SubBody():
    def __init__(self, frame, sym,typeInferred = None,isCell = False):
        self.frame = frame
        self.sym = sym
        self.typeInferred = typeInferred
        self.isCell = isCell
        


class Access():
    def __init__(self, frame, sym, isLeft, isFirst=False, typeInferred = None, isCell = False):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean
        #typeInferred: Type
        #is in cell
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
        self.typeInferred = typeInferred
        self.isCell = isCell

class Val(ABC):
    pass


class Index(Val):
    def __init__(self, value):
        self.value = value


class CName(Val):
    def __init__(self, value):
        self.value = value

def returnType(ast):
    if type(ast) is NumberType or type(ast) is NumberLiteral:
        return NumberType()
    if type(ast) is BoolType or type(ast) is BooleanLiteral:
        return BoolType()
    if type(ast) is StringType or type(ast) is StringLiteral:
        return StringType()
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

global_environment = []
class StaticChecker(BaseVisitor):
    libName = "io"
    glob_env = [Symbol("readNumber",ZCodeType([],NumberType()),CName(libName)),
                Symbol("writeNumber",ZCodeType([NumberType()],VoidType()),CName(libName)),
                Symbol("readBool",ZCodeType([],BoolType()),CName(libName)),
                Symbol("writeBool",ZCodeType([BoolType()],VoidType()),CName(libName)),
                Symbol("readString",ZCodeType([], StringType()),CName(libName)),
                Symbol("writeString",ZCodeType([StringType()],VoidType()),CName(libName))]
    def __init__(self, ast):
        self.ast = ast
    def check(self):
        return self.visitProgram(self.ast,self.glob_env)
    def getGlobal(self):
        return self.glob_env
    def visitProgram(self, ast: Program, context):
        self.glob_env = self.glob_env[0:6]
        context = State([[]],[],self.glob_env,None,0,[])
        #hasEntry = False
        reduce(lambda acc,ele: self.visit(ele,acc), ast.decl, context)     
        global_environment.clear()
        for func in self.glob_env:
            global_environment.append(func)
        return ast
    def visitVarDecl(self, ast: VarDecl,context:State):
        context.ref_envs[0][:0] = [ast]
        if len(context.ref_envs) == 1:
            self.glob_env.append(Symbol(ast.name.name, ast.varType,CName("ZCodeClass")))
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
                    var_type = var_type.eleType
                if type(initType) is ArrayType:
                    if initType.eleType is not None:
                        initType = self.visit(initType.eleType,context)
                    else:
                        initType = initType.eleType
                elif initType is None and ast.varType is not None:
                    if type(ast.varInit) is CallExpr:
                        for func in context.implicit_func:
                            if ast.varInit.name == func.name and func.type.rettype is None:
                                func.type.rettype = ast.varType
            else:
                initType = self.visit(ast.varInit,context)
                ast.varType = initType
                for var in self.glob_env:
                    if var.name == ast.name.name:
                        var.type = ast.varType
        return context
    def visitFuncDecl(self, ast: FuncDecl, context:State):
        isImplicit = False
        func_type = None
        for func in context.implicit_func:
            if func.name == ast.name.name:
                isImplicit = True
                func_type = func.type.rettype
                break
        param_env = []
        for param in ast.param:
            param_env.append(param)
        paramType = []
        for param in param_env:
            paramType.append(getType(param.varType))
        context.ref_envs[0] = [ast]
        context.func_params = param_env
        context.funcs = context.funcs + [ast]
        if ast.body:
            if type(ast.body) is Block: 
                if len(ast.body.stmt) > 0:
                    if isImplicit == True and func_type is not None and func_type is not VoidType():
                        self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,func_type),CName("ZCodeClass")))
                    else:
                        self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,VoidType()),CName("ZCodeClass")))
            elif type(ast.body) is Return:
                if ast.body.expr is not None:
                    if isImplicit == True and func_type is not None and func_type is not VoidType():
                        self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,func_type),None))
                self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,VoidType()),CName("ZCodeClass")))
            else:
                self.glob_env.append(Symbol(ast.name.name,ZCodeType(paramType,VoidType()),CName("ZCodeClass")))
            self.visit(ast.body,State(context.ref_envs,context.funcs,context.built_ins,ast,0,context.implicit_func,param_env,context.typeInferred))

        #if this ast not have body
        elif not ast.body:
            context.implicit_func = context.implicit_func + [Symbol(ast.name.name,ZCodeType(paramType,None),None)]
        return context
    def visitBlock(self, ast: Block, context: State):
        in_params = []
        for stmt in ast.stmt:
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
        for func in self.glob_env:
            if func.name == ast.name.name:
                if type(func.type) is ZCodeType:
                    return func.type.rettype
        for func in context.implicit_func:
            if func.name == ast.name.name:
                if context.typeInferred is not None:
                    func.type.rettype = context.typeInferred
                return context.typeInferred     
    def visitId(self, ast: Id, context: State):
        for ref_env in context.ref_envs:
            for id in ref_env:
                if ast.name == id.name.name:
                    if type(id) is FuncDecl: raise Undeclared(Identifier(), ast.name)
                    return id.varType

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
        # raise Undeclared(Identifier(), ast.name)   

    def visitArrayCell(self, ast: ArrayCell,context:State):
        # arr: Expr
        # idx: List[Expr]
        size = len(ast.idx)
        type_arr = None
        for i in ast.idx:
            idx = self.visit(i, context)
            type_arr = getType(idx)
            if type(type_arr) is ArrayType:
                type_arr = type_arr.eleType
        typ = self.visit(ast.arr, context)
        typ_size = len(typ.size)
        if type(typ) is ArrayType and typ_size == size:
            typ = typ.eleType
        elif type(typ) is ArrayType and typ_size > size:
            res_size = typ.size[size:]
            typ = ArrayType(res_size, typ.eleType)
        return typ
    def visitIf(self, ast: If,  context):
        # expr: Expr
        # thenStmt: Stmt
        # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
        # elseStmt: Stmt = None  # None if there is no else branch
        #context.in_func = ast
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
        if if_type is None and type(ast.expr) is CallExpr:
            for id in context.ref_envs[0]:
                if ast.expr.name == id.name.name:
                    id.varType = BoolType()
                    break
            for id in self.glob_env:
                if ast.expr.name.name == id.name:
                    id.type = BoolType()
                    break
            if_type = BoolType()        
        # if type(if_type) is not BoolType:
        #     raise TypeMismatchInStatement(ast)
        self.visit(ast.thenStmt, context)
        if ast.elifStmt:
            for expr,stmt in ast.elifStmt:
                self.visit(stmt, context)
        if ast.elseStmt:
            self.visit(ast.elseStmt, context)
        


    def visitFor(self, ast: For, context: State):
        """# name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt"""
        # Initialize loop variable
        #context.in_func = ast
        id_type = getType(self.visit(ast.name, context))
        if id_type is None:
            id_type = NumberType()
            for ref_env in context.ref_envs:
                for id in ref_env:
                    if ast.name.name == id.name.name:
                        id.varType = id_type
                        break
        new_context = State(context.ref_envs,context.funcs,context.built_ins,ast,1,context.implicit_func,context.func_params,context.typeInferred)
        self.visit(ast.body, new_context)
        
    def visitContinue(self, ast: Continue,  context):
        return context
        
    def visitBreak(self, ast: Break,  context):
        return context
    def visitReturn(self, ast: Return,  context: State):
        #context.in_func = ast
        if ast.expr is None:
            return VoidType()
        rettype = getType(self.visit(ast.expr, State(context.ref_envs,context.funcs,context.built_ins,ast,0,context.implicit_func,context.func_params,context.typeInferred)))
        context.typeInferred = rettype
        if type(rettype) is ArrayType and type(ast.expr) is ArrayCell:
            rettype = rettype.eleType
        if len(context.ref_envs) > 1:
            updateTypeOfFunction(context.ref_envs[1][0].name.name,rettype,self.glob_env)
        else:
            updateTypeOfFunction(context.ref_envs[0][0].name.name,rettype,self.glob_env)
        return rettype

    def visitAssign(self, ast: Assign,  context: State):
        left_ast = ast.lhs
        right_ast = ast.rhs
        ltype = getType(self.visit(ast.lhs, context))
        rtype = getType(self.visit(ast.rhs, context))
        if ltype is None:
            ltype = rtype
        elif rtype is None:
            rtype = ltype
        if type(left_ast) is Id:
            for ref_env in context.ref_envs:
                for id in ref_env:
                    if left_ast.name == id.name.name and id.modifier == "dynamic":
                        id.varType = rtype
                        id.varInit = right_ast
            for id in self.glob_env:
                if left_ast.name == id.name:
                    id.type = rtype  
        if type (right_ast) is Id:
            for id in context.ref_envs[0]:
                if right_ast.name == id.name.name:
                    id.varType = ltype
            for id in self.glob_env:
                if right_ast.name == id.name:
                    id.type = ltype      
        if type(ltype) is ArrayType and type(rtype) is ArrayType:
            if rtype.eleType is None:
                rtype.eleType = ltype.eleType
                context.typeInferred = ltype.eleType
        if type(ltype) is ArrayType and type(rtype) is not ArrayType and type(ast.lhs) is ArrayCell:
            ltype = ltype.eleType
        if type(ltype) is not ArrayType and type(rtype) is ArrayType and type(ast.rhs) is ArrayCell:
            rtype = rtype.eleType
        return context
        
    def visitCallStmt(self, ast: CallStmt,  context):
        arg_len = len(ast.args)
        for func in self.glob_env:
            if func.name == ast.name.name:
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
            # if str(first_ele_type) != str(index_ele_type):
            #     raise TypeMismatchInExpression(ast)
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
class CodeGenerator:
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("readNumber",ZCodeType([],NumberType()),CName(self.libName)),
                Symbol("writeNumber",ZCodeType([NumberType()],VoidType()),CName(self.libName)),
                Symbol("readBool",ZCodeType([],BoolType()),CName(self.libName)),
                Symbol("writeBool",ZCodeType([BoolType()],VoidType()),CName(self.libName)),
                Symbol("readString",ZCodeType([], StringType()),CName(self.libName)),
                Symbol("writeString",ZCodeType([StringType()],VoidType()),CName(self.libName))]

    def gen(self, ast, path):
        # ast: AST
        # dir_: String
        gl = self.init()
        new_ast = StaticChecker(ast).check()
        gc = CodeGenVisitor(new_ast, gl, path)
        gc.visit(ast, None)
       
        
class CodeGenVisitor(BaseVisitor):
 
    def __init__(self, astTree, env, path):
        self.astTree = astTree
        self.env = env
        self.path = path
        self.className = 'ZCodeClass'
        self.emit = Emitter(self.path + "/" + self.className + ".j")
    def visitProgram(self, ast, c):
        self.env = global_environment
        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        e = SubBody(None, self.env)
        access_field = Access(Frame("ZCodeClass",None),e.sym,True,True)
        for x in ast.decl:
            if type(x) is VarDecl:
                e = self.visit(x, access_field)
        for x in ast.decl:
            if type(x) is FuncDecl:
                e = self.visit(x, e) 
        self.genMETHOD(FuncDecl(Id("<init>"),[],Block([])),self.env,Frame("<init>",VoidType()))
        self.emit.emitEPILOG()
        return c
    def visitFuncDecl(self, ast, o):
        returnType = None
        for func in self.env:
            if func.name == ast.name.name:
                returnType = func.type.rettype
                break
        frame = Frame(ast.name.name, returnType)
        if ast.body:
            self.genMETHOD(ast, o.sym, frame)
        return SubBody(None, o.sym)
    def visitVarDecl(self, ast, o):
        isDynamic = False
        if ast.modifier == "dynamic":
            isDynamic = True
        if type(o) is not SubBody:
            varType = None
            if isDynamic:
               for var in o.sym:
                   if var.name == ast.name.name:
                       varType = var.type
                       break
            else:
               varType = ast.varType
            if type(varType) is ArrayType and ast.varInit is None:
                sizes = varType.size
                init_values = [NumberLiteral(0.0) for _ in range(int(sizes[-1]))]
                for _ in range(len(sizes) - 2, -1, -1):
                    init_values = [ArrayLiteral(init_values) for _ in range(int(sizes[_]))]
                ast.varInit = ArrayLiteral(init_values)
            elif type(varType) is NumberType and ast.varInit is None:
                ast.varInit = NumberLiteral(0.0)
            jsm = self.emit.emitATTRIBUTE(ast.name.name, varType,ast.varInit)
            self.emit.printout(jsm)
            result = SubBody(o.frame, o.sym+ [Symbol(ast.name.name,varType, CName(self.className)),isDynamic])
        else:
            varType = None
            if isDynamic:
               for var in o.sym:
                   if var.name == ast.name.name:
                       varType = var.type
                       break
            else:
               varType = ast.varType
            if type(varType) is ArrayType and ast.varInit is None:
                sizes = varType.size
                init_values = [NumberLiteral(0.0) for _ in range(int(sizes[-1]))]
                for _ in range(len(sizes) - 2, -1, -1):
                    init_values = [ArrayLiteral(init_values) for _ in range(int(sizes[_]))]
                ast.varInit = ArrayLiteral(init_values)
            if not isDynamic and ast.varInit is not None:
                jsm = self.emit.emitVAR(o.frame.getCurrIndex(), ast.name.name, varType, o.frame.getStartLabel(), o.frame.getEndLabel(), o.frame)
                self.emit.printout(jsm)
            result = SubBody(o.frame, [Symbol(ast.name.name,varType, Index(o.frame.getNewIndex()),isDynamic)]+ o.sym)
            if ast.varInit:
                self.visit(Assign(ast.name, ast.varInit), result)
        return result
    def genMETHOD(self, consdecl, o, frame):
        name = consdecl.name.name
        returnType = None
        startType = []
        for func in self.env:
            if func.name == name:
                returnType = func.type.rettype
                startType = func.type.starttype
                break
        
        isInit = returnType is None
        isMain = name == "main" and len(consdecl.param) == 0 and type(returnType) is VoidType
 
        methodName = None
        if isInit:
            returnType = VoidType()
            methodName = "<init>"
        else:
            methodName = name
        intype = [ArrayType([0], StringType())] if isMain else startType
        mtype = ZCodeType(intype, returnType)

        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))

        frame.enterScope(True)

        glenv = o

        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        elif isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayType(
                [0], StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            for dec in self.astTree.decl:
                if type(dec) is VarDecl:
                    if dec.varInit is not None:
                        consdecl.body.stmt = [Assign(dec.name, dec.varInit)] + consdecl.body.stmt

        body = consdecl.body
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this",ClassType(self.className),0,frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        env = SubBody(frame, o)
        for param in consdecl.param:
            env = self.visit(VarDecl(param.name,param.varType), env)
        if consdecl.body:
            if type(body) is Block:
                env = self.visit(consdecl.body, env)
            if type(body) is Return:
                self.visit(body, env)

        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if type(returnType) is VoidType:
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        else:
            self.emit.printout(self.emit.emitRETURN(returnType, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        frame.exitScope()
    def visitNumberLiteral(self, ast, o):
        return self.emit.emitPUSHCONST(str(ast.value),NumberType(), o.frame), NumberType()
    def visitBooleanLiteral(self, ast, o):
        return self.emit.emitPUSHICONST(int(ast.value), o.frame), BoolType()
    def visitStringLiteral(self, ast, o):
        return self.emit.emitPUSHCONST('"' + str(ast.value) + '"',StringType() ,o.frame), StringType()

    def visitBreak(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getBreakLabel(), o.frame))
    def visitContinue(self, ast, o):
        self.emit.printout(self.emit.emitGOTO(o.frame.getContinueLabel(), o.frame))

    def visitAssign(self, ast, o):
        array_cell, data_type = (self.visit(ast.lhs, (Access(o.frame, o.sym, True, True), ast.rhs))) if isinstance(ast.lhs, ArrayCell) else ("", VoidType())
        if array_cell != "":
            self.emit.printout(array_cell)
            return o
        
        left_access = Access(o.frame, o.sym, True, False)
        right_access = Access(o.frame, o.sym, False, False)
        right_jsm, typr = self.visit(ast.rhs, right_access) ## need to return type ? if visit the ID
        if type(ast.lhs) is Id:
            for func in o.sym:
                if type(func) is bool:
                    break
                if func.name == ast.lhs.name and func.type is None:
                    func.type = typr
                    break
        left_jsm, typl = self.visit(ast.lhs,left_access)
        self.emit.printout(right_jsm + left_jsm) 
        return o
    def visitBlock(self, ast, o):
        o.frame.enterScope(False)
        self.emit.printout(self.emit.emitLABEL(o.frame.getStartLabel(), o.frame))
        env = o
        for x in ast.stmt:
            if type(x) is VarDecl or type(x) is If:
                env = self.visit(x, env)
            else:
                self.visit(x, env)
        self.emit.printout(self.emit.emitLABEL(o.frame.getEndLabel(), o.frame))
        o.frame.exitScope()
        return o
    def visitCallExpr(self, ast, o):
        res = self.visit(CallStmt(ast.name,ast.args),o)
        return res
    def visitCallStmt(self, ast, o):
        frame = o.frame
        env = o.sym
        sym = None
        for symbol in self.env:
            if symbol.name == ast.name.name:
                sym = symbol
                break
        cname = sym.value.value
        ctype = sym.type
        inputType = sym.type.starttype if type(sym.type) is ZCodeType else sym.type
        _in = ("",[])
        for x in ast.args:
            str1,typ1 = self.visit(x, Access(frame, env, False,True))
            _in = (_in[0] + str1, _in[1] + [typ1])
        self.emit.printout(_in[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(
                cname + "/" + ast.name.name, ctype, frame))
        return "",sym.type.rettype

    
    def visitBinaryOp(self, ast, o):
        ret,op = None,None
        left_ast,left_type = self.visit(ast.left,o)
        right_ast,right_type = self.visit(ast.right,o)
        if type(left_type) is ZCodeType:
            left_type = left_type.rettype
        if type(right_type) is ZCodeType:
            right_type = right_type.rettype
        ## need to consider when left type and right type is None
        if ast.op in ['+','-']:
            ret = NumberType()
            op = self.emit.emitADDOP(ast.op, ret, o.frame)
        elif ast.op in ['*','/']:
            ret = NumberType()
            op = self.emit.emitMULOP(ast.op, ret, o.frame)
        elif ast.op == '%':
            op = self.emit.emitMOD(o.frame)
        elif ast.op == 'and':
            op = self.emit.emitANDOP(o.frame)
        elif ast.op == 'or':
            op = self.emit.emitOROP(o.frame)
        elif ast.op == '...':
            op = self.emit.emitINVOKEVIRTUAL("java/lang/String/concat", ZCodeType([StringType()], StringType()), o.frame)
        elif ast.op == '==': ## compare two strings
            ret = StringType()
            op = self.emit.emitREOP(ast.op,ret,o.frame)
        elif ast.op == '=': #compare two numbers
            ret = NumberType()
            op = self.emit.emitREOP(ast.op,ret,o.frame)
        else:
            ret = BoolType()
            op = self.emit.emitREOP(ast.op,NumberType(),o.frame)
        return left_ast + right_ast + op, left_type
    def visitUnaryOp(self, ast, o):
        jsmc,typ = self.visit(ast.operand,o)
        if ast.op == '-':
            return jsmc + self.emit.emitNEGOP(typ, o.frame),typ
        else:
            return jsmc + self.emit.emitNOT(typ,o.frame), BoolType()
    
    def visitId(self, ast, o):
        for sym in o.sym:
            if sym.name == ast.name:
                if o.isLeft:
                    if type(sym.value) is Index:
                        return self.emit.emitWRITEVAR(sym.name,sym.type,sym.value.value,o.frame), sym.type
                    elif type(sym.value) is CName:
                        return self.emit.emitPUTSTATIC(sym.value.value+"/"+sym.name,sym.type,o.frame), sym.type
                    else:
                        return self.emit.emitPUTSTATIC(self.className+"/"+sym.name,sym.type,o.frame), sym.type
                else:
                    if type(sym.value) is Index:
                        return self.emit.emitREADVAR(sym.name,sym.type,sym.value.value,o.frame), sym.type
                    elif type(sym.value) is CName:
                        return self.emit.emitGETSTATIC(sym.value.value+"/"+sym.name,sym.type,o.frame), sym.type
                    else:
                        return self.emit.emitGETSTATIC(self.className+"/"+sym.name,sym.type,o.frame), sym.type
    def visitIf(self, ast, o):
        expr_jsm, typ = self.visit(ast.expr, Access(o.frame, o.sym, False))
        has_else = ast.elseStmt is not None
        if not has_else and (ast.elifStmt is None or len(ast.elifStmt) == 0):
            label_exit = o.frame.getNewLabel()
            self.emit.printout(expr_jsm)
            self.emit.printout(self.emit.emitIFFALSE(label_exit, o.frame))
            if type(ast.thenStmt) is not VarDecl:
                self.visit(ast.thenStmt, o)
            else:
                o = self.visit(ast.thenStmt, o)
            self.emit.printout(self.emit.emitLABEL(label_exit, o.frame))
        else:
            label_exit = o.frame.getNewLabel()
            label_else = o.frame.getNewLabel()
            if len(ast.elifStmt) != 0:
                label_next = o.frame.getNewLabel()
                self.emit.printout(expr_jsm)
                self.emit.printout(self.emit.emitIFFALSE(label_next, o.frame))
                if type(ast.thenStmt) is not VarDecl:
                    self.visit(ast.thenStmt, o)
                else:
                    o = self.visit(ast.thenStmt, o)
                self.emit.printout(self.emit.emitGOTO(label_exit, o.frame))
                self.emit.printout(self.emit.emitLABEL(label_next, o.frame))
                for i,(expr, stmt) in enumerate(ast.elifStmt):
                    expr_if, type_if = self.visit(expr, Access(o.frame, o.sym, False))
                    label_elif = o.frame.getNewLabel()
                    self.emit.printout(expr_if)
                    if i == len(ast.elifStmt) - 1 and has_else:
                        self.emit.printout(self.emit.emitIFFALSE(label_else, o.frame))
                    else:
                        self.emit.printout(self.emit.emitIFFALSE(label_elif, o.frame))  
                    if type(stmt) is not VarDecl:
                        self.visit(stmt, o)
                    else:
                        o = self.visit(stmt, o)
                    self.emit.printout(self.emit.emitGOTO(label_exit, o.frame))
                    self.emit.printout(self.emit.emitLABEL(label_elif, o.frame))
                if has_else:
                    self.emit.printout(self.emit.emitLABEL(label_else, o.frame))
                    if type(ast.elseStmt) is not VarDecl:
                        self.visit(ast.elseStmt, o)
                    else:
                        o = self.visit(ast.elseStmt, o)
                self.emit.printout(self.emit.emitLABEL(label_exit, o.frame))
            else:
                else_label = o.frame.getNewLabel()
                self.emit.printout(expr_jsm)
                self.emit.printout(self.emit.emitIFFALSE(else_label, o.frame))
                if type(ast.thenStmt) is not VarDecl:
                    self.visit(ast.thenStmt, o)
                else:
                    o =self.visit(ast.thenStmt, o)
                self.emit.printout(self.emit.emitGOTO(label_exit, o.frame))
                self.emit.printout(self.emit.emitLABEL(else_label, o.frame))
                if type(ast.elseStmt) is not VarDecl:
                    self.visit(ast.elseStmt, o)
                else:   
                    o = self.visit(ast.elseStmt, o)
                self.emit.printout(self.emit.emitLABEL(label_exit, o.frame))
        return o
            
    def visitFor(self, ast, o):
        # Initial
        # -> Loop
        
        temp_var = VarDecl(Id("temp_var"),NumberType(),None,ast.name)
        env = self.visit(temp_var, o)
        o.frame.enterLoop()

        # Initialize i outside of the loop
        # Label
        conLabel = o.frame.getContinueLabel()
        brkLabel = o.frame.getBreakLabel()
        chkLabel, bodyLabel, updLabel = o.frame.getNewLabel(), o.frame.getNewLabel(), o.frame.getNewLabel()
        # Condition Check
        self.emit.printout(self.emit.emitLABEL(chkLabel, o.frame))
        ccode, ctyp = self.visit(ast.condExpr, Access(o.frame, o.sym, False, True))
        self.emit.printout(ccode)
        self.emit.printout(self.emit.emitIFTRUE(brkLabel, o.frame))
        # Body   
        self.emit.printout(self.emit.emitLABEL(bodyLabel, o.frame))
        self.visit(ast.body, o)
        ## Put Continue: Update->Check Cond
        self.emit.printout(self.emit.emitLABEL(conLabel, o.frame))
        # Update
        self.emit.printout(self.emit.emitLABEL(updLabel, o.frame))
        self.visit(Assign(ast.name, BinaryOp("+", ast.name, ast.updExpr)), o)
        self.emit.printout(self.emit.emitGOTO(chkLabel, o.frame))
        ## Put Break
        self.emit.printout(self.emit.emitLABEL(brkLabel, o.frame))
        # <- Loop
        
        o.frame.exitLoop()
        self.visit(Assign(ast.name,temp_var.name), env)
        return
    def visitReturn(self, ast, o):
        ret_type = o.frame.returnType
        if ast.expr:
            expr_jsm, typ_expr = self.visit(ast.expr, Access(o.frame, o.sym, False, True))
            self.emit.printout(expr_jsm)
        self.emit.printout(self.emit.emitGOTO(o.frame.getEndLabel(), o.frame))
    def visitArrayCell(self, ast, o):
        # arr: Expr
        # idx: List[Expr]
        code = ""
        arr = ast.arr
        idx_list = ast.idx
        o, expr = (o[0],o[1]) if type(o) is tuple else (o,None)
        code, arr_type = self.visit(arr,Access(o.frame, o.sym, False, True,None,True))
        for i in range(len(idx_list)-1):
            idx_code, idx_type = self.visit(idx_list[i],Access(o.frame, o.sym, False, True,None,True))
            code += idx_code
            code += self.emit.emitF2I(o.frame) 
            code += self.emit.emitALOAD(arr_type, o.frame)
        idx_code, idx_type = self.visit(idx_list[-1],Access(o.frame, o.sym, False, True,None,True))
        idx_code+=self.emit.emitF2I(o.frame)
        if o.isLeft:
            code += idx_code + self.visit(expr,Access(o.frame, o.sym, False, True,None,True))[0] + self.emit.emitASTORE(arr_type.eleType, o.frame)
            return code,arr_type.eleType
        else:
            if type(arr_type) is ArrayType and len(ast.idx) <len(arr_type.size):
                    res_size = arr_type.size[len(ast.idx):]
                    code += idx_code + self.emit.emitALOAD(arr_type, o.frame)
                    return code, ArrayType(res_size, arr_type.eleType)
            elif type(arr_type) is ArrayType and len(ast.idx) == len(arr_type.size):
                code += idx_code + self.emit.emitALOAD(arr_type.eleType, o.frame)
                return code, arr_type.eleType
    def visitArrayLiteral(self, ast, o):
        code,ele_type = "",None
        o.frame.push()
        for i in range(len(ast.value)):
            code += self.emit.emitDUP(o.frame)
            code += self.emit.emitPUSHICONST(i, o.frame)
            element_code , ele_type = self.visit(ast.value[i], o)
            code += element_code
            code += self.emit.emitASTORE(ele_type, o.frame)
        o.frame.pop()
        arr_len = [len(ast.value)]
        first_ele = ast.value[0]
        while(type(first_ele) is ArrayType):
            sub_list = first_ele.value
            arr_len+= [len(sub_list)]
            first_ele = sub_list[0]
        code = self.emit.emitARRAYLITERAL(ArrayType(arr_len, ele_type), o.frame) + code
        return code,ArrayType(arr_len, ele_type)

    