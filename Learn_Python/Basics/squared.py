# Time for a bit of math. Don't be scared.

# EXAMPLES
# squared(5) would return 25
# squared("2") would return 4
# squared("tim") would return "timtimtim"

def squared(arg1):
    try:
        return (int(arg1) ** 2)
    except ValueError:
        return arg1 * len(arg1)

print(squared(5))
print(squared("2"))
print(squared("Ben"))
