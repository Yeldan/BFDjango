x = int(input())
for i in range(2, x+1):
    if not x % i:
        print(i)
        break