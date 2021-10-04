n = input().split('+')

l = list(n)
l.sort()
for i in range(len(l)):
    print(l[i],end='')
    if i < len(l)-1:
        print('+',end='')

