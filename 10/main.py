# youtube.com/@sudoteach

print('')

value = 125
print(value)

mylist = [1, 2, 3]
mylist.append(4)
mylist

import math
math.sqrt(9)

x = int(input())
y = float(input())
if x + y == 10.5:
    print("it's 10.5")
else:
    print("it's", x + y)

print("it's 10.5" if x + y == 10.5 else ("it's", x + y))

for i in range(1, 6):
    print(i)

a = 1
while a <= 5:
    print(a)
    a += 1

def test(name):
    print(f'Your name is: {name}')

question = input("Wat's your name?: ")
test(question)