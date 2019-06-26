print("Running __ini__.py file ")

class class1:
    def __init__(self):
        print("inside __init__.py/class1 class")
    def printclass1(self):
        print("inside class1 class's print function")

class Stack:
    members = []
    def __init__(self, list = None):
        if(list==None):
            self.members = []
        else:
            self.members = list
    def push(self, number):
        self.members.append(number)
    def pop(self):
        self.members.pop()
    def printStack(self):
        print(self.members)
