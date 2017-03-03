# Create a function named first_4 that returns the first four items from whatever iterable is given to it.
def first_4(iterable):
    return iterable[:4]

print()
print(first_4(list(range(20))))
print()


# Make a new function named first_and_last_4.
# This function also accepts a single iterable, but this time it will return the first four
# and last four items as a single value.
def first_and_last_4(iterable):
    last_4 = iterable[-4:]
    return first_4(iterable) + last_4

print(first_and_last_4(list(range(20))))
print()


# Create a new function named odds that returns every item with an odd index in a provided iterable.
# For example, it will return the items at index 1, 3, 5, ..., and so on.
def odds(iterable):
    return iterable[1::2]

print(odds(list(range(20))))
print()


# Make a function named reverse_evens that accepts a single iterable as an argument.
# Return every item in the iterable with an even index in reverse.
# For example, with [1, 2, 3, 4, 5] as the input, the function will return [5, 3, 1]
def reverse_evens(iterable):
    return list(reversed(iterable[::2]))

print(reverse_evens([1, 2, 3, 4, 5]))
print(reverse_evens(list(range(1,6))))
print(reverse_evens(list(range(20))))
print()
