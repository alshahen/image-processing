# import io from scikit-image library
from skimage import io
# import color from scikit-image library
from skimage import color
# from matplotlib import pyplot
import matplotlib.pyplot as plt

# read image
img = io.imread(fname='imagename.jpg')

# convert RGB image to gray level
gimg = color.rgb2gray(img)


# display image
# pass image to pyplot to show it later
plt.imshow(gimg, cmap='gray')
# put title for image
plt.title('gray')
# show image
plt.show()

# display histogram
plt.hist(gimg.ravel())
# put title for image
plt.title('histogram')
# show image
plt.show()