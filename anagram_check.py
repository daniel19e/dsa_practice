"""Given two strings, check to see if they are anagrams"""
def anagram(s1, s2):
    s1 = s1.replace(' ', '')
    s2 = s2.replace(' ', '')

    if len(s1) != len(s2):
        return False
    
    #hash table to keep count of repeated characters
    my_dict = {}

    for i in s1:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    
    for j in s2:
        if j in my_dict:
            my_dict[j] -= 1
        else:
            my_dict[j] = 1
    #check all counts of the letters are equal to 0
    for k in my_dict:
        if my_dict[k] != 0:
            return False
    
    return True

        