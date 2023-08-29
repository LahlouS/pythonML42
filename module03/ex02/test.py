from scrapBooker import ScrapBooker
import numpy as np
sb = ScrapBooker()

arr1 = np.arange(0,25).reshape(5,5)
print(arr1)
print('\nOutput:\n')
print(sb.crop(arr1, (3, 1), (1, 0)))
print('\n\n----------> thin')
arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
# print(arr2)
print(sb.thin(arr2,2,0))

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print('\n\njuxtapose function:\n', sb.juxtapose(arr3, 3, 1))
#Output :
# array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3, 1, 2, 3]])

print('\n\nmosaic function:\n', sb.mosaic(arr3, (3, 1)))
