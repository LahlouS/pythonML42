from imageProcessor import ImageProcessor
from colorFilter import ColorFilter
import numpy as np

impro = ImageProcessor()
colFil = ColorFilter()
elonimg = impro.load('./elon.png')

# impro.display(elonimg)

# impro.display(colFil.invert(elonimg))
# 
# impro.display(colFil.to_blue(elonimg))
# 
# impro.display(colFil.to_green(elonimg))
# 
# impro.display(colFil.to_red(elonimg))

# impro.display(colFil.to_celluloid(elonimg))

impro.display(colFil.to_grayscale(elonimg, 'w', weights = [7, 1, 1]))


