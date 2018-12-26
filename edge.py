import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('7.jpg',0) 
#laplacian
img_laplacian = cv2.Laplacian(img,cv2.CV_64F)
#sobel
img_sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
img_sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
#canny
img_canny = cv2.Canny(img,100,200)
#prewitt
kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img,-1, kernely)
plt.figure
plt.subplot(3,2,1),plt.imshow(img_laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,2),plt.imshow(img_sobelx,cmap = 'gray')
plt.title('Sobelx'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,3),plt.imshow(img_sobely,cmap = 'gray')
plt.title('Sobely'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,4),plt.imshow(img_canny,cmap = 'gray')
plt.title('Canny'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,5),plt.imshow(img_prewittx,cmap = 'gray')
plt.title('Prewittx'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,6),plt.imshow(img_prewitty,cmap = 'gray')
plt.title('Prewitty'), plt.xticks([]), plt.yticks([])
plt.show()
plt.figure
plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.show()
