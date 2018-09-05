def make_chocolate(small, big, goal):
    mbig = goal / 5
  
    if big < mbig:
        if small >= (goal - big * 5):
            return goal - big * 5
  
    if big >= mbig:
        if small >= (goal - mbig * 5):
            return goal - mbig * 5

    return -1