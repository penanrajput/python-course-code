def add(x, y):
    return x + y


def sub(x, y):
    return x - y


# as we implemented new multiply method is started showing error
# crashing our python project
# so testing in python is important
def multiply(x, y):
    """Function to perform multiply"""
    return x * (-1 * y)
    # return x * y


def division(x, y):
    """Function to perform division"""
    if y == 0:
        raise ValueError("Can;t divide by zero")
    return x / y


def eq(x, y):
    """Function to perform (x+y)*x+(x+y)*y"""
    sum = add(x, y)
    mult = multiply(sum, x) + multiply(sum, y)
    return mult


def boolNot(num):
    """ return True if num is not 0 """
    return num != 0


def TestIn(num):
    """Return 3 times value of num"""
    return num * 3


def GreaterEqual(num):
    """ Return Twice the num"""
    return num * 2


class Arithmatic:
    """class with add function"""

    def __init__(self, *args):
        self.foo = list(args)

    def add(self, num, foo):
        return num + foo

    def __repr__(self):
        return "Arithmatic: {}".format(self.foo)

    def __str__(self):
        self.foo = [str(item) for item in self.foo]
        return "Arithmatic(string): {}".format(", ".join(self.foo))


def HasAttr(object, method):
    """method should be String"""

    if hasattr(object, method):
        print("{} has attr {}".format(object, method))
    else:
        print("{} hasn't attr {}".format(object, method))


h = Arithmatic(10, 20, 30)

result = h.add(10, 20)


string = "Penan"

foo = "ABCD"
bar = "Hello World"
# bar = 1234


a = 10
b = 20

email = "chetanrajput2777c@gmail.com"

