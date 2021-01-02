import cv2
import numpy as np

# px
resolution = (2560, 1440)

# mm
screenSize = (286, 175)

# mm/px
scale = resolution[0]/screenSize[0]

# Output Image Settings
dim = (500, 500, 1)
img = np.ones(dim, np.uint8)

# Checkerboard Settings
# boardSize = 25
gridSize = (5,5)
squareSize = dim[0]/gridSize[0]

def tiling(n, m):
    result = np.zeros((n, m))
    result[::2, 1::2] = 1
    result[1::2, ::2] = 1
    return result


n = 9
m = 16
x = 50

img = tiling(n, m)
imgResize = cv2.resize(img, (m*x, n*x), interpolation=cv2.INTER_NEAREST)

while True:

    # Roll
    imgResize = np.roll(imgResize, 1)
    cv2.imshow("Raw", img)
    cv2.imshow("Frame", imgResize)
    cv2.waitKey(1)