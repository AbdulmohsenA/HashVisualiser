from PIL import Image
import math
import numpy as np


def pseudoRandom(seed):
    # Under this line, put any complex mathmatical operations to the seed (an int) to make it as randomized as possible
    #######

    # Examples:
    # n = np.sin(seed)                  # Bad, you can easily see patterns
    # n = np.sin(seed * np.cos(seed))   # Good, no patterns can be easily detected.

    # This should be a white screen indicating all output to be 1, the famous Trigonometry identity.
    # n = np.sin(seed)**2 + np.cos(seed)**2

    # Change this.
    n = seed

    #######
    return n



# Random Pattern Visualiser
width = 500
height = width

pixels = np.arange(1, width*height + 1, dtype=np.int64)
pixels = pseudoRandom(pixels)

# Processing
pixels = pixels - np.min(pixels)                    # To start from 0 -> infinity
pixelScaled = pixels / pixels.max()                 # Scale down to be from 0 - 1
pixels = np.round(pixelScaled * 255)                # Default, Allow grayscale.
#pixelsBW = np.round(pixelScaled) * 255             # Alt, Either be white or black, No greyscaling.
pixels = pixels.reshape((width, height))            # Reshape to see as a square image

pixels = pixels                                     # pixelsGS = Grayscaled, pixelsBW = Black and White

img = Image.fromarray(pixels)
img.show()