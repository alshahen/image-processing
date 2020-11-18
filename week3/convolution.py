# import ndimage from scipy library
from scipy import ndimage
# import numpy library as np
import numpy as np

# create image
image = np.array([[2, 2, 2, 3],
              [2, 1, 3, 3],
              [2, 2, 1, 2],
              [1, 3, 2, 2]
              ])
# create filter
# note : filter will rotate 180 degre when executed (correlation)
kernel = np.array([
    [1, 1, 1],
    [-1, 2, 1],
    [-1, -1, 1]
    ])

# apply convolution on image
newImage = ndimage.convolve(image, kernel, mode='constant')
