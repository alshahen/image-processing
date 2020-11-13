# import data from scikit-image library
from skimage import data
# from matplotlib import pyplot
import matplotlib.pyplot as plt

img = data.camera();


# display image
plt.imshow(img, cmap='gray')
plt.title('before')
plt.show()
