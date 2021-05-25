import numpy as np
import cv2
import os
import copy

pictures = os.listdir('OnlineDrawing')
pictures.sort()

for im in pictures:
    image = cv2.imread('OnlineDrawing/'+im)

    #convert to grayscale
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #resize to 28x28
    image = cv2.resize(image, (28, 28))

    # thresholding
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] >= 215:
                image[i][j] = 255
            else:
                image[i][j] = 0

    cv2.imwrite('OnlineDrawing/'+im, image)
    