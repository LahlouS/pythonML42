

def plusPlus(x, y, z):
	return x + y + z

def ft_map(func, iterable, *iterables):
	"""
	Map the function to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	lenGood = len(iterable)
	for obj in iterables: # getting the shortest iterable arg
		iter(obj)
		if len(obj) < lenGood:
			lenGood = len(obj)
	i = 0
	while i < lenGood:
		args = []
		for stuff in iterables:
			args.append(stuff[i])
		yield func(iterable[i], *args)
		i += 1

