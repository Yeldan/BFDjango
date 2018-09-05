def squirrel_play(temp, is_summer):
    if is_summer and (temp >= 60 and temp <= 100):
        return True
    return temp >= 60 and temp <= 90