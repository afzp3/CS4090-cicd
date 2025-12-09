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
        return ZeroDivisionError

def squared(a):
    return a ** 2