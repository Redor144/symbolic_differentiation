from math import log

class Symbol:
    """Klasa bazowa dla symbolicznych wyrażeń matematycznych."""
    def differentiate(self, variable):
        raise NotImplementedError("Metoda różniczkowania nie jest zaimplementowana.")

    def simplify(self):
        return self

    def __add__(self, other):
        return Add(self, other)

    def __sub__(self, other):
        return Add(self, Constant(-1) * other)

    def __mul__(self, other):
        return Mul(self, other)

    def __truediv__(self, other):
        return Mul(self, Pow(other, Constant(-1)))

    def __repr__(self):
        return str(self)


class Variable(Symbol):
    """Reprezentuje zmienną, np. x."""
    def __init__(self, name):
        self.name = name

    def differentiate(self, variable):
        return Constant(1) if self.name == variable else Constant(0)

    def __repr__(self):
        return self.name


class Constant(Symbol):
    """Reprezentuje stałą, np. 3."""
    def __init__(self, value):
        self.value = value

    def differentiate(self, variable):
        return Constant(0)

    def simplify(self):
        return self

    def __repr__(self):
        return str(self.value)


class Add(Symbol):
    """Dodawanie dwóch symboli."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def differentiate(self, variable):
        return self.left.differentiate(variable) + self.right.differentiate(variable)

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value + right.value)
        if isinstance(left, Constant) and left.value == 0:
            return right
        if isinstance(right, Constant) and right.value == 0:
            return left
        
        if type(left) == type(Variable) == type(right):
            return Mul(Constant(2), left).simplify()
        
        # Uproszczenie: grupowanie podobnych wyrazów (np. 2 * x + x -> 3 * x)
        if isinstance(left, Mul) and isinstance(right, Variable) and left.right == right:
            if isinstance(left.left, Constant):
                return Mul(Constant(left.left.value + 1), right).simplify()
        if isinstance(right, Mul) and isinstance(left, Variable) and right.right == left:
            if isinstance(right.left, Constant):
                return Mul(Constant(right.left.value + 1), left).simplify()
        if isinstance(left, Mul) and isinstance(right, Mul) and type(left.right) == type(right.right):
            if isinstance(left.left, Constant) and isinstance(right.left, Constant):
                return Mul(Constant(left.left.value + right.left.value), left.right).simplify()
        
        return Add(left, right)

    def __repr__(self):
        return f"({self.left} + {self.right})"


class Mul(Symbol):
    """Mnożenie dwóch symboli."""
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def differentiate(self, variable):
        return self.left.differentiate(variable) * self.right + self.left * self.right.differentiate(variable)

    def simplify(self):
        left = self.left.simplify()
        right = self.right.simplify()
        if isinstance(left, Constant) and isinstance(right, Constant):
            return Constant(left.value * right.value)
        if isinstance(left, Constant) and left.value == 0 or isinstance(right, Constant) and right.value == 0:
            return Constant(0)
        if isinstance(left, Constant) and left.value == 1:
            return right
        if isinstance(right, Constant) and right.value == 1:
            return left
        
        if isinstance(left, Pow) and isinstance(right, Pow) and left.base == right.base:
            return Pow(left.base, Add(left.exponent, right.exponent).simplify())
        
        if isinstance(left, Variable) and isinstance(right, Pow) and left == right.base:
            return Pow(left, Add(Constant(1), right.exponent).simplify())
        if isinstance(right, Variable) and isinstance(left, Pow) and right == left.base:
            return Pow(right, Add(Constant(1), left.exponent).simplify())
        
        if isinstance(left, Variable) and isinstance(right, Variable) and left == right:
            return Pow(left, Constant(2))
        
        if isinstance(left, Mul) and (isinstance(left.right, Variable) or isinstance(left.right, Pow)) and (isinstance(right, Variable) or isinstance(right, Pow)):
            return Mul(left.left, Mul(left.right, right)).simplify()
        if isinstance(left, Mul) and (isinstance(left.right, Variable) or isinstance(left.right, Pow)) and isinstance(right, Mul) and (isinstance(right.right, Variable) or isinstance(right.right, Pow)):
            return Mul(Mul(left.left, right.left), Mul(left.right, right.right)).simplify()
        
        if isinstance(right, Constant) and isinstance(left, Add):
            return Add(Mul(left.left, right), Mul(left.right, right)).simplify()
        
        if isinstance(left, Constant) and isinstance(right, Add):
            return Add(Mul(left, right.left), Mul(left, right.right)).simplify()
        
        if isinstance(left, Constant) and isinstance(right, Mul) and isinstance(right.left, Constant):
            return Mul(Mul(left, right.left), right.right).simplify()
        
        if isinstance(left, Mul) and isinstance(right, Mul) and isinstance(right.left, Constant) and isinstance(left.left, Constant):
            return Mul(Mul(left.left, right.left), Mul(left.right, right.right)).simplify()

        return Mul(left, right)
        
    def __repr__(self):
        return f"({self.left} * {self.right})"


class Sin(Symbol):
    """Reprezentuje funkcję sin(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return Cos(self.arg) * self.arg.differentiate(variable)

    def simplify(self):
        arg = self.arg.simplify()
        return Sin(arg)

    def __repr__(self):
        return f"sin({self.arg})"


class Cos(Symbol):
    """Reprezentuje funkcję cos(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return Constant(-1) * Sin(self.arg) * self.arg.differentiate(variable)

    def simplify(self):
        arg = self.arg.simplify()
        return Cos(arg)

    def __repr__(self):
        return f"cos({self.arg})"

class Pow(Symbol):
    """Reprezentuje potęgowanie."""
    def __init__(self, base, exponent):
        self.base = base
        self.exponent = exponent

    def differentiate(self, variable):
        base_diff = self.base.differentiate(variable)
        exponent_diff = self.exponent.differentiate(variable)
        return (
            self.exponent * Pow(self.base, self.exponent + Constant(-1)) * base_diff
            + self * Ln(self.base) * exponent_diff
        )

    def simplify(self):
        base = self.base.simplify()
        exponent = self.exponent.simplify()
        if isinstance(base, Constant) and isinstance(exponent, Constant):
            return Constant(base.value**exponent.value)
        if isinstance(exponent, Constant) and exponent.value == 1:
            return base
        if isinstance(exponent, Constant) and exponent.value == 0:
            return Constant(1)
        if isinstance(base, Pow):
            return Pow(base.base, base.exponent * self.exponent).simplify()
        return Pow(base, exponent)

    def __repr__(self):
        return f"({self.base}^{self.exponent})"

class Abs(Symbol):
    """Reprezentuje funkcję abs(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return self.arg.differentiate(variable) * self.arg / Abs(self.arg)

    def simplify(self):
        arg = self.arg.simplify()
        if isinstance(arg, Constant):
            return Constant(abs(arg.value))
        return Abs(arg)

    def __repr__(self):
        return f"abs({self.arg})"

class Sqrt(Symbol):
    """Reprezentuje funkcję sqrt(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return self.arg.differentiate(variable) / (Constant(2) * Sqrt(self.arg))

    def simplify(self):
        arg = self.arg.simplify()
        if isinstance(arg, Pow) and isinstance(arg.exponent, Constant) and arg.exponent.value == 2:
            # sqrt(x^2) = |x|
            return Abs(arg.base)
        return Sqrt(arg)

    def __repr__(self):
        return f"sqrt({self.arg})"

class Exp(Symbol):
    """Reprezentuje funkcję exp(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return self.arg.differentiate(variable) * Exp(self.arg)

    def simplify(self):
        arg = self.arg.simplify()
        if isinstance(arg, Ln):
            return arg.arg
        return Exp(arg)

    def __repr__(self):
        return f"exp({self.arg})"

class Sinh(Symbol):
    """Reprezentuje funkcję sinh(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return Cosh(self.arg) * self.arg.differentiate(variable)

    def simplify(self):
        arg = self.arg.simplify()
        return Sinh(arg)

    def __repr__(self):
        return f"sinh({self.arg})"

class Cosh(Symbol):
    """Reprezentuje funkcję cosh(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return Sinh(self.arg) * self.arg.differentiate(variable)

    def simplify(self):
        arg = self.arg.simplify()
        return Cosh(arg)

    def __repr__(self):
        return f"cosh({self.arg})"

class Tanh(Symbol):
    """Reprezentuje funkcję tanh(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return Pow(Sec(self.arg), Constant(2)) * self.arg.differentiate(variable)

    def simplify(self):
        arg = self.arg.simplify()
        return Tanh(arg)

    def __repr__(self):
        return f"tanh({self.arg})"

class Asin(Symbol):
    """Reprezentuje funkcję asin(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return self.arg.differentiate(variable) / Sqrt(Constant(1) - Pow(self.arg, Constant(2)))

    def simplify(self):
        arg = self.arg.simplify()
        return Asin(arg)

    def __repr__(self):
        return f"asin({self.arg})"

class Acos(Symbol):
    """Reprezentuje funkcję acos(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return Mul(Constant(-1), self.arg.differentiate(variable)) / Sqrt(Constant(1) - Pow(self.arg, Constant(2)))

    def simplify(self):
        arg = self.arg.simplify()
        return Acos(arg)

    def __repr__(self):
        return f"acos({self.arg})"

class Atan(Symbol):
    """Reprezentuje funkcję atan(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return self.arg.differentiate(variable) / (Constant(1) + Pow(self.arg, Constant(2)))

    def simplify(self):
        arg = self.arg.simplify()
        return Atan(arg)

    def __repr__(self):
        return f"atan({self.arg})"

class Sec(Symbol):
    """Reprezentuje funkcję sec(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return Sec(self.arg) * Tan(self.arg) * self.arg.differentiate(variable)

    def simplify(self):
        arg = self.arg.simplify()
        return Sec(arg)

    def __repr__(self):
        return f"sec({self.arg})"

class Tan(Symbol):
    """Reprezentuje funkcję tan(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return Pow(Sec(self.arg), Constant(2)) * self.arg.differentiate(variable)

    def simplify(self):
        arg = self.arg.simplify()
        return Tan(arg)

    def __repr__(self):
        return f"tan({self.arg})"
    
class Ln(Symbol):
    """Reprezentuje funkcję ln(x)."""
    def __init__(self, arg):
        self.arg = arg

    def differentiate(self, variable):
        return self.arg.differentiate(variable) / self.arg

    def simplify(self):
        arg = self.arg.simplify()
        if isinstance(arg, Constant):
            if arg.value == 1:
                return Constant(0)  # ln(1) = 0
            elif arg.value == 2.718281828459045:
                return Constant(1)  # ln(e) = 1
        return Ln(arg)

    def __repr__(self):
        return f"ln({self.arg})"
    
class Log(Symbol):
    def __init__(self, base, arg):
        self.base = base
        self.arg = arg

    def __repr__(self):
        return f"log({self.base}, {self.arg})"

    def differentiate(self, var):
        return Mul(self.arg.differentiate(var), Pow(Mul(Ln(self.base), self.arg),Constant(-1))).simplify()

    def simplify(self):
        if isinstance(self.arg, Constant) and isinstance(self.base, Constant):
            return Constant(log(self.arg.value, self.base.value))
        return Log(self.base.simplify(), self.arg.simplify())


