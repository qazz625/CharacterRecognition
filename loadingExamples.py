import numpy as np
import tensorflow as tf
from tensorflow import keras
import os
from random import shuffle
import cv2
import copy

model = keras.models.load_model('my_model')


alphabets = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

pictures = os.listdir('DatasetExamples')

# shuffle(pictures)

# for i in range(10):
# 	print(pictures[i])

input_vectors = []
targets = []
print(pictures[0])
print(len(pictures))
going = 0
for im in pictures:
    # print(im)
    if going % 10**3 == 0:
    	print(going)

    image = cv2.imread('DatasetExamples/'+im, 0)
    tar = [0]*62
    newimage = copy.deepcopy(image)
    # print(image)
    # print(len(image[0]))
    # print(len(image))

    #change orientation to match train set
    for i in range(len(image)):
        for j in range(len(image[0])):
            newimage[i][j] = image[j][i]

    # reshaping to 1x784
    temp = []
    for i in range(len(newimage)):
        for j in range(len(newimage[0])):
            #normalizing
            if newimage[i][j] == 255:
                temp += [0]
            else:
                temp += [1]

    input_vectors += [temp[:]]

    # number = int(im.split('-')[0][3:])
    # tar[number-1] = 1
    # targets += [tar[:]]
    # going += 1


predicted = model.predict(input_vectors)

for i in range(len(pictures)):
	# print(input_vectors[i])
	p = np.argmax(predicted[i])
	# t = targets[i].index(1)
	# print(np.argmax(predicted[i]), targets[i].index(1))
	# print(alphabets[p], alphabets[t])
	print(alphabets[p], pictures[i])




