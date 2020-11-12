# import io from scikit-image library
from skimage import io
# from matplotlib import pyplot
import matplotlib.pyplot as plt

# read image
img = io.imread(fname='imagename.jpg')
# pass image to pyplot to show it later
plt.imshow(img)
# put title for image
plt.title('image title here')
# show image
plt.show()

# you can display more than one image by repeat the code blocks before and change any attributes you want

# pass image to pyplot to show it later
plt.imshow(img)
# put title for image
plt.title('image2 title here')
# show image
plt.show()


