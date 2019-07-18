val = 5

foo = None
# foo = 10


class Add:
    pass


class Multiply:
    pass


a = Add()
m = Multiply()

a = 22 / 7  # 3.142857142857143
b = 3.14
difference = a - b
# round (a-b, 2) # 0.01

# Some exception code
def fun(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = 0
        return "Division by Zero."
    finally:
        print("Result -> {}", format(result))
