import numpy as np
import matplotlib.pyplot as plt
from skimage import io

class ImageProcessor:
    def __init__(self):
        self.fileAsNumpyArr = None

    def load(self, path):
        try:
            self.fileAsNumpyArr = io.imread(path)
            print(f'loading image of size {self.fileAsNumpyArr.shape[0]}x{self.fileAsNumpyArr.shape[1]}')
            return self.fileAsNumpyArr
        except OSError as err:
            print("Error occurred:", err)
            if hasattr(err, 'filename'):
                print("Filename:", err.filename)
    
    def display(self, img):
        if isinstance(img, np.ndarray):
            plt.imshow(img)
            plt.show()
            return True
        else:
            print('ERRRO: arg must be of type nd.array')
            return False

if __name__ == '__main__':
    imgp = ImageProcessor()
    testimg = imgp.load('./42AI.png')
    # print(testimg)
    imgp.display(testimg)
