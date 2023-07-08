import game

gotChar = game.Stark("dontKnow")
print('1:', gotChar.is_alive)
gotChar.print_house_words()
gotChar.die()
print('2:', gotChar.is_alive)
