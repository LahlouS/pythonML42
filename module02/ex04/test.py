import my_minipack.progress
import my_minipack.logger

print('hello')

@my_minipack.logger.log
def myfunc():
	print('in the decorated function')

for i in my_minipack.progress.ft_progress(range(5)):
	pass

myfunc()
myfunc()
myfunc()
myfunc()

