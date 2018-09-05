a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(a, b + 1):
    if d == 0:
        break
    if i % d == c: 
        print(i, end = " ")
    