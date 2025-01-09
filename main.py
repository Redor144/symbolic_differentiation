from symbolic.lexer import lexer
from symbolic.parser import parser

if __name__ == '__main__':
    expressions = [
        "sin(x)",
        "cos(x)",
        "tan(x)",
        "sec(x)",
        "ln(x)",
        "sqrt(x^2)",
        "abs(x)",
        "exp(x)",
        "sinh(x)",
        "cosh(x)",
        "tanh(x)",
        "asin(x)",
        "acos(x)",
        "atan(x)",
        "x^2 + 3*x + 5",
        "2 * (x + 1)",
        "pi * r^2",
        "e^x",
        "sqrt(x^2 + y^2)",
        "100*x^2",
        "x^3*e^x",
        "ln(x^2 + 1)",
        "ln(x^2)",
        "log(2, log(2, x))",
        "log(2, x^2)",
        "log(2, x)",
        "lm(x)",
        "lm*(x^2)"
    ]

    for expr in expressions:
        print(f"Wyrażenie: {expr}")
        try:
            lexer.input(expr)
            parsed_expr = parser.parse(expr)
            print(f"Parsowane wyrażenie: {parsed_expr}")
            derivative = parsed_expr.differentiate("x").simplify()
            print(f"Pochodna: {derivative}")
        except Exception as e:
            print(f"Błąd: {e}")
        print("-" * 40)
