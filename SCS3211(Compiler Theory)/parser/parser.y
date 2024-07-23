%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>

void yyerror(const char *s);
int yylex(void);

extern char *yytext;
%}

%union {
    int ival;
    double dval;
    char *sval;
}

%token <ival> NUMBER
%token PLUS MINUS MUL DIV MOD EXP LPAREN RPAREN EOL

%left PLUS MINUS
%left MUL DIV MOD
%right EXP
%nonassoc UMINUS

%type <dval> expr term factor primary

%%

input:
    | input line
    ;

line:
    expr EOL { printf("Result: %g\n", $1); }
    | EOL
    ;

expr:
    term
    | expr PLUS term  { $$ = $1 + $3; }
    | expr MINUS term { $$ = $1 - $3; }
    ;

term:
    factor
    | term MUL factor { $$ = $1 * $3; }
    | term DIV factor { $$ = $1 / $3; }
    | term MOD factor { $$ = fmod($1, $3); }
    ;

factor:
    primary
    | primary EXP factor { $$ = pow($1, $3); }
    ;

primary:
    NUMBER { $$ = (double)$1; }  // Convert int to double
    | LPAREN expr RPAREN { $$ = $2; }
    | MINUS primary %prec UMINUS { $$ = -$2; }
    ;

%%

void yyerror(const char *s) {
    if (strcmp(s, "syntax error") == 0) {
        fprintf(stderr, "Syntax error: ");
        switch (yychar) {
            case 0:
                fprintf(stderr, "Unexpected end of input.\n");
                break;
            case RPAREN:
                fprintf(stderr, "Unmatched closing parenthesis.\n");
                break;
            default:
                fprintf(stderr, "Unexpected token '%s'.\n", yytext);
                break;
        }
    } else {
        fprintf(stderr, "Error: %s\n", s);
    }
}

int main(void) {
    return yyparse();
}
