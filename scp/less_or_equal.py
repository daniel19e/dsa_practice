n, k = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]

v.sort()

if k==0:
    if v[0] == 1:
        print(-1)
    else:
        print(1)
elif k==n:
    print(v[n-1])
elif v[k-1] == v[k]:
    print(-1)
else:
    print(v[k-1]) 





