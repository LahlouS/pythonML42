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
morselist = []

if nbargs > 1:
    i = 1
    while i < nbargs:
        for char in argv[i]:
            try:
                morselist.append(morseDico[char.upper()])
            except:
                if char.isspace():
                    morselist.append('/')
                else:
                    print('ERROR')
                    exit()
        morselist.append('/')
        i += 1
    
    for idx, word in enumerate(morselist):
        if idx != (len(morselist) - 1):
            print(word, end=' ')
        else:
            print()