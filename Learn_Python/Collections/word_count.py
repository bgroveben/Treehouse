#!# In this exercise, we're making a counter from scratch.
# https://docs.python.org/3.5/library/collections.html#counter-objects

# Make a function named word_count().
# It should accept a single argument which will be a string.
# The function needs to return a dictionary.
# The keys in the dictionary will be each of the words in the string, lowercased.
# The values will be how many times that particular word appears in the string.

# >>> word_count("I do not like it Sam I Am")
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}


def word_count(a_string):
    """
    (str)-> dict

    Accepts a string as input.
    Returns a dictionary with each word in the string, lowercased, as a key and the number of times
    that the word appears in the string as a value.

    >>> word_count("I do not like it Sam I Am")
    {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
    """
    words = a_string.lower().split()
    counts = {}
    for word in words:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1

    return counts


print(word_count("I do not like it Sam I Am"))
