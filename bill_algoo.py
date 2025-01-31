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

#implementing Atkinson dithering
@numba.jit("f4[:,:,:](f4[:,:,:])", nopython=True, nogil=True)
def billy(image):
    frac = 8
    Lx, Ly, Lc = image.shape
    for j in range(Ly): 
        for i in range(Lx):
            for c in range(Lc):
                rounded = round(image[i,j,c])
                err = image[i,j,c] - rounded
                image[i,j,c] = rounded
                if i<Lx-1: image[i+1,j,c] += err / frac 
                if i<Lx-2: image[i+2,j,c] += err /frac
                if j<Ly-1:
                    image[i,j+1,c] += err / frac
                    if i>0: image[i-1,j+1,c] += err / frac
                    if i<Lx-1: image[i+1,j+1,c] += err / frac
                if j<Ly-2: image[i,j+2,c] += err / frac      
    return image

#apply Floyd Steinberg dithering to the image 
data_bill = billy(data.copy())
plt.imshow(data_bill[:,:,0], cmap='Greys_r')
plt.show()