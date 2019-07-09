# Derived.py
from Base import Base

class Derived(Base):
    def __init__(self):
        self.foo = 12

d = Derived ()
print('foo -> ', d.foo) # this is serios problem,
    # User / Developer should not change Module level code
