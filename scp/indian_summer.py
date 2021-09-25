import sys
input = sys.stdin.readline

n = int(input())
s = set()
counter = 0

for i in range(n):
    leaf = str(input())
    s.add(leaf)
print(len(s))

