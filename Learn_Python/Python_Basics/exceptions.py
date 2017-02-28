# Demonstration of try and except.

try:
    speed = int(input("What is the airspeed velocity of an unladen swallow? "))
except ValueError:
    print("What? I don't kno-oooooooooow!")
else:
    print("I think a swallow could go faster than {}.".format(speed))


try:
    count = int(input("Give me a number: "))
except ValueError:
    print("That's not a number, sucka!")
else:
    print("Hi " * count)
