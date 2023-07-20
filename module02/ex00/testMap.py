

def plusPlus(x, y):
	return x + y

def ft_map(func, iterable, *iterables):
	lenGood = len(iterable)
	for obj in iterables:
		if len(obj) < lenGood:
			lenGood = len(obj)
	i = 0
	while i < lenGood:
		args = []
		for stuff in iterables:
			args.append(stuff[i])
		yield func(iterable[i], *args)
		i += 1

# print(list(ft_map(lambda dum, dumber: dum + dumber, [1, 2, 3, 4, 5])))
# print(list(ft_map(plusPlus, [1, 2, 3, 4, 5])))

print(list(map(plusPlus, [0,2,3,4,5,6,7,8,9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8])))
print(list(ft_map(plusPlus, [0,2,3,4,5,6,7,8,9, 10, 11], [0, 1, 2, 3, 4, 5, 6, 7, 8])))
