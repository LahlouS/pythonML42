import random

secret_num = random.randint(1, 99)
guess = None
count = 1

print('''
    This is an interactive guessing game!
    You have to enter a number between 1 and 99 to find out the secret number.
    Type 'exit' to end the game.
    Good luck!
    ''')

while guess != 'exit':
    guess = input('Choose a number from 1 to 99: ')
    try:
        nb = int(guess)
        if nb > 99 or nb < 1:
            print('--> your number must be between 1 and 100')
        elif nb < secret_num:
            print('--> too low')
        elif nb > secret_num:
            print('--> too high')
        else:
            guess = 'exit'
            if nb == 42:
                print('The answer to the ultimate question of life, the universe and everything is 42.')
            if count == 1:
                print('Congratulation, you found it first time !')
            else:
                print('Congrats, you found it\nYou won in {} attemps'.format(count))
        count += 1
    except:
        if guess != 'exit':
            count += 1
            print('--> input error')

print('\nGoodbye')


