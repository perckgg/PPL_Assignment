grammar ZCode;

@lexer::header {
from lexererr import *
}

options {
	language=Python3;
}
//2110242

program: newlines? declaration_list EOF;
declaration_list: declaration declaration_list | declaration;
declaration: function_decl | variable_decl newlines;

//Expression
expr_list: expr COMMA expr_list | expr;
expr:  expr1 CONC expr1 | expr1; 
expr1 : expr2 (EQ| EQEQ | NEQ | LT | GT | LTE | GTE) expr2 | expr2;
expr2 : expr2 (AND | OR) expr3 | expr3;
expr3 : expr3 (ADD | MINUS) expr4 | expr4;
expr4 : expr4 (MUL | DIV | MOD) expr5 | expr5;
expr5 : NOT expr5 | expr6;
expr6 : MINUS expr6 | expr7;
expr7: (IDENTIFIER | IDENTIFIER LR index_operators? RR) LS expr_list RS | expr8;
expr8: IDENTIFIER | constant | func_call_expr |sub_expr| LS expr_list RS;
constant: NUMBERLIT| BOOLEANLIT| STRINGLIT;
sub_expr: LR expr RR;
index_operators:  expr COMMA index_operators | expr ;
func_call_expr: IDENTIFIER LR expr_list? RR;

// VARIABLE DECLARATION
variable_decl: var_decl | single_decl | dynamic_decl;
var_decl: VAR IDENTIFIER ASS expr;
single_decl: primitive_type IDENTIFIER array? (ASS expr)?;
primitive_type: NUMBER | BOOL | STRING;
dynamic_decl: DYNAMIC IDENTIFIER (ASS expr)?;
dimension : NUMBERLIT COMMA dimension | NUMBERLIT;
array: LS dimension RS;

//function
function_decl: FUNC IDENTIFIER func_head func_body;
func_head: LR para_decl_list? RR;
func_body: newlines? block_stmt | newlines? return_stmt  | newlines;
//parameter
para_decl: primitive_type IDENTIFIER array?;
para_decl_list: para_decl COMMA para_decl_list| para_decl ;

//STATEMENT
statement_list: statement statement_list | ;
statement: ass_stmt
	|if_stmt
	|for_stmt
	|break_stmt
	|continue_stmt
	|return_stmt
	|block_stmt
	|decl_stmt
	|call_stmt;

// Declaration statement
decl_stmt: variable_decl newlines;
call_stmt: func_call_expr newlines;
//assignment
ass_stmt: IDENTIFIER (LS expr_list RS)? ASS expr newlines;

// IF statement
if_stmt: IF expr newlines? statement elif_stmt newlines? else_stmt?;
elif_stmt: ELIF expr newlines? statement newlines? elif_stmt | ;
else_stmt: ELSE newlines? statement newlines?;

//for
for_stmt: FOR IDENTIFIER UNTIL expr BY expr newlines? statement newlines?;

//break
break_stmt: BREAK newlines;

//Continue
continue_stmt: CONTINUE newlines;

//return
return_stmt: RETURN expr? newlines;

//Block
block_stmt: BEGIN newlines statement_list END newlines;

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

//Set of characters
newlines: NEWLINE comnew_list;
comnew_list: comnew comnew_list |;
comnew: COMMENT NEWLINE | NEWLINE;
NEWLINE: '\n';
WS : [ \t\b\f\r]+ -> skip ;

//COMMENT
COMMENT: '##' ~[\r\n]* -> skip;

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

//IDENTIFIER
IDENTIFIER : [a-zA-Z_] [0-9a-zA-Z_]*;

UNCLOSE_STRING:'"' (NON_ESC | ESC)* ( '\r\n' | '\n' | EOF ) {
	if(len(self.text) >= 2 and self.text[-1] == '\n' and self.text[-2] == '\r'):
        raise UncloseString(self.text[1:-2])
	elif(self.text[-1] == '\n'):
		raise UncloseString(self.text[1:-1])
	else:
        raise UncloseString(self.text[1:])
};
ILLEGAL_ESCAPE:'"' (NON_ESC | ESC)* ILL_ESC { 
	raise IllegalEscape(self.text[1:])
};
ERROR_CHAR: . {raise ErrorToken(self.text)};
