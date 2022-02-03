n = int(input())
problems = 0

for i in range(n):
    a, b, c = [int(x) for x in input().split()]
    if a + b + c >= 2:
        problems +=1

print(problems)