# import data from scikit-image library
from skimage import data
# from matplotlib import pyplot
import matplotlib.pyplot as plt
# import utli from scikit-image library
from skimage import util

image = data.camera()

# add noise
# newImage = util.random_noise(image, mode='pepper')
# newImage = util.random_noise(image, mode='salt')
newImage = util.random_noise(image, mode='s&p')

# display image
plt.imshow(image, cmap='gray')
plt.title('before')
plt.show()
plt.imshow(newImage, cmap='gray')
plt.title('after')
plt.show()
