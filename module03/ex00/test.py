from numpyCreator import NumpyCreator
import numpy as np

npc = NumpyCreator()

print('\n ---------- > from_list()')
nparray = npc.from_list([[1,2,3],[6,3,4]])
print(nparray)
# Output :
# array([[1, 2, 3],
# [6, 3, 4]])


print('\n ---------- > from_list() with ununiform data 01')
print(npc.from_list([[1,2,3],[6,4]]))
# Output :
# None

print('\n ---------- > from_list() with ununiform data 02')
print(npc.from_list([[1,2,3],['a','b','c'],[6,4,7]]))
# Output :
# array([['1','2','3'],
# ['a','b','c'],
# ['6','4','7'], dtype='<U21'])

print('\n ---------- > from_list(() called with tuple')

print(npc.from_list(((1,2),(3,4))))
# Output :
# None


print('\n ---------- > from_tuple()')
print(npc.from_tuple(("a", "b", "c")))
# Output :
# array(['a', 'b', 'c'])


print('\n ---------- > from_tuple() called with a list')
print(npc.from_tuple(["a", "b", "c"]))
# Output :
# None

print('\n ---------- > from_iterable()')
print(npc.from_iterable(range(5)))
# Output :
# array([0, 1, 2, 3, 4])

shape=(3,5)
print(f'\n ---------- > from_shape({shape})')
print(npc.from_shape(shape, value=1))
# Output :
# array([[0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0]])
print(f'\n ---------- > random({shape})')

print(npc.random(shape))
# Output :
# array([[0.57055863, 0.23519999, 0.56209311, 0.79231567, 0.213768 ],
# [0.39608366, 0.18632147, 0.80054602, 0.44905766, 0.81313615],
# [0.79585328, 0.00660962, 0.92910958, 0.9905421 , 0.05244791]])

print('\n ---------- > identity')
print(npc.identity(4))
# Output :
# array([[1., 0., 0., 0.],
# [0., 1., 0., 0.],
# [0., 0., 1., 0.],
# [0., 0., 0., 1.]])


# i need to configure the return value to return None instead of raising an error
# Your identity matrice is not good and you need to verify the data type into the function.