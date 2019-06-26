s = "String in Stack File"
n = 50
def foo(arg):
  print(f"{arg}")
def prints():
    print(s)
k = "Another String"
m = k + "Another"
n = 90

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
