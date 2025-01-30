import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import numba

#open the image 
path = "picture.jpg"
image = Image.open(path)

#convert to float32 and normalize the image 0-1
data = np.array(image).astype(np.float32) / 255.
if len(data.shape)==2:
    data = data[:,:,np.newaxis]

#round the pixel values
data_rounded = np.round(data)
plt.imshow(data_rounded[:,:,0], cmap='Greys_r')
#plt.show()

#implementing Floyd Steinberg dithering
@numba.jit("f4[:,:,:](f4[:,:,:])", nopython=True, nogil=True)
def floyd_steinberg(image):
    Lx, Ly, Lc = image.shape # image size for x,y,z
    for j in range(Ly):
        for i in range(Lx):
            for c in range(Lc):
                rounded = round(image[i,j,c]) # roundind pixels
                err = image[i,j,c] - rounded
                image[i,j,c] = rounded
                if i<Lx-1: image[i+1,j,c] += (7/16)*err 
                if j<Ly-1:
                    image[i,j+1,c] += (5/16)*err
                    if i>0: image[i-1,j+1,c] += (1/16)*err
                    if i<Lx-1: image[i+1,j+1,c] += (3/16)*err           
    return image 

#apply Floyd Steinberg dithering to the image 
data_fs = floyd_steinberg(data.copy())
plt.imshow(data_fs[:,:,0], cmap='Greys_r')
plt.show()