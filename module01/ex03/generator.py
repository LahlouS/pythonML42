import re
import string
import random

def generator(text, sep=" ", option=None):
    '''
    Splits the text according to sep value and yield the substrings.
    option precise if an action is performed to the substrings before it is yielded.
    '''
    try:
        outlist = [words for words in re.split(sep, text)]
    except:
        option = 'pb'
    
    if option == 'ordered':
        outlist.sort()
    elif option == 'unique':
        outlist = list(dict.fromkeys(outlist))
    elif option == 'shuffle':
        temp = [""] * len(outlist)
        for word in outlist:
            randi = random.randint(0, len(outlist) - 1)
            while temp[randi] != "":
                randi = random.randint(0, len(outlist) - 1)
            else:
                temp[randi] = word
        outlist = temp
    elif option != None:
        outlist = ["ERROR"]
    

    for word in outlist:
        yield word

for word in generator(1.0, ".", 'shuffle'):
    print(word)