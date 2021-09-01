"""Given an integer array, output all the unique pairs that sum up to a specific value k.

So the input:

pair_sum([1,3,2,2],4)

would return 2 pairs:

 (1,3)
 (2,2)
"""
def pair_sum(nums, target):
    seen = set()    
    ans = set()    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff not in seen:
            seen.add(nums[i])
        else:
            ans.add((diff, nums[i]))
    return ans



