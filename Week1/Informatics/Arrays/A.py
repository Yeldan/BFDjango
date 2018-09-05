n = int(input())

a = list(map(int, input().split()))
for x in range(n):
    if x % 2 == 0: 
        print(a[x])
