import sys
input = sys.stdin.readline

n = int(input())
nums = input().split()
s = set()
arr = []
for i in range(n):
    if nums[i] not in s:
        s.add(nums[i])

