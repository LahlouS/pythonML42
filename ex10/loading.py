import time

def ft_progress(listy):
    i = 0
    past = int(time.time())
    while i < len(listy):
        print('time --> ', int(time.time()) - past)
        past = int(time.time())
        print('')
        yield listy[i]
        i += 1

for i in ft_progress([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
    print('main --> ', i)
    time.sleep(1)

