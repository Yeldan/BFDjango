import math
a = int(input())
b = int(input())

for i in range(a, b + 1):
    Sqrt = int(math.sqrt(i))
    if  Sqrt * Sqrt == i:
        print(i, end = " ")





