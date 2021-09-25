import sys
input = sys.stdin.readline

n = int(input())
s = str(input())
m = {}

for i in range(n-1):
    pair = s[i:i+2]
    if pair in m:
        m[pair] += 1
    else:
        m[pair] = 1

maxval = 0
bestkey = ''
for key, val in m.items():
    if val > maxval:
        maxval = val
        bestkey = key

print(bestkey)
