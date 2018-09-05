def xor(x, y):
    if (x == y): 
        return 0
    else: 
        return 1

arr = list(map(int, input().split()))
print(xor(arr[0], arr[1]))