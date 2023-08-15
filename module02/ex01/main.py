class ObjectC(object):
	def __init__(self):
		pass
	def __dir__(self):
		return sorted(self.__dict__.keys())


def what_are_the_vars(*args, **kwargs):
	"""
	...
	"""
	new_obj = ObjectC()
	i = 0
	for arg in args:
		new_obj.__dict__[f'var_{i}'] = arg
		i += 1
	for key, val in kwargs.items():
		if not new_obj.__dict__.get(key):
			new_obj.__dict__[key] = val
		else:
			return None

	return new_obj

def doom_printer(obj):
	if obj is None:
		print("ERROR")
		print("end")
		return
	for attr in dir(obj):
		if attr[0] != '_':
			value = getattr(obj, attr)
			print("{}: {}".format(attr, value))
	print("end")


if __name__ == "__main__":
	obj = what_are_the_vars(7)
	doom_printer(obj)
	obj = what_are_the_vars(None, [])
	doom_printer(obj)
	obj = what_are_the_vars("ft_lol", "Hi")
	doom_printer(obj)
	obj = what_are_the_vars()
	doom_printer(obj)
	obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, a=10, var_0="world")
	doom_printer(obj)
	obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
	doom_printer(obj)

	# showing that the class did not change
	print(ObjectC.__dir__)
