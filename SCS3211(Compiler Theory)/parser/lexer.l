%{
#include "parser.tab.h"
%}

%%

[0-9]+          { yylval.ival = atoi(yytext); return NUMBER; }
[ \t]           { /* ignore whitespace */ }
\n              { return EOL; }
"+"             { return PLUS; }
"-"             { return MINUS; }
"*"             { return MUL; }
"/"             { return DIV; }
"%"             { return MOD; }
"^"             { return EXP; }
"("             { return LPAREN; }
")"             { return RPAREN; }
.               { printf("Unknown character: %s\n", yytext); }
"STOP"  {return STOP;}

%%

int yywrap() {
    return 1;
}
