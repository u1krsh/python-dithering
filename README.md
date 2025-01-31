# Floyd-Steinberg Dithering Algorithm

This repository contains a detailed explanation of the **Floyd-Steinberg dithering algorithm**, a popular method used for reducing color depth while preserving image details through error diffusion.

## Features
- **Error Diffusion**: Distributes quantization errors to neighboring pixels.
- **Preserves Image Details**: Retains important features even with reduced color depth.
- **Supports Grayscale & RGB Images**.
- **Widely Used in Printing and Image Processing**.

## Algorithm Overview
The **Floyd-Steinberg dithering algorithm** applies error diffusion using the following weight distribution:
```
      X   7/16
  1/16   5/16   3/16
```

### Example of Dithering Effect
**Rounded Image:**  
![image](https://github.com/user-attachments/assets/605957ca-1d22-4d14-8148-d05e70cfa381)


**Dithered Image:**  
![image](https://github.com/user-attachments/assets/a558e3f1-a67e-45ea-876f-f9ea61ad6a68)


### Steps Involved
1. **Process Each Pixel**: The algorithm iterates through the image pixel by pixel, processing from left to right and top to bottom.
2. **Quantization**: The pixel value is rounded to the nearest integer (or thresholded in binary mode).
3. **Calculate Error**: The difference (error) between the original and quantized value is computed.
4. **Distribute Error**: This error is then spread to neighboring pixels using the Floyd-Steinberg diffusion matrix:
   - 7/16 of the error is added to the right neighbor.
   - 5/16 of the error is added to the pixel directly below.
   - 3/16 of the error is added to the bottom-right neighbor.
   - 1/16 of the error is added to the bottom-left neighbor.
5. **Repeat Until Completion**: This process continues for all pixels in the image, ensuring that errors are evenly distributed to maintain the visual fidelity of the image.

## Why Use Floyd-Steinberg Dithering?
- **Enhances Visual Quality**: Creates the illusion of smooth gradients using a limited number of colors.
- **Efficient for Low-Color Displays**: Helps display images effectively on monochrome or limited-color screens.
- **Common in Printing Applications**: Used for halftone printing where only black and white dots are available.

## Example Application Areas
- **Image Compression**: Reducing file sizes while maintaining quality.
- **Monochrome Displays**: Converting full-color images to black-and-white while preserving detail.
- **Artistic Effects**: Creating stylized, pixelated images with enhanced contrast.

## Reference
For a more detailed explanation, refer to the original paper: [Floyd-Steinberg Dithering Algorithm](https://research.cs.wisc.edu/graphics/Courses/559-s2004/docs/floyd-steinberg.pdf).

## Contributions
Pull requests are welcome! If you find a bug or have a feature request, feel free to open an issue.

