n = int(input())
count = 0
a = list(map(int, input().split()))
for x in range(n):
    if a[x-1] < a[x] and x != 0: 
        count += 1
print(count)