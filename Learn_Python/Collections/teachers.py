# Create a function named num_teachers that takes a single argument.
# The argument will be a dictionary of Treehouse teachers and their courses.
# The num_teachers function should return an integer of how many teachers are in the dict.
# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
# Each key will be a Teacher and the value will be a list of courses.
def num_teachers(some_dict):
    """
    (dict)-> int

    This function will return an integer for how many teachers are in the dict.

    example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
               'Kenneth Love': ['Python Basics', 'Python Collections']}
    >>> print(num_teachers(example))
    2
    """
    count = 0
    for key in some_dict:
        count += 1
    return count


example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
           'Kenneth Love': ['Python Basics', 'Python Collections']}
print(num_teachers(example))
print()



# Create a new function named num_courses that will receive the same dictionary as its only argument.
# The function should return the total number of courses for all of the teachers.
def num_courses(some_dict):
    """
    (dict)-> dict

    Returns the total number of courses for all of the teachers.

    example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
               'Kenneth Love': ['Python Basics', 'Python Collections']}
    >>> print(num_courses(example))
    4
    """
    counts = 0
    for teacher, course in some_dict.items():
        counts += len(some_dict[teacher])
    return counts


example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
           'Kenneth Love': ['Python Basics', 'Python Collections']}
print(num_courses(example))
print()



# For this step, make another new function named courses that will, again, take the dictionary of teachers and courses.
# The courses() function should return a single list of all of the available courses in the dictionary.
# No teachers, just course names.
