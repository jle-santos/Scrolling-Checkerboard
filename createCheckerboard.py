import cv2
import numpy as np

class checkerboard():
    def __init__(self, monitor, resolution, checkerboardSize, boardSize, units="MM"):
        self.scaleX = monitor[0]/resolution[0]
        self.scaleY = monitor[1]/resolution[1]
        self.board = self.createBoard(checkerboardSize, boardSize, units)

    def createBoard(self, checkerboardSize, boardSize, units):
        if units == "MM":
            sizeWidth = int(boardSize[0]/self.scaleX)
            sizeHeight = int(boardSize[1]/self.scaleY)

            return np.ones((sizeHeight, sizeWidth, 1), np.uint8)

# Create board
monitorMM = (597, 300)
resolution = (1920, 1080)
boardMM = (156, 10)

board1 = checkerboard(monitorMM, resolution, 5, boardMM)

cv2.imshow("Board", board1.board)
cv2.waitKey(0)




