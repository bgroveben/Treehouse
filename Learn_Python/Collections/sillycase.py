# Create a function sillycase that takes a single string as an argument.
# sillycase() should return the same string, but with the first half lowercased and the second half uppercased.
# For example, with the string "Treehouse", sillycase() will return "treeHOUSE".
# Don't worry about rounding your halves.

def sillycase(str):
    """
    (string) -> string

    Take a string as input and return that same string with the first half lowercased and the second half uppercased.
    The halves don't need to be rounded.

    >>> sillycase("Treehouse")
    treeHOUSE
    """
    first_half = str[:len(str)//2].lower()
    second_half = str[len(str)//2:].upper()
    return first_half + second_half

print(sillycase("Treehouse"))
