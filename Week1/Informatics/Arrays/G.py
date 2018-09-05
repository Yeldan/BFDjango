n = int(input())

a = list(map(int, input().split()))
for x in reversed(range(n)):
    print(a[x])
