import sys

translation_table = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
for index, arg in enumerate(reversed(sys.argv)):
	if arg != sys.argv[0]:
		tr = arg.translate(translation_table)
		if (index != len(sys.argv) - 2):
			print(tr[::-1], end=" ")
		else:
			print(tr[::-1], end="")
print("")


