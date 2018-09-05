def make_bricks(small, big, goal):
    if goal % 5 - small <= 0 and goal % 5 >= 0 and small + 5 * big >= goal:
        return True
    return False