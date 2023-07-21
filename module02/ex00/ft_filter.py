def odd(i):
	return list([(i % 2)])

def sub(i):
	return i[0] - i[1]


def ft_filter(function_to_apply, iterable):
	"""Filter the result of function apply to all elements of the iterable.
	Args:
	function_to_apply: a function taking an iterable.
	iterable: an iterable object (list, tuple, iterator).
	Return:
	An iterable.
	None if the iterable can not be used by the function.
	"""
	if not function_to_apply:
		function_to_apply = lambda x: x
	iter(iterable)
	for i in iterable:
		if function_to_apply(i):
			yield i

print(list( ft_filter(sub, [(1, 1), (2, 2), (2, 3)]) ))
