a = int(input())
b = input().split()
c = int(input())
d = input().split()

s1 = set(b)
s2 = set(d)

print(len(s1.union(s2)))