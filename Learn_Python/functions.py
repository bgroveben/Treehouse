# Demonstration of how functions work.

def hows_the_parrot():
    print("He's pining for the fjords.")

hows_the_parrot()


def lumberjack(name, pronoun):
    print("{}'s a lumberjack and {}'s okay!".format(name, pronoun))

lumberjack("Ben", "he")


def average(num1, num2):
    return (num1 + num2) / 2

avg = average(2, 8)
print(avg)
