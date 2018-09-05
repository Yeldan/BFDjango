def double_pow(a , n):
    x = 1
    for item in range(n):
        x *= a
    return x

arr = list(map(float, input().split()))

print(double_pow(arr[0], int(arr[1])))