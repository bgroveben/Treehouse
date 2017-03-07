# Create a function named num_teachers that takes a single argument, which will be a
# dictionary of Treehouse teachers and their courses.
# The num_teachers() function should return an integer for how many teachers are in the dict.
def num_teachers(a_dict):
    """
    (dict) -> int

    Return an integer for how many teachers are in the dict.
    Each key will be a Teacher and the value will be a list of courses.

    example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
               'Kenneth Love': ['Python Basics', 'Python Collections']}
    >>> print(num_teachers(example))
    2
    """
    return len(a_dict.keys())


print()
example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
           'Kenneth Love': ['Python Basics', 'Python Collections']}
print(num_teachers(example))
print()



# Create a function named num_courses that will take the same dictionary as its only argument.
# The num_courses() function should return the total number of courses for all of the teachers.
def num_courses(a_dict):
    """
    (dict) -> int

    Return the total number of courses for all of the teachers.

    example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
               'Kenneth Love': ['Python Basics', 'Python Collections']}
    >>> print(num_courses(example))
    4
    """
    count = 0
    for course in a_dict.values():
        count += len(course)
    return count



example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
           'Kenneth Love': ['Python Basics', 'Python Collections']}
print(num_courses(example))
print()



# Make a function named courses that will, again, take the dictionary of teachers and courses.
# The courses() function should return a single list of all of the available courses in the dictionary.
# No teachers, just course names.
def courses(a_dict):
    """
    (dict) -> list

    Returns a single list of all of the available courses in the dictionary.
    The list will contain all courses for all teachers, but will *not* contain the teachers names.

    example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
               'Kenneth Love': ['Python Basics', 'Python Collections']}
    >>> print(courses(example))
    ['Python Basics', 'Python Collections', 'jQuery Basics', 'Node.js Basics']
    """
    result = []
    for course_list in a_dict.values():
        for each_course in course_list:
            result.append(each_course)
    return result


example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
           'Kenneth Love': ['Python Basics', 'Python Collections']}
print(courses(example))
print()



# Create a function named most_courses that takes the same teacher and course dictionary.
# The most_courses() function should return the name of the teacher with the most courses.
# You might need to hold on to some sort of max_count variable.
def most_courses(a_dict):
    """
    (dict) -> str

    Returns the name of the teacher with the most courses.

    example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
               'Kenneth Love': ['Python Basics', 'Python Collections'],
               'Three Courses': ['Web Development', 'Android Development', 'iOS Development'],
               'Correct Answer': ['More Python', 'More Node.js', 'More jQuery', 'Rails Basics']}
    >>> print(most_courses(example))
    Correct Answer
    """
    max_count = 0
    result = ''
    for teacher, course_list in a_dict.items():
        if len(course_list) > max_count:
            max_count = len(course_list)
            result = teacher
    return result


example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
           'Kenneth Love': ['Python Basics', 'Python Collections'],
           'Three Courses': ['Web Development', 'Android Development', 'iOS Development'],
           'Correct Answer': ['More Python', 'More Node.js', 'More jQuery', 'Rails Basics']}
print(most_courses(example))
print()



# Create a function named stats that takes our teacher dictionary as the only argument.
# The stats() function sould return a list of lists where:
# 1. The first item in each inner list is the teacher's name.
# 2. The second item is the number of courses that teacher has.
# For example, it might return: [["Kenneth Love", 5], ["Craig Dennis", 10]]
def stats(a_dict):
    """
    (dict) -> list of lists

    Returns a list of lists where:
    1. The first item in each inner list is the teacher's name.
    2. The second item is the number of courses that teacher has.

    example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
               'Kenneth Love': ['Python Basics', 'Python Collections'],
               'Three Courses': ['Web Development', 'Android Development', 'iOS Development'],
               'Four Courses': ['More Python', 'More Node.js', 'More jQuery', 'Rails Basics']}
    >>> print(stats(example))
    [['Kenneth Love', 2], ['Four Courses', 4], ['Andrew Chalkley', 2], ['Three Courses', 3]]
    """
    result = []
    for teacher, course_list in a_dict.items():
        item = [teacher, len(course_list)]
        result.append(item)
    return result


example = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
           'Kenneth Love': ['Python Basics', 'Python Collections'],
           'Three Courses': ['Web Development', 'Android Development', 'iOS Development'],
           'Four Courses': ['More Python', 'More Node.js', 'More jQuery', 'Rails Basics']}
print(stats(example))
print()
