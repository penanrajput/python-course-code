def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def multiply(x, y):
    return x * y


def division(x, y):
    if y == 0:
        raise ValueError
    return x / y

