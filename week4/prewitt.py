# import data from scikit-image library
from skimage import data
# import filters from scikit-image library
from skimage import filters
# from matplotlib import pyplot
import matplotlib.pyplot as plt


image = data.camera()

# apply prewitt filter on image
# edges = filters.prewitt_h(image)
# edges = filters.prewitt_v(image)
edges = filters.prewitt(image)


# display image
plt.imshow(image, cmap='gray')
plt.title('image')
plt.show()
plt.imshow(edges, cmap='gray')
plt.title('edges')
plt.show()






