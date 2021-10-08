def permute(s):
    out = []
    if len(s) == 1:
        out = [s]
    else:
        # iterate over string
        for i, letter in enumerate(s):
            # for every permutation resulting from step 2 and 3
            for perm in permute(s[:i] + s[i+1:]):
                out += [letter+perm]
    return out