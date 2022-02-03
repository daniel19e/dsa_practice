
n = int(input())
v = [int(x) for x in input().split()]


lowest = 0
largest = 0
v.sort()
for i in range(n):
    if v[0] == v[i]:
        lowest += 1
    elif v[n-1] == v[i]:
        largest += 1

print(n-lowest-largest)
    

