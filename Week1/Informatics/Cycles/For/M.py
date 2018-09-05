n = int(input())
i = 1
count = 0
while i <= n:
    num = int(input())
    i += 1
    if num == 0:
        count += 1
print(count)