import game

gotChar = game.Stark("dontKnow")
print('1:', gotChar.is_alive)
gotChar.print_house_words()
gotChar.die()
print('2:', gotChar.is_alive)

print('--------------------------------')

arya = game.Stark("Arya")
print(arya.__dict__)

arya.print_house_words()

print(arya.is_alive)
arya.die()
print(arya.is_alive)

print(arya.__doc__)