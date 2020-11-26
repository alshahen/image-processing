# import data from scikit-image library
from skimage import data
# import filters from scikit-image library
from skimage import filters
# from matplotlib import pyplot
import matplotlib.pyplot as plt

import numpy as np


# image = np.array([
#     [153 ,157 ,156 ,153 ,155],
#     [159 ,156 ,158 ,156 ,159],
#     [155 ,158 ,154 ,156 ,160],
#     [154 ,157 ,158 ,160 ,160],
#     [157 ,157 ,157 ,156 ,155]
#     ]).astype(np.float)

image = data.camera().astype(np.float)


laplace = filters.laplace(image)
laplace = filters.laplace(laplace)

sharp = image + laplace


sharp = np.clip(sharp, 0,255)


# display image
plt.imshow(image, cmap='gray')
plt.title('original')
plt.axis('off')
plt.show()
plt.imshow(sharp, cmap='gray')
plt.title('laplace second derivative')
plt.axis('off')
plt.show()




