# import ndimage from scipy library
from scipy import ndimage
# import numpy library as np
import numpy as np

# create image
image = np.array([[110, 120, 90, 130],
              [91, 94, 98, 200],
              [90, 91, 99, 100],
              [82, 96, 85, 90]
              ])
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
