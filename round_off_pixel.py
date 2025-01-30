import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import numba

# Open the image form working directory
path = "picture.jpg"
image = Image.open(path)
data = np.array(image).astype(np.float32) / 255.
if len(data.shape)==2:
    data = data[:,:,np.newaxis]
    
data_rounded = np.round(data)
plt.imshow(data_rounded[:,:,0], cmap='Greys_r')
plt.show()
