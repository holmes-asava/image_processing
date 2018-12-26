import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('5.jpg',0) 
kernel = np.ones((3,3),np.uint8)

#Erosion
erosion = cv2.erode(img,kernel,iterations = 1)
#Dilation
dilation = cv2.dilate(img,kernel,iterations = 1)
#Openingn
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#Closing
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)



plt.subplot(3,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,2),plt.imshow(erosion,cmap = 'gray')
plt.title('Erosion'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,3),plt.imshow(dilation,cmap = 'gray')
plt.title('Dilation'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,4),plt.imshow(opening,cmap = 'gray')
plt.title('Opening'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,5),plt.imshow(closing,cmap = 'gray')
plt.title('Closing'), plt.xticks([]), plt.yticks([])
plt.show()
