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
img = io.imread('image.jpg') 

# convert image to gray level
r = color.rgb2gray(img)
# convert data type of image to 8-bit
r = util.img_as_ubyte(r)
   
# apply log transformation method s = c * log(1 + r)
c = 1
s = exp.adjust_log(r, c)
# convert data type of image to 8-bit
s = s.astype(np.uint16)


# display image
plt.imshow(r, cmap='gray')
plt.title('before')
plt.show()

ax = plt.hist(r.ravel())
plt.title('hist before')
plt.show()

plt.imshow(s, cmap='gray')
plt.title('after')
plt.show()

ax = plt.hist(s.ravel())
plt.title('hist after')
plt.show()