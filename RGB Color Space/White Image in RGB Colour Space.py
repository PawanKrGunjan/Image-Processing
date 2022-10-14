import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[[ 255 , 255 , 255 ] , [ 255 , 255 , 255 ] , [ 255 , 255 , 255 ]],
                [[ 255 , 255 , 255 ] , [ 255 , 255 , 255 ] , [ 255 , 255 , 255 ]],
                [[ 255 , 255 , 255 ] , [ 255 , 255 , 255 ] , [ 255 , 255 , 255 ]]])

L = []
for i in range(1020):
    l =[]
    for j in range(1280):
        temp = []
        for k in range(3):
            temp.append(255)
        l.append(temp)
    L.append(l)
    

arr = np.array(L)

plt.imshow(arr)
plt.show()

cv.imwrite('White.png',arr)