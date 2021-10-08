def factorial(n):
    # Base case
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum(n-1)

def sum_func(n):
    if len(str(n)) == 1:
        return n
    else:
        # strip another digit
        return n % 10 + sum_func(n//10)

def word_split(phrase, list_of_words, output = None):
    if output is None:
        output = []

    for word in list_of_words:

        if phrase.startswith(word):
            output.append(word)
            return word_split(phrase[len(word):], list_of_words, output)
            
    return output