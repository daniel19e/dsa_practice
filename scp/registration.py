import sys
input = sys.stdin.readline

n = int(input())
m = {}

for i in range(n):
    name = str(input().strip('\n'))
    if name not in m:
        print("OK")
        m[name] = 1
    else:
        print(name + str(m[name]))
        m[name] += 1
 
        
