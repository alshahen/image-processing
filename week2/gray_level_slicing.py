# import io from scikit-image library
from skimage import io
# import color from scikit-image library
from skimage import color
# import util to convert image to 8-bit (img_as_ubyte) from scikit-image library
from skimage import util
# from matplotlib import pyplot
import matplotlib.pyplot as plt




# read image
img = io.imread(fname= 'image4.jpg' )

# convert RGB image to gray level
gimg = color.rgb2gray(img)

# convert data type of image to 8-bit
r = util.img_as_ubyte(gimg)

# take copy of r
s = r.copy()

# for loop every pixel if pixel >= 20 and <= 50 then pixel = 200
for x in range(0,s.shape[0]):
    for y in range(0,s.shape[1]):
        if s[x][y] >= 20 and s[x][y] <= 50:
            s[x][y] = 200

# pass image to pyplot to show it later
plt.imshow(r, cmap='gray')
# put title for image
plt.title('before')
# show image
plt.show()

# pass image to pyplot to show it later
plt.hist(r.ravel())
# put title for image
plt.title('hist before')
# show image
plt.show()

# pass image to pyplot to show it later
plt.imshow(s, cmap='gray')
# put title for image
plt.title('after')
# show image
plt.show()


# pass image to pyplot to show it later
plt.hist(s.ravel())
# put title for image
plt.title('hist after')
# show image
plt.show()