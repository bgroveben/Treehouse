favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']
print()
print(favorite_things)
print()

# Create a new variable named slice1 that has the second, third, and fourth items from favorite_things.
slice1 = favorite_things[1:4]
print(slice1)
print()

# Get the last two items form favorite_things and put them into slice2.
slice2 = favorite_things[-2:]
print(slice2)
print()

# Make a copy of favorite_things and name it sorted_things, then sort sorted_things.
sorted_things = favorite_things[:]
sorted_things.sort()
print(sorted_things)
