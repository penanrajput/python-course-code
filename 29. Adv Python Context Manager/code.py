"""
# Implementing a Context Manager as a Class:
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.object = open(self.filename, self.mode)
        return self.object

    def __exit__(self, type, value, traceback):
        self.object.close()


with File("Open.txt", "w") as f:
    f.write("Some text is being written on file")

print(f.closed)

"""
"""
# implementation a Context Manager using Generator (a better way)
from contextlib import contextmanager


@contextmanager  # decorator 
def file(filename, mode):
    f = open(filename, mode)
    yield f
    f.close()


with file("Open.txt", "w") as f:
    f.write("Implementation of Context Manager using Generator ")

print(f.closed)
"""
"""
# Handling Exceptions
# Open Folder as argument
# and listing the filenames

# Normal Code
cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)
"""
"""
# With Context Manager
import os
from contextlib import contextmanager


@contextmanager  # decorator
def listfiles(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)``
        yield
    finally:
        os.chdir(cwd)


with listfiles("Sample-Dir-One"):
    print(os.listdir())

with listfiles("Sample-Dir-Two"):
    print(os.listdir())
"""

