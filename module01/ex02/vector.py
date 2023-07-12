import sys
import numpy as np

    # CHECK IF ARG IS REALLY A VECTOR
    # ERROR CHECKING TRY CATCH L.56
    # TEST FOR BOTH SHAPE OF VECTOR
    # FINISH OTHER OPERATION
    # TEST
    
class Vector:
    def __init__(self, arg):
        try:
            self.values = []
            if isinstance(arg, list):
                if len(arg) == 1 and isinstance(arg[0], list):
                    self.values.append([float(val) for val in arg[0]])
                    self.shape = (1, len(arg[0]))
                elif len(arg) != 0:
                    for val in arg:
                        if not isinstance(val, list) or len(val) != 1 or isinstance(val[0], float):
                            raise TypeError('Column vectors values must be lists of single float')
                        else:
                            self.values.append([float(val[0])])
                    self.values = arg
                    self.shape = (len(arg), 1)
            elif isinstance(arg, int):
                self.values = [[float(x)] for x in range(arg)]
                self.shape = (len(self.values), 1)
            elif isinstance(arg, tuple) and len(arg) == 2:
                if arg[0] < arg[1]:
                    self.values = [[float(x)] for x in range(arg[0], arg[1])]
                    self.shape = (len(self.values), 1)
                else:
                    raise TypeError('unvalid range')
            else:
                raise TypeError('Vector instanciation is based on a list, an int or a range (tuple)')
        except (ValueError, TypeError) as t:
            print('ERROR:', t)
            sys.exit()

    def typeChecking(self, V):
        if self.shape[0] == 1 and V.shape[0] == 1 and self.shape[1] == V.shape[1]:
            return 1
        if self.shape[1] == 1 and V.shape[1] == 1 and self.shape[0] == V.shape[0]:
            return 2
        return 0
    


    def __iterateVector(self, v_b):
        i = 0
        while i < self.shape[0]:
            if self.typeChecking(v_b) == 1:
                yield self.values[0][i], v_b.values[0][i]
            elif self.typeChecking(v_b) == 2:
                yield self.values[i][0], v_b.values[i][0]
            elif not self.typeChecking(v_b):
                raise
            i += 1

    def dot(self, V):
        scalar = 0
        for v1, v2 in self.__iterateVector(V):
            scalar += v1 * v2
        return scalar
