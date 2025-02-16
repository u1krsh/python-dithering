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

### Example of Floyd-Steinberg Dithering Effect
**Original Image:**  
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

## Bill Atkinson Dithering Algorithm
Another widely used dithering algorithm is **Bill Atkinson's dithering**, which is known for distributing errors more locally compared to Floyd-Steinberg. This method uses a simpler and more uniform error distribution pattern, making it ideal for images displayed on early Macintosh computers.

### Bill Atkinson Error Distribution Matrix:
```
      X   1/8   1/8
  1/8   1/8   1/8
      1/8
```
### Example of Bill Atkinson Dithering Effect
**Original Image:**  
![image](https://github.com/user-attachments/assets/605957ca-1d22-4d14-8148-d05e70cfa381)

**Dithered Image:**  
![image](https://github.com/user-attachments/assets/03be84a7-b79e-48e8-97f0-965a03f5d3b5)

## Why Use Floyd-Steinberg or Bill Atkinson Dithering?
- **Floyd-Steinberg**: Creates a smoother dithering effect by distributing error further, producing high-quality images with better gradient preservation.
- **Bill Atkinson**: Distributes error more locally, which can result in a more compact, less grainy appearance.

## Example Application Areas
- **Image Compression**: Reducing file sizes while maintaining quality.
- **Monochrome Displays**: Converting full-color images to black-and-white while preserving detail.
- **Artistic Effects**: Creating stylized, pixelated images with enhanced contrast.

## Support for Color Images
The Floyd-Steinberg dithering algorithm can also be applied to **color images** by processing each color channel (Red, Green, Blue) separately. This ensures that color variations and gradients are preserved while reducing the color depth. The process follows these steps:
1. **Convert Image to RGB Format**: Ensure the image is processed in its red, green, and blue channels.
2. **Apply Floyd-Steinberg Dithering to Each Channel**: Perform error diffusion on the red, green, and blue channels independently.
3. **Combine the Processed Channels**: Merge the dithered red, green, and blue channels back to form the final color-dithered image.

### Example of Dithering on Color Images
![image](https://github.com/user-attachments/assets/bfb64355-3f27-4755-b8f6-6ea2feb110cf)

### Zoomed In Colored Images
![image](https://github.com/user-attachments/assets/16f4554e-8278-4145-ba6e-1f74aa1bdb02)

## References
For a more detailed explanation, refer to the original papers:  
- [Floyd-Steinberg Dithering Algorithm](https://research.cs.wisc.edu/graphics/Courses/559-s2004/docs/floyd-steinberg.pdf)  
- [Bill Atkinson Dithering Algorithm](https://research.cs.wisc.edu/graphics/Courses/559-s2004/docs/floyd-steinberg.pdf)

## Contributions
Pull requests are welcome! If you find a bug or have a feature request, feel free to open an issue.

