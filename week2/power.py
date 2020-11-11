# import io from scikit-image library
from skimage import io
# import color from scikit-image library
from skimage import color
# import utli from scikit-image library
from skimage import util
# from matplotlib import pyplot
import matplotlib.pyplot as plt
# import numpy library as np
import numpy as np

from skimage import exposure as exp

# Read an image 
img = io.imread('sample.jpg') 

# convert image to gray level
r = color.rgb2gray(img)
# convert data type of image to 8-bit
r = util.img_as_ubyte(r)
   
# apply gamma method s = cr^y
c = 1
y = 1.5
s = exp.adjust_gamma(r, y, c)
# convert data type of image to 8-bit
s = s.astype(np.uint8)


# display image
plt.imshow(s, cmap='gray')
plt.show()
ax = plt.hist(s.ravel())
plt.show()