import numpy as np


class ScrapBooker:
    def __init__(self):
        pass
    

    def crop(self, array, dim, position=(0,0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        start_y, start_x = position[0], position[1]

        stop_y, stop_x = dim[0], dim[1]
        if isinstance(array, np.ndarray):
            return array[start_y:start_y + stop_y, start_x:start_x + stop_x]
        return None

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if axis:
            return array[np.array([x for x in range(array.shape[0]) if (x + 1) % n == 0]), ::]
        else:
            return array[::, np.array([x for x in range(array.shape[1]) if (x + 1) % n != 0])]
        return None
        

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            # print([array for i in range(n)])
            return np.concatenate([array for i in range(n)], axis=axis)
    
    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            arr1 = np.concatenate([array for i in range(dim[0])], axis=0)
            return np.concatenate([arr1 for i in range(dim[1])], axis=1)
