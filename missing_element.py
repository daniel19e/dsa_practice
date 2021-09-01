"""Consider an array of non-negative integers. 
A second array is formed by shuffling the elements of the first array and deleting a random element. 
Given these two arrays, find which element is missing in the second array."""

def finder(arr1, arr2):
    seen = {}
    """add values from first array to hash table
    count the number of times the key appears in the array,
    and substract 1 each time it appears in the second array,
    then return the key whose value isn't 0"""
    for num in arr1:
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
    for num in arr2:
        if num in seen:
            seen[num] -= 1 
        else:
            seen[num] = 1
    
    for k in seen:
        if seen[k] != 0:
             return k

