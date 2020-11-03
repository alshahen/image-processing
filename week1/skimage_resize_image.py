# import io from scikit-image library
from skimage import io
# import transform from scikit-image library as tf
import skimage.transform as tf
img = io.imread(fname= 'imagename.jpg' )
newimg = tf.resize(img, ( 400 , 200 ))
io.imshow(newimg)