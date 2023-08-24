import numpy as np

class NumpyCreator(object):
    def __init__(self):
        print('in constructor')

    def is_scalar(self, a):
        if np.isscalar(a):
            return True
        try:
            len(a)
        except TypeError:
            return True
        return False


    def get_shape(self, a):
        """
        Returns the shape of `a`, if `a` has a regular array-like shape.

        Otherwise returns None.
        """
        if self.is_scalar(a):
            return ()
        shapes = [self.get_shape(item) for item in a]
        if len(shapes) == 0:
            return (0,)
        if any([shape is None for shape in shapes]):
            return None
        if not all([shapes[0] == shape for shape in shapes[1:]]):
            return None
        return (len(shapes),) + shapes[0]


    def is_ragged(self, a):
        return self.get_shape(a) is None

    def from_list(self, lst, dtype=None):
        try:
            if isinstance(lst, list) and not self.is_ragged(lst):
                return np.array(lst, dtype=None)
            raise Exception
        except Exception as e:
            print(e)
            return None
    
    def from_tuple(self, tpl, dtype=None):
        try:
            if isinstance(tpl, tuple) and not self.is_ragged(tpl):
                return np.array(tpl, dtype=None)
            raise Exception
        except:
            return None


    def from_iterable(self, itr, dtype=None):
        try:
            if not self.is_ragged(itr):
                return np.array(itr, dtype=None)
        except:
            return None

    def from_shape(self, shape, value=0, dtype=None):
        try:
            return np.full(shape, value, dtype=None)
        except:
            return None

    def random(self, shape):
        try:
            return np.empty(shape, dtype=np.float_)
        except:
            return None

    def identity(self, n):
        try:
            return np.identity(n)
        except:
            return None
