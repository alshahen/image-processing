# import io from scikit-image library
from skimage import io
img = io.imread(fname= 'imagename.jpg' )
# do some process here :)
# save the image
io.imsave(fname= 'C:\\Users\\username\\Pictures\\newimagename.jpg' , arr=img)