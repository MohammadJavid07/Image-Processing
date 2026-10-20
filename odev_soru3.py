
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Open the original image.
img = Image.open(r"D:\Python Codes and Project\Image Processing\Image-Processing\img1.jpg").convert("RGB")

# Convert the image to a NumPy array.
rgb_array = np.array(img)

# Convert the original RGB image into grayscale.
# The weighted formula accounts for human visual sensitivity.
gray = np.array(img.convert("L"))

# Reduce intensity levels to 2^bits.
def reduce_levels(image_array, bits):
    # Calculate the number of available intensity levels.
    levels = 2 ** bits

    # Map pixel values from 0-255 into the available levels.
    quantized = np.floor(image_array.astype(np.float32) * levels / 256)

    # Rescale quantized values back to 0-255 for display.
    result = np.round(quantized * 255 / (levels - 1))

    # Ensure all values are valid 8-bit pixel intensities.
    return np.clip(result, 0, 255).astype(np.uint8)


# ---------------------------------------------------
# PART A: Display grayscale images at different bit depths.
# ---------------------------------------------------

bit_depths = [8, 7, 6, 5, 4, 3, 2, 1]

fig, axes = plt.subplots(2, 4, figsize=(14, 8))

for ax, bits in zip(axes.flat, bit_depths):
    # Apply the requested grayscale bit depth.
    reduced_gray = reduce_levels(gray, bits)

    # Display the grayscale image.
    ax.imshow(reduced_gray, cmap="gray", vmin=0, vmax=255)
    ax.set_title(f"{2**bits} Levels ({bits} bit)")
    ax.axis("off")

    # Save the processed grayscale image.
    Image.fromarray(reduced_gray).save(
        f"grayscale_{bits}_bit.png"
    )

plt.tight_layout()
plt.show()


# ---------------------------------------------------
# PART B: Apply the same bit-depth reduction to RGB.
# ---------------------------------------------------

fig, axes = plt.subplots(2, 4, figsize=(14, 8))

for ax, bits in zip(axes.flat, bit_depths):
    # Quantize each color channel independently.
    reduced_rgb = reduce_levels(rgb_array, bits)

    # Display the resulting color image.
    ax.imshow(reduced_rgb)
    ax.set_title(f"RGB: {2**bits} Levels/Channel ({bits} bit)")
    ax.axis("off")

    # Save the processed color image.
    Image.fromarray(reduced_rgb).save(f"rgb_{bits}_bit.png")

plt.tight_layout()
plt.show()
