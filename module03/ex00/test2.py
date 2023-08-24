import numpy as np
from numpyCreator import NumpyCreator

def random(shape):
    return np.empty(shape)

npc = NumpyCreator()

shape = (3, 5)
print(random(shape), end='\n\n')
print(npc.random(shape))
