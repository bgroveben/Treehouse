# Make a dictionary named player and add two keys to it.
# The first key shall be named "name" and the value shall be any string you want.
# The second key shall be "remaining lives" and the value shall be set to 3.
player = {"name": "Ben", "remaining_lives": 3}

# Now add a "levels" key.
# It shall be a list with the values 1, 2, 3, and 4 in it.
player["levels"] = [1, 2, 3, 4]

# Add an "items" key.
# This key's value shall be another dictionary.
# Give it at least one key and value, but they shall be anything you want.
player["items"] = {"stuff": "amount"}

print(player)
