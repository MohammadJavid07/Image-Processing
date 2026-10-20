
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the original image and convert it to RGB.
img = Image.open(r"D:\Python Codes and Project\Image Processing\Image-Processing\img1.jpg").convert("RGB")

# Convert the image into a NumPy array.
img_array = np.array(img)

# Extract the original R, G, and B channels.
R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

# Create new images by rearranging the color channels.
# RGB: Original order.
rgb = np.stack((R, G, B), axis=2)

# GRB: Green takes the red position; red takes the green position.
grb = np.stack((G, R, B), axis=2)

# RBG: Exchange green and blue.
rbg = np.stack((R, B, G), axis=2)

# BRG: Blue first, red second, green third.
brg = np.stack((B, R, G), axis=2)

# GBR: Green first, blue second, red third.
gbr = np.stack((G, B, R), axis=2)

# BGR: Reverse the original channel order.
bgr = np.stack((B, G, R), axis=2)

# Display all six channel arrangements.
images = [rgb, grb, rbg, brg, gbr, bgr]
titles = ["RGB - Original", "GRB", "RBG", "BRG", "GBR", "BGR"]

fig, axes = plt.subplots(2, 3, figsize=(12, 8))

for ax, image, title in zip(axes.flat, images, titles):
    ax.imshow(image)
    ax.set_title(title)
    ax.axis("off")

plt.tight_layout()
plt.show()

# Save each artificial-color image.
for image, title in zip(images, titles):
    filename = title.split(" - ")[0].lower() + ".png"
    Image.fromarray(image.astype(np.uint8)).save(filename)
