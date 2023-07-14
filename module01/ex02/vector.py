import sys

    # (1, n) = [[0,1,2,3,4, . . .]]
    # (n, 1) = [[1], [2], [3], . . .]

class Vector:
    def __init__(self, arg):
        try:
            self.values = []
            if isinstance(arg, list):
                if len(arg) == 1 and isinstance(arg[0], list):
                    self.values.append([float(val) for val in arg[0]])
                    self.shape = (1, len(arg[0])) # (1, n) is row vector aka TYPE 2 (see __typeChecking() method)
                elif len(arg) != 0:
                    for val in arg:
                        if not isinstance(val, list) or len(val) != 1:
                            raise TypeError('Column vectors values must be lists of single float')
                        else:
                            self.values.append([float(val[0])])
                    self.values = arg
                    self.shape = (len(arg), 1) # (n, 1) is columns vector aka TYPE 1 (see __typeChecking() method)
            elif isinstance(arg, int):
                self.values = [[float(x)] for x in range(arg)]
                self.shape = (len(self.values), 1) # (n, 1) is columns vector aka TYPE 1 (see __typeChecking() method)
            elif isinstance(arg, tuple) and len(arg) == 2:
                if arg[0] < arg[1]:
                    self.values = [[float(x)] for x in range(arg[0], arg[1])]
                    self.shape = (len(self.values), 1) # (n, 1) is columns vector aka TYPE 1 (see __typeChecking() method)
                else:
                    raise TypeError('unvalid range')
            else:
                raise TypeError('Vector instanciation is based on a list, an int or a range (tuple)')
        except (ValueError, TypeError) as t:
            print('ERROR:', t)
            sys.exit()

    def __typeChecking(self, V):
        if not isinstance(V, Vector):
            raise TypeError('arg is not of type Vector')
        if self.shape == V.shape:
            if self.shape[0] == 1:
                return 2
            return 1
        return 0
    
    def __atIndex(self, i):
        if self.__typeChecking(self) == 2:
            return self.values[0][i]
        else:
            return self.values[i][0]

    def __iterateVector(self, v_b, vecType):
        i = 0
        while i < self.shape[vecType - 1]: # type 2, size is at index 1 type 1, size is at index 0
            yield self.__atIndex(i), v_b.__atIndex(i)
            i += 1

    def dot(self, V):
        scalar = 0
        try:
            vectorType = self.__typeChecking(V)
            if vectorType:
                for v1, v2 in self.__iterateVector(V, vectorType):
                    scalar += v1 * v2
                return scalar
            else:
                raise ValueError('Vectors types are not compatible !')
        except (TypeError, ValueError) as v:
            print('ERROR', v)

    # (1, n) == [[0,1,2,3,4, . . .]] == type 2
    # (n, 1) == [[1], [2], [3], . . .] == type 1

    def T(self):
        if self.__typeChecking(self) == 2:
            return Vector([[val] for val in self.values[0]])
        else:
            return Vector([[val[0] for val in self.values]])
   
   
    # the dunders
    def __add__(self, y):
        try:
            vectorType = self.__typeChecking(y)
            if vectorType == 1:
                return Vector( [[val1 + val2] for val1, val2, in self.__iterateVector(y, vectorType)])
            elif vectorType == 2:
                return Vector([[val1 + val2 for val1, val2, in self.__iterateVector(y, vectorType)]])
            else: 
                raise ValueError('Vectors types are not compatible !')
        except (TypeError, ValueError) as t:
            print('ERROR:', t)
    
    def __radd__(self, y):
        if not isinstance(y, Vector):
            raise NotImplementedError
        else:
            self.__add__(y)

    def __sub__(self, y):
        try:
            vectorType = self.__typeChecking(y)
            if vectorType == 1:
                return Vector( [[val1 - val2] for val1, val2, in self.__iterateVector(y, vectorType)])
            elif vectorType == 2:
                return Vector([[val1 - val2 for val1, val2, in self.__iterateVector(y, vectorType)]])
            else: 
                raise ValueError('Vectors types are not compatible !')
        except (TypeError, ValueError) as t:
            print('ERROR:', t)

    def __rsub__(self, y):
        if not isinstance(y, Vector):
            raise NotImplementedError
        else:
            self.__sub__(y)

    def __truediv__(self, y):
        try:
            yOk = float(y)
            vectorType = self.__typeChecking(self)
            if vectorType == 1:
                return Vector( [ [val1[0] / yOk] for val1 in self.values ])
            elif vectorType == 2:
                return Vector([ [val1 / yOk for val1 in self.values[0]] ])
            else: 
                raise ValueError('Vectors types are not compatible !')
        except (TypeError, ValueError, ZeroDivisionError) as t:
            print('ERROR:', t)

    def __rtruediv__(self, y):
        raise NotImplementedError('NotImplementedError: Division of a scalar by a Vector is not defined here.')

    def __mul__(self, y):
        try:
            yOk = float(y)
            vectorType = self.__typeChecking(self)
            if vectorType == 1:
                return Vector( [ [val1[0] * yOk] for val1 in self.values ])
            elif vectorType == 2:
                return Vector([ [val1 * yOk for val1 in self.values[0]] ])
            else: 
                raise ValueError('Vectors types are not compatible !')
        except (TypeError, ValueError) as t:
            print('ERROR:', t)

    def __rmul__(self, y):
        print('in __rmul__')
        try:
            return self.__mul__(float(y))
        except:
            raise NotImplementedError

    def __str__(self):
        return f'Vector({str(self.values)})'
    
    def __repr__(self):
        return f'Vector({str(self.values)})'
        

    