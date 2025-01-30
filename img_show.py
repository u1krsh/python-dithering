from PIL import Image
import matplotlib.pyplot as plt

# Open an image file using PIL
image = Image.open("picture.jpg")

# Display the image using Matplotlib
plt.imshow(image)
plt.axis('off')  # Hide the axes
plt.show()