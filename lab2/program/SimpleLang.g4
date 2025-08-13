grammar SimpleLang;

// ----------- Reglas sintacticas  ------------

//estas gramatica esta tomada del repositorio de brolo y se modifico un poco

prog: (stat | NEWLINE)* EOF ;

stat
  : ID '=' expr (NEWLINE | EOF)   # assign
  | expr        (NEWLINE | EOF)   # printExpr
  | NEWLINE                       # blank
  ;

expr
    : <assoc=right> expr '^' expr      # Pow
    | op=('+'|'-') expr                # UnarySign
    | expr op=('*'|'/'|'%') expr       # MulDiv
    | expr op=('+'|'-') expr           # AddSub
    | INT                              # Int
    | FLOAT                            # Float
    | STRING                           # String
    | BOOL                             # Bool
    | ID                               # Var
    | '(' expr ')'                     # Parens
    ;


INT     : DIGIT+ ;
FLOAT   : DIGIT+ ('.' DIGIT*)? EXP? | '.' DIGIT+ EXP? ;
fragment EXP : [eE] [+\-]? DIGIT+ ;
STRING  : '"' ( '\\' . | ~["\\\r\n] )* '"' ;
BOOL: 'true' | 'false' ;
NEWLINE: '\r'? '\n' ;
WS: [ \t]+ -> skip ;

ID  : [a-zA-Z_][a-zA-Z_0-9]*; // match identifiers

LINE_COMMENT  : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;

fragment DIGIT : [0-9] ;