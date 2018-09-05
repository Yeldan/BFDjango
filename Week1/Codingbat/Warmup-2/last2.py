def last2(str):
    cnt = 0
    if len(str) - 2 >= 0:
        for i in range(0, len(str) - 2):
            if str[i:i+2] == str[-2:]:
                cnt = cnt + 1
    return cnt