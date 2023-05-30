import sys

translation_table = str.maketrans("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")

for index, arg in enumerate(sys.argv):
	if arg != sys.argv[0]:
		print(arg.translate(translation_table), end="")
	if index != len(sys.argv) - 1:
		print("", end=" ")
print("")


