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
print('Vector:', v1.dot(v2))
test1 = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
test2 = np.array([10.0, 11.0, 12.0, 13.0, 14.0, 15.0])
print('Numpy:', np.dot(test1, test2))

print('\n\n--------------switching v1, v2, v3 shape---------------')

print('initial values v1:', v1.values, 'after switch values v1:', v1.T().values)
print('initial values v2:', v2.values, 'after switch values v2:', v2.T().values)
print('initial values v3:', v3.values, 'after switch values v3:', v3.T().values)

print('\n\n--------------__add__ v1, v2---------------')
v12 = v1 + v2

print(v12.values)

print('\n\n--------------__sub__ v1, v2---------------')
v12 = v1 - v2
print(v12)

print('\n\n------creating new vectors v4 v5 in row shape----------')
v3 = Vector([[1, 2, 3]])
v4 = Vector([[4, 5, 6]])
print(v3.values)
print(v4.values)


print('\n\n------testing dot product----------')
print('v3.dot(v4):', v3.dot(v4))
np3 = np.array([1, 2, 3], float)
np4 = np.array([4, 5, 6], float)
print('np.dot(np3, np4):', np.dot(np3, np4))

print('\n\n------testing __mul__----------')
print('v4 * v3.dot(v4):', v4 * v3.dot(v4))
print('np4 * np.dot(np3, np4):', np4 * np.dot(np3, np4))

print('\n\n------testing __truediv__----------')
print('v4 / v3.dot(v4):', v4 / v3.dot(v4))
print('np4 / np.dot(np3, np4):', np4 / np.dot(np3, np4))