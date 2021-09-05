def balance_check(s):

    if len(s) % 2 != 0:
        return False
    
    opening = '([{'
    matches = [('(',')'),('[', ']'),('{', '}')]

    stack = []

    for parenthesis in s:
        if parenthesis in opening:
            stack.append(parenthesis)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()

            if (last_open, parenthesis) not in matches:
                return False
    
    return len(stack) == 0
