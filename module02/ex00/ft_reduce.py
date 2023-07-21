import functools

def add(x, y):
	return x + y

def ft_reduce(function_to_apply, iterable, initial=None):
	iter(iterable)
	i = 1
	ret = initial + iterable[0] if initial != None else iterable[0]
	while i < len(iterable):
		ret = function_to_apply(ret, iterable[i])
		i += 1
	return ret

lst = ['H', 'e', 'l', 'l', 'o',' ', 'w', 'o', 'r', 'l', 'd']
print(functools.reduce(lambda u, v: u + v, lst, '5') )
print(ft_reduce(lambda u, v: u + v, lst, '5'))
