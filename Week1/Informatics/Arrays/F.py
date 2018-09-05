n = int(input())

a = list(map(int, input().split()))
s = 0
for x in range(1, n-1):
    if a[x-1] < a[x] and a[x] > a[x+1]: 
        s += 1
print(s)