import random

secretNum = random.randint(1, 100)
print(secretNum)
count = 0


def verify(a, b):
    global count
    if a == b and b == 42:
        print('The answer to the ultimate question of life, the universe and everything is 42.')
    if a < b:
        print('too low')
        count += 1
    elif a > b:
        print('too high')
        count += 1
    elif a == b and count == 0:
        print('well done, you got it first try')
        exit()
    elif a == b:
        print('well done, you got it at attempt {}'.format(count))
        exit()



print('''
    This is an interactive guessing game!
    You have to enter a number between 1 and 99 to find out the secret number.
    Type 'exit' to end the game.
    Good luck !
''')

while 1:
    raw = input('What\'s your guess between 1 and 99? ')
    try:
        verify(int(raw), secretNum)
    except:
        if raw == 'exit':
            print('exiting. . . ')
            exit()
        else:
            print('this is not an integer')
