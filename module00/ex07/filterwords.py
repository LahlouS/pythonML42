from sys import argv
import re
import string

output = []
if len(argv) == 3 and argv[2].isdigit():
    size = int(argv[2])
    tr = ''.join([c for c in argv[1] if not (c in string.punctuation)])
    output = [word for word in re.split(' |\t|\n|\r|\v', tr) if len(word) >= size]
    print(output)
else:
    print('ERROR')
