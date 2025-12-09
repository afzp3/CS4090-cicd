from math import sqrt, log, sin, cos, radians

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    try:
        return a / b
    except:
        raise ZeroDivisionError("Cannot divide by zero")

def logfunc(a, base=10):
    if a <= 0:
        raise ValueError("Log is undefined for zero or negative numbers")
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1.")
    return log(a, base)

def squared(a):
    return a ** 2

def sinfunc(a, in_degrees=False):
    if in_degrees:
        a = radians(a)
    return sin(a)

def cosfunc(a, in_degrees=False):
    if in_degrees:
        a = radians(a)
    return cos(a)

def squareroot(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return sqrt(a)

def percentage(a, b):
    # a is x% of b
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return (a / b) * 100
