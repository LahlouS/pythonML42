import numpy as np

class ColorFilter:
    def __init__(self):
        pass
    
    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """        
        if isinstance(array, np.ndarray):
            ret = array.copy()
            ret[::, ::, 0:3] = 255 - ret[::, ::, 0:3]
            return (ret)
        return None


    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            ret = array.copy()
            ret[::, ::, (0, 1)] = 0
            return (ret)
        return None

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            ret = array.copy()
            ret[::, ::, (0, 2)] = 0
            return (ret)
        return None

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            ret = array.copy()
            ret[::, ::, (1, 2)] = 0
            return (ret)
        return None
    
    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            ret = array.copy()
            ret[ret <= 65] = 0
            ret[(ret > 65) & (ret <= 100)] = 25
            ret[(ret > 100) & (ret <= 190)] = 200
            ret[ret > 190] = 255
            return (ret)
        return None
    

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if isinstance(array, np.ndarray):
            ret = array.copy()
            ret = np.reshape(array, (array.shape[0] * array.shape[1], array.shape[2]))
            if filter[0] == 'w' and len(kwargs['weights']) == 3:
                ret = ret[::, 0:3] * kwargs['weights']
            ret2 = np.sum(ret[::, 0:3], axis=1) / 3
            ret2 = np.reshape(ret2, (ret2.shape[0], 1))
            ret3 = np.reshape(np.broadcast_to(ret2, (ret2.shape[0], 3)), (array.shape[0], array.shape[1], 3)).astype(int)
            return (ret3)
        return None
