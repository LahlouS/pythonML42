import numpy as np

class NumpyCreator(object):
    def __init__(self):
        print('in constructor')
    
    def from_list(self, lst, dtype=None):
            return np.array(lst, dtype=dtype)
    
    def from_tuple(self, tpl, dtype=None):
        return np.array(tpl, dtype=dtype)

    def from_iterable(self, itr, dtype=None):
        return np.array(list(itr), dtype=dtype)

    def from_shape(self, shape, value=0, dtype=None):
        return np.full(shape, value, dtype=dtype)

    def random(self, shape, dtype=None):
        return np.empty(shape, dtype=dtype)

    def identity(self, n, dtype=None):
        return np.zeros((n, n), dtype=dtype)
