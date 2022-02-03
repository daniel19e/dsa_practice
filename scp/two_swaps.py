t = int(input())

for _ in range(t):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    b.sort()
    #1 2 3 4 5
    #5 4 3 2 1
    for i in range(n-k, len(b)):
        a.append(b[i])

            
    a.sort()
    #1 2 6 7 8 4 5
    #1 2 4 5 6 7 8
    #8 7 6 5 4 2 1
    print(sum(a[k:]))
