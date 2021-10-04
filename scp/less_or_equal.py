import sys
input = sys.stdin.readline

n, k = input().split(' ')
n = int(n)
k = int(k)

v = []

for i in range(n):
    a = int(input())
    v.append(a)
v.sort()

if k == 0:
    if v[0] > 1:
        print(1)
    elif v[0] == 1:
        print(-1)
elif v[k-1] == v[k]:
    print(-1)
else:
    print(v[k-1])



