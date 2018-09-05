def min4(a, b, c, d):
    return(min(a, b, c, d)) 

arr = list(map(int, input().split()))

print(min4(arr[0], arr[1], arr[2], arr[3]))
