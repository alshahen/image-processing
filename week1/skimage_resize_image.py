# import io from scikit-image library
from skimage import io
# import transform from scikit-image library as tf
import skimage.transform as tf
# from matplotlib import pyplot
import matplotlib.pyplot as plt

# read image
img = io.imread(fname= 'imagename.jpg' )
# resize image (height , width)
newimg = tf.resize(img, ( 400 , 200 ))
# pass image to pyplot to show it later
plt.imshow(newimg, cmap='gray')
# put title for image
plt.title('resized image')
# show image
plt.show()
