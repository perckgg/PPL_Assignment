//2110242
grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}

program: EOF ;
//DECLARATIONS
declaration: variable_decl | function_decl;
variable_decl:  (NUMBER| STRING| BOOL) IDENTIFIER (COMMA IDENTIFIER)*| var_decl| dyna_decl;
var_decl: VAR IDENTIFIER ASS expr;
dyna_decl: DYNAMIC IDENTIFIER;
function_decl: FUNC IDENTIFIER LR NUMBER RR;

//Expression

expr: expr0;
expr_list: exprsimple | ;
exprsimple: expr COMMA exprsimple | expr;

expr0 : expr1 CONC expr1 | expr1;
expr1 : expr2 (EQ| EQEQ | NEQ | LT | GT | LTE | GTE) expr2 | expr2;
expr2 : expr2 (AND | OR) expr3 | expr3;
expr3 : expr3 (ADD | MINUS) expr4 | expr4;
expr4 : expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5 : NOT expr5 | expr6;
expr6 : MINUS expr6 | expr7;

expr7: IDENTIFIER | constant | func_call_expr | index_expr | sub_expr;

constant: NUMBERLIT | BOOLEANLIT | STRINGLIT;

func_call_expr: IDENTIFIER LR expr_list RR;

sub_expr: LR expr RR;

index_operator: LS index_operators RS;

index_operators: NUMBERLIT | NUMBERLIT COMMA index_operators;

index_expr: (IDENTIFIER | func_call_expr) index_operator;

//TYPE
DATATYPE: PRIMITIVE | ARRAY;
PRIMITIVE: NUMBER | BOOL | STRING;
ARRAY : PRIMITIVE DIMENSION '<-' LS ARRAY_VALUES RS;
fragment DIMENSION: LS DIGIT (COMMA DIGIT)* RS;
fragment ARRAY_VALUES: LS (PRIMITIVE | ARRAY_VALUES) (COMMA (PRIMITIVE | ARRAY_VALUES))* RS;

// LITERAL
BOOLEANLIT: 'TRUE' | 'FALSE';
NUMBERLIT: '-'?DIGIT+(.DIGIT*)?([eE] [+-]? DIGIT+)? ;
fragment DIGIT: [0-9]+;

STRINGLIT:
	'"' (NON_ESC | ESC)* '"' {self.text = self.text[1:-1]};
fragment NON_ESC: ~[\n'\r"];
fragment ESC: '\\' [bfrnt'"\\];
fragment ILL_ESC: '\\' ~[bfrnt'"\\];



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
NOT: '!'| 'not';
AND: '&&'| 'and';
OR: '||'| 'or';

//COMMENT
COMMENT : '##' .*? '\n';


//OPERATOR
MUL: '*';
DIV: '/';
ADD: '+';
MINUS: '-';
MOD: '%';
LTE: '<=';
GTE: '>=';
EQ: '=';
NEQ: '!=';
ASS: '<-';
LT : '<' ;
GT : '>' ;
CONC: '...';
EQEQ: '==';

//SEPARATORS
LR: '(';
RR: ')';
LS: '[';
RS: ']';
COMMA: ',';

//IDENTIFIER
IDENTIFIER : [a-zA-Z_] [0-9a-zA-Z_]*;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines

UNCLOSE_STRING:
	'"' (NON_ESC | ESC)* {raise UncloseString(self.text[1:])};
ILLEGAL_ESCAPE:
	'"' (NON_ESC | ESC)* ILL_ESC { raise IllegalEscape(self.text[1:])};

ERROR_CHAR: . {raise ErrorToken(self.text)};
