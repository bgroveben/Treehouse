# Let's test unpacking dictionaries in keyword arguments.
# You've used the string .format() method to fill in blank placeholders.
# If you give the placeholder a name, though, like in 'template' below, you fill it in through keyword
# arguments to .format(), like this:
# template.format(name="Kenneth", food="tacos")

# Write a function named string_factory() that accepts a list of dictionaries as an argument.
# Return a new list of strings made by using ** for each dictionary in the list and the 'template' string provided.

template = "Hi, I'm {name} and I love to eat {food}!"

def string_factory(list_of_dicts):
    """
    (list of dicts) -> list of strings

    Take a list of dictionaries as a single argument.
    Return a new list of strings made by using ** for each dict in the list and the 'template' string.

    >>> values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
    >>> string_factory(values)
    ["Hi, I'm Michelangelo and I love to eat PIZZA!", "Hi, I'm Garfield and I love to eat lasagna!"]
    """
    result = []
    for item in range(len(list_of_dicts)):
        result.append(template.format(**list_of_dicts[item]))
    return result


values = [{"name": "Michelangelo", "food": "PIZZA"}, {"name": "Garfield", "food": "lasagna"}]
print(string_factory(values))
