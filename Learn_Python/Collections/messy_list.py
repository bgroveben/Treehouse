messy_list = ["a", 2, 3, 1, False, [1, 2, 3]]

# Move the 1 from index 3 to index 0.
messy_list.pop(3) and messy_list.insert(0, 1)
print(messy_list)

# Now use remove() and/or del to remove the string, the boolean, and the list from inside of messy_list.
# When you're done, messy_list should only contain integers.
messy_list.remove('a')
messy_list.remove(False)
del messy_list[-1]
print(messy_list)
