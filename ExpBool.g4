

grammar ExpBool;

funtion: variable ':=' exp #functionBool
    ;

exp: variable           #variableBool
    | exp 'and' exp     #opANDD
    | exp 'or' exp      #opORR
    | exp 'xor' exp     #opXor
    | 'not(' exp ')'    #opNOT
    | '(' exp ')'       #intoMarks
    ;

variable: (LOWERCASEE | UPPERCASEE) (INT | LOWERCASEE | UPPERCASEE )*;

LOWERCASEE  : [a-z] ;

UPPERCASEE  : [A-Z] ;

INT: [0-9]+ ;

WHITESPACE : ' ' -> skip ;