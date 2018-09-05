def front_times(str, n):
    if len(str) < 3:
        front = len(str)
    front = str[:3]
    return n * front