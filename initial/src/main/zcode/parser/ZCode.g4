//2110242
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: declaration_list EOF ;

//DECLARATIONS
declaration_list: declaration declaration_list | declaration;
declaration: variable_decl | function_decl;

// VARIABLE DECLARATION
variable_decl:  var_type index_list sign_decl array_decl NEWLINE* | var_decl NEWLINE*| dyna_decl NEWLINE*;
index_list: IDENTIFIER COMMA index_list| IDENTIFIER| expr COMMA index_list| expr;
array_decl:  array_type | ;
var_decl: VAR IDENTIFIER ASS expr;
sign_decl: ASS | EQ |;
dyna_decl: dynamic_type sign_decl ( expr | ) ;

//parameter
para_decl: var_type IDENTIFIER array_decl;

//function
function_decl: FUNC func_head func_body;
func_head: IDENTIFIER LR para_decl_list RR;
para_decl_list: para_decl COMMA para_decl_list| para_decl | ;
func_body: NEWLINE* block_stmt NEWLINE*| NEWLINE* RETURN expr NEWLINE* |;

//STATEMENT
statement: if_stmt | normal_stmt;
if_stmt: IF expr NEWLINE* statement NEWLINE* elif_stmt else_stmt;
elif_stmt: ELIF expr NEWLINE* statement NEWLINE* elif_stmt | ;
else_stmt: NEWLINE* ELSE NEWLINE* statement | ;
normal_stmt: ass_stmt
	|if_stmt
	|for_stmt
	|break_stmt
	|continue_stmt
	|return_stmt
	|call_stmt
	|block_stmt;


//assignment
ass_stmt: lhs ASS expr NEWLINE+ ;	 
lhs: IDENTIFIER | index_expr | func_call_expr |variable_decl ;

//for
for_stmt: FOR IDENTIFIER UNTIL expr BY expr NEWLINE* statement NEWLINE*;
//break
break_stmt: BREAK NEWLINE+;
//Continue
continue_stmt: CONTINUE NEWLINE+;
//Function
call_stmt: func_call_expr NEWLINE+;
//Block
block_stmt: BEGIN NEWLINE+ stodl_list END NEWLINE+;
stodl: statement | (variable_decl NEWLINE+) | (expr NEWLINE*);
stodl_list: stodl stodl_list | ;

//return
return_stmt: RETURN expr NEWLINE+;


//Expression
expr:  expr0;
expr0 : expr1 CONC expr1 | expr1; 
expr1 : expr2 (EQ| EQEQ | NEQ | LT | GT | LTE | GTE) expr2 | expr2;
expr2 : expr2 (AND | OR) expr3 | expr3;
expr3 : expr3 (ADD | MINUS) expr4 | expr4;
expr4 : expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5 : NOT expr5 | expr6;
expr6 : MINUS expr6 | expr7;
expr7: IDENTIFIER | constant | func_call_expr | index_expr|sub_expr;

sub_expr: LR expr RR;
constant: NUMBERLIT | BOOLEANLIT | STRINGLIT;

func_call_expr: IDENTIFIER LR (expr_list| ) RR;
expr_list: exprprime |;
exprprime: expr COMMA exprprime | expr;

index_expr: IDENTIFIER index_operator;

index_operator: LS index_operators RS;

index_operators:  num_id COMMA index_operators| num_id ;
num_id: NUMBERLIT | IDENTIFIER | expr;


//TYPE
var_type: var_prime | array_type;
var_prime: NUMBER | BOOL | STRING;
dynamic_type: DYNAMIC;
array_type : LS array_lit RS;
array_lit: (constant|expr|array_type) COMMA array_lit | constant| expr| array_type|;


// LITERAL
BOOLEANLIT: TRUE | FALSE;
NUMBERLIT: INT('.'DEC)?(EXP)?;
fragment INT: DIGIT+;
fragment DEC: DIGIT* ;
fragment EXP: [eE] [+-]? DIGIT+;  
fragment DIGIT: [0-9];

STRINGLIT : '"' (NON_ESC | ESC | DOUBLE_QUOTE)* '"' {self.text = self.text[1:-1]};
fragment ESC: '\\b'
			| '\\t'
			| '\\n'
			| '\\f'
			| '\\r'
			| '\\\''
			| '\\\\';
fragment NON_ESC : ~[\n\r"\\];			
fragment ILL_ESC : '\\' ~[bfrnt'\\];
fragment DOUBLE_QUOTE : '\'"'; 



//KEYWORD
TRUE: 'true';
FALSE: 'false';
NUMBER: 'number';
BOOL: 'bool';
STRING: 'string';
RETURN: 'return';
VAR: 'var';
DYNAMIC: 'dynamic';
FUNC: 'func';
FOR: 'for';
UNTIL: 'until';
BY: 'by';
BREAK: 'break';
CONTINUE: 'continue';
IF: 'if';
ELSE: 'else';
ELIF: 'elif';
BEGIN: 'begin';
END: 'end';
NOT:  'not';
AND: 'and';
OR:  'or';

//COMMENT
COMMENT: '##' ~[\r\n]* -> skip;


//OPERATOR
ASS: '<-';
MUL: '*';
DIV: '/';
ADD: '+';
MINUS: '-';
MOD: '%';
LTE: '<=';
GTE: '>=';
NEQ: '!=';
LT : '<' ;
GT : '>' ;
CONC: '...';
EQEQ: '==';
EQ: '=';
//SEPARATORS
LR: '(';
RR: ')';
LS: '[';
RS: ']';
COMMA: ',';
NEWLINE: '\n' | '\r' | '\r\n' ;
//IDENTIFIER
IDENTIFIER : [a-zA-Z_] [0-9a-zA-Z_]*;


WS : [ \t\b\f]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING:'"' (NON_ESC | ESC)* (EOF | [\n\r]) {
	raise UncloseString(self.text[1:].replace('\n','').replace('\r',''))
};
ILLEGAL_ESCAPE:'"' (NON_ESC | ESC)* ILL_ESC { 
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};
