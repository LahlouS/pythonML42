from sys import argv

morseDico = {
    'A' : '.-',
    'B' : '-...',
    'C' : '-.-.',
    'D' : '-..',
    'E' : '.',
    'F' : '..-.',
    'G' : '--.',
    'H' : '....',
    'I' : '..',
    'J' : '.---',
    'K' : '-.-',
    'L' : '.-..',
    'M' : '--',
    'N' : '-.',
    'O' : '---',
    'P' : '.--.',
    'Q' : '--.-',
    'R' : '.-.',
    'S' : '...',
    'T' : '-',
    'U' : '..-',
    'V' : '...-',
    'W' : '.--',
    'X' : '-..-',
    'Y' : '-.--',
    'Z' : '--..',
    '0' : '-----',
    '1' : '.----',
    '2' : '..---',
    '3' : '...--',
    '4' : '....-',
    '5' : '.....',
    '6' : '-....',
    '7' : '--...',
    '8' : '---..',
    '9' : '----.'
}

nbargs = len(argv)

if nbargs > 1:
    i = 1
    while i < nbargs:
        
        for char in argv[i]:
            try:
                print(morseDico[char.upper()], end='')
                print(' ', end='')
            except:
                if char.isspace():
                    print('/', end='')
                else:
                    print('ERROR')
        if i != nbargs - 1:
            print(' ', end='')
        i += 1 
    print()