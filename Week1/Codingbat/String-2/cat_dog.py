def cat_dog(str):
    cntcat = 0
    cntdog = 0
    for i in range(len(str)-2):
        if str[i:i+3] == 'cat':
            cntcat = cntcat + 1
        if str[i:i+3] == 'dog':
            cntdog = cntdog + 1
    return cntcat == cntdog