import math

ab = int(input())
bc = int(input())
ac = math.sqrt(ab*ab + bc*bc)
achalf = ac / 2.0
bchalf = bc / 2.0
print(str(int(round(math.degrees(math.acos(bchalf/achalf))))) + '°')