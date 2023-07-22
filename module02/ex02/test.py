def myfunction():
    print('laaaaaaaaaaaaaa ')

print('1', myfunction.__name__)

foo = myfunction

print('2', foo.__name__)

bar = foo

bar()

print(bar.__name__)