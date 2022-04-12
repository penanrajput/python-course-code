# What is difference between "==" and "is"
# "==" checks for equality
# "is" checks for identity

# Some Real life examples
5 == 5  # True
'coke' == 'pepsi'  # False
'pepsi' == 'pepsi'  # True

'coke' is 'pepsi'  # False
'pepsi' is 'pepsi'  # True
# --------------------------------------------------
l1 = [1, 2, 3, 4, 5]
l2 = [1, 2, 4, 5]

# == checks for content
# is checks for memory address

l1 == l2  # False
l1 is l2  # False

# l3 and l4 have content same but have different memory address
l3 = [1, 2, 3]
l4 = [1, 2, 3]

# now we check for == and is
l3 == l4  # True
l3 is l4  # False
# as You see l3 and l4 have different memory addreess
# is returns False


l4 = l3
# now if we store the l3 into l4 i.e. it saves the whole l3 with memory address same to l3 refers to
# memory location of l3 and l4 is same now

l3 == l4  # True
l3 is l4  # True


# now experiment time
l3[0] = 6
print(l3)  # [6, 2, 3]
print(l4)  # [6, 2, 3] # magic, but its true

l3 is l4

# we talked a lot about memory location
# print the memory location

print(id(l3))  # 2356404431112
print(id(l4))  # 2356404431112

print(id(l3) == id(l4))  # True
