def missing_char(str, n):
    s2 = str[n+1:]
    s1 = str[:n]
    return s1 + s2
