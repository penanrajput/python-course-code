# there is a special technique to define main method in python program, so that it gets executed only when the program is run directly and not executed when imported as a module.

print("__name__: ",__name__)

print(type(__name__ ))

def main():
    print("This only printed if file is run directly")

if __name__=='__main__':
    main()

'''
this is obvious 
if __name__=='python_main_module':
    print("This only printed if file is imported")
'''