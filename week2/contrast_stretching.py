# import io from scikit-image library
from skimage import io
# from matplotlib import pyplot
import matplotlib.pyplot as plt
# import exposure from scikit-image library as exp
from skimage import exposure as exp


# read image
img = io.imread(fname= 'image.jpg' )

# Contrast shrinking
# in_range(ix,iy)
# ix : any pixel less than ix 
# iy : any pixel larger than iy 
# out_range(ox,oy)
# ox : any pixel < ix = ox
# oy : any pixel > iy = oy
img_rescale = exp.rescale_intensity(img, in_range=(90, 180), out_range=(0, 255))

# pass image to pyplot to show it later
plt.imshow(img, cmap='gray')
# put title for image
plt.title('before')
# show image
plt.show()

# pass image to pyplot to show it later
plt.hist(img.ravel())
# put title for image
plt.title('hist before')
# show image
plt.show()

# pass image to pyplot to show it later
plt.imshow(img_rescale, cmap='gray')
# put title for image
plt.title('after')
# show image
plt.show()


# pass image to pyplot to show it later
plt.hist(img_rescale.ravel())
# put title for image
plt.title('hist after')
# show image
plt.show()