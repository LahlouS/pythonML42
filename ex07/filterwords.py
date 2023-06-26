from sys import argv
import re

output = []
if len(argv) == 3 and argv[2].isdigit():
    size = int(argv[2])
    sentence=argv[1]
    output = [word for word in re.split(';|,|\*|\n| ', sentence) if len(word) > size]
    print(output)
else:
    print('ERROR')

    