# Demonstration of Pythons random module.

# EXAMPLE
# random_item("Treehouse")
# The randomly selected number is 4.
# The return value would be "h".

import random

def random_item(iterable):
    selected_number = random.randint(0, len(iterable) - 1)
    print(selected_number)
    return iterable[selected_number]

print(random_item("Treehouse"))
