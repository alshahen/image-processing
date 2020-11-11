# import io from scikit-image library
from skimage import io
# import color from scikit-image library
from skimage import color
# import utli from scikit-image library
from skimage import util
# from matplotlib import pyplot
import matplotlib.pyplot as plt



# Read an image 
img = io.imread('sample.jpg') 

# convert image to gray level
r = color.rgb2gray(img)
# convert data type of image to 8-bit
r = util.img_as_ubyte(r)
   
# apply thresholding method 
r[r >= 127] = 255
r[r < 127] = 0


# display image
plt.imshow(r, cmap='gray')
plt.show()
ax = plt.hist(r.ravel())
plt.show()