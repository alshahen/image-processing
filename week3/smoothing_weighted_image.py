# import data from scikit-image library
from skimage import data
# import ndimage from scipy library
from scipy import ndimage
# import numpy library as np
import numpy as np
# from matplotlib import pyplot
import matplotlib.pyplot as plt

image = data.camera()

# create filter
# note : filter will rotate 180 degree when executed (correlation)
kernel = np.array([
    [1, 2, 1],
    [2, 4, 2],
    [1, 2, 1]
    ])

kernel = kernel / np.sum(kernel)

# apply convolution on image
newImage = ndimage.convolve(image, kernel, mode='constant', output=np.uint8)

# display image
plt.imshow(image, cmap='gray')
plt.title('before')
plt.show()
plt.imshow(newImage, cmap='gray')
plt.title('after')
plt.show()
