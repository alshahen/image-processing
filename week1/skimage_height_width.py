# import io from scikit-image library
from skimage import io
img = io.imread(fname= 'imagename.jpg')
# Height (y)
print(img.shape[0])
# Output: 600
# Width (x)
print(img.shape[1])
# Output: 800