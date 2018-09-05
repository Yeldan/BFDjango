x = int(input())
cnt = 0
for i in range(0, x):
    i += 1
    if x % i == 0:
        cnt += 1
print(cnt)