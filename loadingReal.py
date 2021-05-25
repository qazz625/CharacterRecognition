import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
from random import shuffle
import cv2
import copy

model = keras.models.load_model('my_model')


alphabets = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

pictures = os.listdir('Real')

shuffle(pictures)

input_vectors = []
targets = []

going = 0
for im in pictures:
    image = cv2.imread('Real/'+im, 0)
    tar = [0]*62
    newimage = copy.deepcopy(image)

    #change orientation to match train set
    for i in range(len(image)):
        for j in range(len(image[0])):
            newimage[i][j] = image[j][i]

    # reshaping to 1x784
    temp = []
    for i in range(len(newimage)):
        for j in range(len(newimage[0])):
            #normalizing and thresholding
            if newimage[i][j] >= 215:
                temp += [0]
            else:
                temp += [1]

    input_vectors += [temp[:]]

predicted = model.predict(input_vectors)

for i in range(3):
	p = np.argmax(predicted[i])
    # print(predicted[i])
	print(alphabets[p], pictures[i]);





