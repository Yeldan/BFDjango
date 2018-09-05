def string_match(a, b):
    cnt = 0
    minstr = min(len(a), len(b))
    for i in range(minstr - 1):
        if a[i+1] == b[i+1] and a[i] == b[i]:
            cnt = cnt + 1
        return cnt