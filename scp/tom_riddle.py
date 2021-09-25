import sys
input = sys.stdin.readline

s = set()
n = int(input())

for i in range(n):
    name = str(input())
    if name in s:
        print('YES')
    else:
        print('NO')
        s.add(name)
