from my_minipack import progress
from my_minipack import logger

print('hello')

@logger.log
def myfunc():
	print('in the decorated function')

for i in progress.ft_progress(range(5)):
	pass

myfunc()
myfunc()
myfunc()
myfunc()

