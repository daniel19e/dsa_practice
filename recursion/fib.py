def fib_rec(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    a = 0
    b = 1
    ans = 0
    for i in range(1,n):
        ans = a + b
        a = b
        b = ans
    return ans

#cache
n = 10
cache = [None]*(n+1)

def fib_dyn(n):
    #Base case
    if n == 0 or n == 1:
        return n
    #check cache
    if cache[n] != None:
        return cache[n]
    #keep setting cache
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)


print(fib_rec(10))
print(fib_iter(10))