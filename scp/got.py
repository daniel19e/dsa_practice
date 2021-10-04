
n = int(input())
output = 0
v = []
for i in range(n):
    s = int(input())
    v.append(s)

v.sort()
for i in range(len(v)):
    if v[i] > v[0] and v[i] < v[n-1]:
        output += 1

print(output)