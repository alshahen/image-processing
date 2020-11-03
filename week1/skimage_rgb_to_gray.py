# import io from scikit-image library
from skimage import io
# import color from scikit-image library
from skimage import color
img = io.imread(fname= 'imagename.jpg' )
gimg = color.rgb2gray(img)
io.imshow(gimg)