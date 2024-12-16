import ply.lex as lex

tokens = (
    'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'POWER', 
    'LPAREN', 'RPAREN',
    'SIN', 'COS', 'TAN', 'SEC', 'LN', 'SQRT', 'ABS', 'EXP',
    'SINH', 'COSH', 'TANH', 'ASIN', 'ACOS', 'ATAN', 'LOG',
    'PI', 'E',
    'VARIABLE', 'COMMA'
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_POWER = r'\^'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','

def t_LN(t):
    r'ln'
    return t

def t_SQRT(t):
    r'sqrt'
    return t

def t_ABS(t):
    r'abs'
    return t

def t_EXP(t):
    r'exp'
    return t

def t_SINH(t):
    r'sinh'
    return t

def t_COSH(t):
    r'cosh'
    return t

def t_TANH(t):
    r'tanh'
    return t

def t_ASIN(t):
    r'asin'
    return t

def t_ACOS(t):
    r'acos'
    return t

def t_ATAN(t):
    r'atan'
    return t

def t_SIN(t):
    r'sin'
    return t

def t_COS(t):
    r'cos'
    return t

def t_TAN(t):
    r'tan'
    return t

def t_SEC(t):
    r'sec'
    return t

def t_LOG(t):
    r'log'
    return t

def t_PI(t):
    r'pi'
    return t

def t_E(t):
    r'e'
    return t

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_]\w*'
    return t

t_ignore = ' \t'

def t_error(t):
    print(f"Błąd leksykalny: {t.value[0]}")
    t.lexer.skip(1)

lexer = lex.lex()