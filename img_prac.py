"""Convert an image to grayscale and print its dimensions."""

from numpy import array
from PIL import Image

#to covert an image into grayscale black and white 
img = array(Image.open(r"D:\Python Codes and Project\Image Processing\Image-Processing\img1.jpg").convert("L"))
#to print the dimensions of img1
print(img.shape)
