def near_ten(num):
    if (num % 10 >= 0 and num % 10 <= 2) or (num % 10 >= 8 and num % 10 <= 10):
        return True
    return False