import random
arr = []
for i in range(5):
    r = random.randint(0,120)
    if r > 70 :
        arr.append(r)
print(arr)