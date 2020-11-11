# import io from scikit-image library
from skimage import io
# import color from scikit-image library
from skimage import color
# import util to convert image to 8-bit (img_as_ubyte) from scikit-image library
from skimage import util

# read image
img = io.imread(fname= 'image.jpg')

# convert RGB to Gray Level
gray_image = color.rgb2gray(img)

# convert image to 8-bit (byte)
r = util.img_as_ubyte(gray_image)

# s = L-1-r
# apply linear rule s = 255 - r 
s = 255 - r

# display s image
io.imshow(s)