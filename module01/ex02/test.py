from vector import Vector
import numpy as np

print('------------------v1------------------')

v1 = Vector(6)
print(v1.values)
print(v1.shape)
print('\n\n------------------v2------------------')

v2 = Vector((10,16))
print(v2.values)
print(v2.shape)
print('\n\n------------------v3------------------')
v3 = Vector([[1, 2, 3, 4, 5, 6, 7, 8, 9]])
print(v3.values)
print(v3.shape)

print('\n\n--------------v1 dot v2---------------')

print(v1.dot(v2))

test1 = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
test2 = np.array([10.0, 11.0, 12.0, 13.0, 14.0, 15.0])

print(np.dot(test1, test2))