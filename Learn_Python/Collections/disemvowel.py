def disemvowel(word):
    """
    (str) -> str

    Takes a word as input and returns that word without the vowels ('a', 'e', 'i', 'o', 'u').
    Removes both uppercase and lowercase letters.

    >>> disemvowel("disemvowel")
    dsmvwl
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for letter in word:
        if letter not in vowels:
            result += letter
    return result


print(disemvowel("disemvowel"))
