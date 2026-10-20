
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the original color image and convert it to RGB.
img = Image.open(r"D:\Python Codes and Project\Image Processing\Image-Processing\img1.jpg").convert("RGB")

# Convert the image into a NumPy array.
# The shape is (height, width, 3), representing R, G, and B.
img_array = np.array(img)

# Extract the individual color bands.
red = img_array[:, :, 0]
green = img_array[:, :, 1]
blue = img_array[:, :, 2]

# Repeat each band's values across all three channels.
# This produces grayscale RGB images: (R,R,R), (G,G,G), (B,B,B).
red_gray = np.stack((red, red, red), axis=2)
green_gray = np.stack((green, green, green), axis=2)
blue_gray = np.stack((blue, blue, blue), axis=2)

# Display the original image and the three grayscale bands.
fig, axes = plt.subplots(1, 4, figsize=(16, 5))

axes[0].imshow(img_array)
axes[0].set_title("Original Image")

axes[1].imshow(red_gray)
axes[1].set_title("Red Band - Grayscale")

axes[2].imshow(green_gray)
axes[2].set_title("Green Band - Grayscale")

axes[3].imshow(blue_gray)
axes[3].set_title("Blue Band - Grayscale")

# Hide the coordinate axes for a cleaner display.
for ax in axes:
    ax.axis("off")

plt.tight_layout()
plt.show()

# Save the three resulting images.
Image.fromarray(red_gray.astype(np.uint8)).save("red_band_grayscale.png")
Image.fromarray(green_gray.astype(np.uint8)).save("green_band_grayscale.png")
Image.fromarray(blue_gray.astype(np.uint8)).save("blue_band_grayscale.png")
