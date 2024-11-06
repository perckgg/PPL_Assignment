from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *
#2110242 - Nguyễn Văn Hoàng Khang
from functools import reduce
class ASTGeneration(ZCodeVisitor):
    #program: newlines? declaration_list EOF;
    def visitProgram(self, ctx: ZCodeParser.ProgramContext):
        return Program(self.visit(ctx.declaration_list()))
    #declaration_list: declaration declaration_list | declaration;
    def visitDeclaration_list(self, ctx: ZCodeParser.Declaration_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.declaration())]
        return [self.visit(ctx.declaration())] + self.visit(ctx.declaration_list()) 
    #declaration: VarDecl | FuncDecl;
    def visitDeclaration(self, ctx: ZCodeParser.DeclarationContext):
        if ctx.variable_decl():
            return self.visit(ctx.variable_decl())
        return self.visit(ctx.function_decl())
## Expression
    #expr_list: expr COMMA expr_list | expr;
    def visitExpr_list(self,ctx: ZCodeParser.Expr_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.expr_list())
    #expr: expr1 CONC expr1 | expr1; 
    def visitExpr(self, ctx: ZCodeParser.ExprContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    #expr1 : expr2 (EQ| EQEQ | NEQ | LT | GT | LTE | GTE) expr2 | expr2;
    def visitExpr1(self, ctx: ZCodeParser.Expr1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    # expr2 : expr2 (AND | OR) expr3 | expr3;
    def visitExpr2(self, ctx: ZCodeParser.Expr2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    #expr3 : expr3 (ADD | MINUS) expr4 | expr4;
    def visitExpr3(self, ctx: ZCodeParser.Expr3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    #expr4 : expr4 (MUL | DIV | MOD) expr5 | expr5;
    def visitExpr4(self, ctx: ZCodeParser.Expr4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return BinaryOp(ctx.getChild(1).getText(), self.visit(ctx.getChild(0)), self.visit(ctx.getChild(2)))
    #expr5 : NOT expr5 | expr6;
    def visitExpr5(self, ctx: ZCodeParser.Expr5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expr5()))
    #expr6 : MINUS expr6 | expr7;
    def visitExpr6(self, ctx: ZCodeParser.Expr6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        return UnaryOp(ctx.MINUS().getText(), self.visit(ctx.getChild(1)))
    #expr7: (IDENTIFIER | IDENTIFIER LR index_operators? RR) LS index_operators RS | expr8;
    ### function in special call : foo()[expr_list] | foo(expr_list)[expr_list] | foo[expr_list]
    def visitExpr7(self, ctx: ZCodeParser.Expr7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.expr8())
        elif ctx.getChildCount() == 4:
            return ArrayCell(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr_list()))
        elif ctx.RR():
            if ctx.getChildCount() == 6:
                return ArrayCell(CallExpr(Id(ctx.IDENTIFIER().getText()), []), self.visit(ctx.expr_list()))
        return ArrayCell(CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.index_operators())), self.visit(ctx.expr_list()))

    #expr8: IDENTIFIER | constant | func_call_expr |sub_expr| LS expr_list RS;
    def visitExpr8(self, ctx: ZCodeParser.Expr8Context):
        if ctx.IDENTIFIER():
            return Id(ctx.IDENTIFIER().getText())
        if ctx.constant():
            return self.visit(ctx.constant())
        if ctx.func_call_expr():
            return self.visit(ctx.func_call_expr())
        if ctx.sub_expr():
            return self.visit(ctx.sub_expr())
        return ArrayLiteral(self.visit(ctx.expr_list()))
    def visitConstant(self, ctx: ZCodeParser.ConstantContext):
        if ctx.NUMBERLIT():
            return NumberLiteral(float(ctx.NUMBERLIT().getText()))
        elif ctx.BOOLEANLIT():
            return BooleanLiteral(ctx.BOOLEANLIT().getText() == "true")
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        return self.visit(ctx.getChild(0))
    def visitSub_expr(self, ctx: ZCodeParser.Sub_exprContext):
        return self.visit(ctx.getChild(1))
    #index_operators:  expr COMMA index_operators | expr ;
    def visitIndex_operators(self, ctx: ZCodeParser.Index_operatorsContext):
        if ctx.getChildCount() == 1 : return [self.visit(ctx.expr())]
        return [self.visit(ctx.expr())] + self.visit(ctx.index_operators()) 
    #func_call_expr: IDENTIFIER LR expr_list? RR;
    def visitFunc_call_expr(self, ctx: ZCodeParser.Func_call_exprContext):
        if ctx.expr_list():
            return CallExpr(Id(ctx.IDENTIFIER().getText()), self.visit(ctx.expr_list()))
        return CallExpr(Id(ctx.IDENTIFIER().getText()), [])
## Declaration
    #variable_decl: var_decl | single_decl | dynamic_decl;
    def visitVariable_decl(self, ctx: ZCodeParser.Variable_declContext):
        if ctx.var_decl():
            return self.visit(ctx.var_decl())
        elif ctx.single_decl():
            return self.visit(ctx.single_decl())
        return self.visit(ctx.dynamic_decl())
    #var_decl: VAR IDENTIFIER ASS expr;
    def visitVar_decl(self, ctx: ZCodeParser.Var_declContext):
        return VarDecl(Id(ctx.IDENTIFIER().getText()),None,ctx.VAR(),self.visit(ctx.expr()))
    #single_decl: PRIME IDENTIFIER array? (ASS expr)?;
    #PRIME: NUMBER | BOOL | STRING;
    def visitSingle_decl(self, ctx: ZCodeParser.Single_declContext):
        var_type = self.visit(ctx.primitive_type())
        #array_type = self.visit(ctx.array())
        if ctx.expr():
            if ctx.array():
                dimension = self.visit(ctx.array())
                return VarDecl(Id(ctx.IDENTIFIER().getText()),ArrayType(dimension,var_type),None,self.visit(ctx.expr()))
            return VarDecl(Id(ctx.IDENTIFIER().getText()),var_type,None,self.visit(ctx.expr()))
        else:
            if ctx.array():
                dimension = self.visit(ctx.array())
                return VarDecl(Id(ctx.IDENTIFIER().getText()),ArrayType(dimension,var_type),None,None)
            return VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.primitive_type()),None,None)
    def visitPrimitive_type(self, ctx: ZCodeParser.Primitive_typeContext):
        if ctx.NUMBER():
            return NumberType()
        elif ctx.BOOL():
            return BoolType()
        return StringType()
    #dynamic_decl: DYNAMIC IDENTIFIER (ASS expr)?;
    def visitDynamic_decl(self, ctx: ZCodeParser.Dynamic_declContext):
        if ctx.expr():
            return VarDecl(Id(ctx.IDENTIFIER().getText()),None,ctx.DYNAMIC().getText(),self.visit(ctx.expr()))
        return VarDecl(Id(ctx.IDENTIFIER().getText()),None,ctx.DYNAMIC().getText(),None)
    #dimension : NUMBERLIT COMMA dimension | NUMBERLIT;
    def visitDimension(self, ctx: ZCodeParser.DimensionContext):
        if ctx.getChildCount() == 1:
            return [float(ctx.NUMBERLIT().getText())]
        return [float(ctx.NUMBERLIT().getText())] + self.visit(ctx.dimension())
        
    def visitArray(self, ctx: ZCodeParser.ArrayContext):
        return self.visit(ctx.dimension())
    #function_decl: FUNC func_head func_body;
    def visitFunction_decl(self, ctx: ZCodeParser.Function_declContext):
        name = Id(ctx.IDENTIFIER().getText())
        param = self.visit(ctx.func_head())
        body = self.visit(ctx.func_body())
        return FuncDecl(name, param, body)
    #func_head: IDENTIFIER LR para_decl_list? RR;
    def visitFunc_head(self, ctx: ZCodeParser.Func_headContext):
        if ctx.para_decl_list():
            return self.visit(ctx.para_decl_list())
        return []
    #func_body: newlines? block_stmt | newlines? return_stmt  | newlines;
    def visitFunc_body(self, ctx: ZCodeParser.Func_bodyContext):
        if ctx.block_stmt():
            return self.visit(ctx.block_stmt())
        elif ctx.return_stmt():
            return self.visit(ctx.return_stmt())
        return None
    #para_decl: primitive_type IDENTIFIER array?;
    def visitPara_decl(self, ctx: ZCodeParser.Para_declContext):
        if ctx.array():
            dimension = self.visit(ctx.array())
            return VarDecl(Id(ctx.IDENTIFIER().getText()),ArrayType(dimension,self.visit(ctx.primitive_type())),None,None)
        return VarDecl(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.primitive_type()),None,None)
    #para_decl_list: para_decl COMMA para_decl_list| para_decl ;
    def visitPara_decl_list(self, ctx: ZCodeParser.Para_decl_listContext):
        if ctx.getChildCount() == 1:
            return [self.visit(ctx.para_decl())]
        return [self.visit(ctx.para_decl())] + self.visit(ctx.para_decl_list())
    
## Statement
    def visitStatement(self, ctx: ZCodeParser.StatementContext):
        return self.visit(ctx.getChild(0))
    #statement_list: statement statement_list | ;
    def visitStatement_list(self, ctx: ZCodeParser.Statement_listContext):
        if ctx.getChildCount() == 0:
            return []
        return [self.visit(ctx.statement())] + self.visit(ctx.statement_list())
    #decl_stmt: variable_decl newlines;
    def visitDecl_stmt(self, ctx: ZCodeParser.Decl_stmtContext):
        return self.visit(ctx.variable_decl())
    #ass_stmt: IDENTIFIER (LS expr_list RS)? ASS expr newlines;
    def visitAss_stmt(self, ctx: ZCodeParser.Ass_stmtContext):
        if ctx.LS():
            return Assign(ArrayCell(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expr_list())),self.visit(ctx.expr()))
        return Assign(Id(ctx.IDENTIFIER().getText()),self.visit(ctx.expr()))
    #if_stmt: IF expr newlines? statement elif_stmt newlines? else_stmt?;
    def visitIf_stmt(self, ctx: ZCodeParser.If_stmtContext):
        if ctx.elif_stmt():
            if ctx.else_stmt():
                return If(self.visit(ctx.expr()),self.visit(ctx.statement()),self.visit(ctx.elif_stmt()),self.visit(ctx.else_stmt()))
            return If(self.visit(ctx.expr()),self.visit(ctx.statement()),self.visit(ctx.elif_stmt()),None)
        else:
            if ctx.else_stmt():
                return If(self.visit(ctx.expr()),self.visit(ctx.statement()),None,self.visit(ctx.else_stmt()))
            return If(self.visit(ctx.expr()),self.visit(ctx.statement()),None,None)
    #elif_stmt: ELIF expr newlines? statement newlines? elif_stmt | ;
    def visitElif_stmt(self, ctx: ZCodeParser.Elif_stmtContext):
        if ctx.getChildCount() == 0:
            return []
        return [(self.visit(ctx.expr()), self.visit(ctx.statement()))] + self.visit(ctx.elif_stmt())
    #else_stmt: ELSE newlines? statement newlines?;
    def visitElse_stmt(self, ctx: ZCodeParser.Else_stmtContext):
        return self.visit(ctx.statement())
    
    def visitFor_stmt(self, ctx: ZCodeParser.For_stmtContext):
        name = Id(ctx.IDENTIFIER().getText())
        condExpr = self.visit(ctx.expr(0))
        updExpr = self.visit(ctx.expr(1))
        body = self.visit(ctx.statement())
        return For(name,condExpr,updExpr,body)
    def visitBreak_stmt(self, ctx: ZCodeParser.Break_stmtContext):
        return Break()
    def visitContinue_stmt(self, ctx: ZCodeParser.Continue_stmtContext):
        return Continue()
    def visitReturn_stmt(self, ctx: ZCodeParser.Return_stmtContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        return Return(None)
    #call_stmt: func_call_expr newlines;
    def visitCall_stmt(self, ctx: ZCodeParser.Call_stmtContext):
        if ctx.func_call_expr().expr_list():
            name = Id(ctx.func_call_expr().IDENTIFIER().getText())
            args = self.visit(ctx.func_call_expr().expr_list())
            return CallStmt(name,args)
        return CallStmt(Id(ctx.func_call_expr().IDENTIFIER().getText()),[])
    #block_stmt: BEGIN newlines statement_list END newlines;
    def visitBlock_stmt(self, ctx: ZCodeParser.Block_stmtContext):
        ## check if statement_list empty
        if ctx.statement_list():
            return Block(self.visit(ctx.statement_list()))
        return Block(None)
## NEWLINE
    #newlines: NEWLINE comnew_list;
    def visitNewlines(self, ctx: ZCodeParser.NewlinesContext):
        if ctx.getChildCount() == 1:
            return ["\\n"]
        return ["\\n" + self.visit(ctx.comnew_list())]
    #comnew_list: comnew comnew_list | ;
    def visitComnew_list(self, ctx: ZCodeParser.Comnew_listContext):
        if ctx.getChildCount() == 0:
            return []
        return self.visit(ctx.getChild(0)) + self.visit(ctx.getChild(1))
    #comnew: COMMENT NEWLINE | NEWLINE;
    def visitComnew(self, ctx: ZCodeParser.ComnewContext):
        if ctx.COMMENT():
            return ctx.COMMENT().getText() + "\\n"
        return "\\n"