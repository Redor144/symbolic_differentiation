import ply.yacc as yacc
from .symbolic_math import *
from .lexer import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POWER'),
    ('right', 'UMINUS'),
)

def p_expression(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression'''
    if p[2] == '+':
        p[0] = Add(p[1], p[3])
    elif p[2] == '-':
        p[0] = Add(p[1], Mul(Constant(-1), p[3]))
    elif p[2] == '*':
        p[0] = Mul(p[1], p[3])
    elif p[2] == '/':
        p[0] = Mul(p[1], Pow(p[3], Constant(-1)))
    elif p[2] == '^':
        p[0] = Pow(p[1], p[3])

def p_expression_unary(p):
    '''expression : MINUS expression %prec UMINUS'''
    p[0] = Mul(Constant(-1), p[2])

# Funkcje matematyczne
def p_expression_function(p):
    '''expression : SIN LPAREN expression RPAREN
                  | COS LPAREN expression RPAREN
                  | LN LPAREN expression RPAREN
                  | SQRT LPAREN expression RPAREN
                  | ABS LPAREN expression RPAREN
                  | EXP LPAREN expression RPAREN
                  | SINH LPAREN expression RPAREN
                  | COSH LPAREN expression RPAREN
                  | TANH LPAREN expression RPAREN
                  | ASIN LPAREN expression RPAREN
                  | ACOS LPAREN expression RPAREN
                  | ATAN LPAREN expression RPAREN
                  | TAN LPAREN expression RPAREN
                  | SEC LPAREN expression RPAREN
                  | LOG LPAREN expression COMMA expression RPAREN'''
    if p[1] == 'sin':
        p[0] = Sin(p[3])
    elif p[1] == 'cos':
        p[0] = Cos(p[3])
    elif p[1] == 'ln':
        p[0] = Ln(p[3])
    elif p[1] == 'sqrt':
        p[0] = Sqrt(p[3])
    elif p[1] == 'abs':
        p[0] = Abs(p[3])
    elif p[1] == 'exp':
        p[0] = Exp(p[3])
    elif p[1] == 'sinh':
        p[0] = Sinh(p[3])
    elif p[1] == 'cosh':
        p[0] = Cosh(p[3])
    elif p[1] == 'tanh':
        p[0] = Tanh(p[3])
    elif p[1] == 'asin':
        p[0] = Asin(p[3])
    elif p[1] == 'acos':
        p[0] = Acos(p[3])
    elif p[1] == 'atan':
        p[0] = Atan(p[3])
    elif p[1] == 'tan':
        p[0] = Tan(p[3])
    elif p[1] == 'sec':
        p[0] = Sec(p[3])
    elif p[1] == 'ln':
        p[0] = Ln(p[3])
    elif p[1] == 'log':
        p[0] = Log(p[3], p[5])
    
def p_expression_group(p):
    '''expression : LPAREN expression RPAREN'''
    p[0] = p[2]

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = Constant(p[1])

def p_expression_variable(p):
    '''expression : VARIABLE'''
    p[0] = Variable(p[1])

def p_expression_constants(p):
    '''expression : PI
                  | E'''
    if p[1] == 'pi':
        p[0] = Constant(3.141592653589793)
    elif p[1] == 'e':
        p[0] = Constant(2.718281828459045)

def p_error(p):
    if p:
        error_message = f"Błąd składniowy: {p.value} na pozycji linia: {p.lineno}, kolumna: {find_column(p.lexer.lexdata, p.lexpos)}"
    else:
        error_message = "Błąd składniowy: koniec wyrażenia"
    raise SyntaxError(error_message)

def find_column(input, lexpos):
    last_cr = input.rfind('\n', 0, lexpos)
    if last_cr < 0:
        column = lexpos + 1
    else:
        column = lexpos - last_cr
    return column
    
parser = yacc.yacc()
