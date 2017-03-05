#!# Packing and unpacking dictionaries
#!# https://stackoverflow.com/questions/1769403/understanding-kwargs-in-python

print()
my_dict = {"name": "Ben"}
print("Hi, my name is {name}!".format(**my_dict))
print()

# If you use **kwargs in a function, it must be the last input.

# def packer(**kwargs):
def packer(name=None, **kwargs):
	print(kwargs)

packer(name="Ben", num=42, spanish_inquisition=None)
print()


def unpacker(first_name=None, last_name=None):
	if first_name and last_name:
		print("Hi {} {}!".format(first_name, last_name))
	else:
		print("Hi no name!")

unpacker(**{"last_name": "Grove", "first_name": "Ben"})
print()


def packing(**kwargs):
	print(len(kwargs))

packing(name="Ben")
print()
