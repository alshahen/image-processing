# import data from scikit-image library
from skimage import data
# from matplotlib import pyplot
import matplotlib.pyplot as plt
# import filters from scikit-image library
from skimage import filters


image = data.camera()


newImage = filters.median(image, [[1,1,1], [1,1,1], [1,1,1]])

# display image
plt.imshow(image, cmap='gray')
plt.title('before')
plt.show()
plt.imshow(newImage, cmap='gray')
plt.title('after')
plt.show()
