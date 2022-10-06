import numpy as np
import matplotlib.pyplot as plt

img = np.ones((1280,1280), dtype = int)
zeros = np.zeros((160,160), dtype = int)

for i in range(1,9):
    for j in range(1,9):
        if ((i+j)%2)==0:
            img[(i-1)*160:i*160,(j-1)*160:j*160] = zeros

print(img)

plt.figure(figsize=(8,8), dpi=100)            
plt.imshow(img, cmap=plt.cm.binary) 
plt.show()