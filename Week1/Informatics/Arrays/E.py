n = int(input())

a = list(map(int, input().split()))
for x in range(1, n):
    if a[x] * a[x-1] > 0:
       print("YES")
       break 
else:
    print("NO")