import numpy as np
import math
import cv2
import imageio
from matplotlib import pyplot as plt

def equalizes(img,hist,cdf):

    row = np.size(img,0)
    col = np.size(img,1)
    newImg= np.zeros((row,col),np.uint8)
    for x in range(0,255):
        H= (cdf[x]-cdf[np.min(img)])/(cdf[254]-cdf1[np.min(img)])
        H=round(H*255)
        newImg[img==x]=H
           
       
    return newImg
"""
--------------------------------------------------------------------------------------------
"""
img1 = cv2.imread('1.tiff',0)
img2 = cv2.imread('2.png',0)
gif  = imageio.mimread('3.gif')
img3 = cv2.cvtColor(gif[0],cv2.COLOR_BGR2GRAY)
img4 = cv2.imread('4.jpg',0)
img5 = cv2.imread('5.bmp',0)
"""
showing image 
"""
plt.subplot(151),plt.imshow(img1,cmap="gray"),plt.axis("off"),plt.title("format:TIFF")
plt.subplot(152),plt.imshow(img2,cmap="gray"),plt.axis("off"),plt.title("format:PNG")
plt.subplot(153),plt.imshow(img3,cmap="gray"),plt.axis("off"),plt.title("format:GIF")
plt.subplot(154),plt.imshow(img4,cmap="gray"),plt.axis("off"),plt.title("format:JPG")
plt.subplot(155),plt.imshow(img4,cmap="gray"),plt.axis("off"),plt.title("format:BMP")
plt.show()



hist1 = cv2.calcHist([img1],[0],None,[256],[0,255])
hist2 = cv2.calcHist([img2],[0],None,[256],[0,255])
hist3 = cv2.calcHist([img3],[0],None,[256],[0,255])
hist4 = cv2.calcHist([img4],[0],None,[256],[0,255])
hist5 = cv2.calcHist([img5],[0],None,[256],[0,255])
 
    
hist1.astype(int)

plt.subplot(511),plt.bar(hist1),plt.title("format:TIFF")
plt.subplot(512),plt.plot(hist2),plt.title("format:PNG")
plt.subplot(513),plt.plot(hist3),plt.title("format:GIF")
plt.subplot(514),plt.plot(hist4),plt.title("format:JPG")
plt.subplot(515),plt.plot(hist5),plt.title("format:BMP")
plt.show()

cdf1 = np.cumsum(hist1)
cdf2 = np.cumsum(hist2)
cdf3 = np.cumsum(hist3)
cdf4 = np.cumsum(hist4)
cdf5 = np.cumsum(hist5)
plt.subplot(511),plt.plot(cdf1),plt.title("format:TIFF")
plt.subplot(512),plt.plot(cdf2),plt.title("format:PNG")
plt.subplot(513),plt.plot(cdf3),plt.title("format:GIF")
plt.subplot(514),plt.plot(cdf4),plt.title("format:JPG")
plt.subplot(515),plt.plot(cdf5),plt.title("format:BMP")
plt.show()



img1=equalizes(img1,hist1,cdf1)
img2=equalizes(img2,hist2,cdf2)
img3=equalizes(img3,hist3,cdf3)
img4=equalizes(img4,hist4,cdf4)
img5=equalizes(img5,hist5,cdf5)
plt.subplot(151),plt.imshow(img1,cmap="gray"),plt.axis("off"),plt.title("format:TIFF")
plt.subplot(152),plt.imshow(img2,cmap="gray"),plt.axis("off"),plt.title("format:PNG")
plt.subplot(153),plt.imshow(img3,cmap="gray"),plt.axis("off"),plt.title("format:GIF")
plt.subplot(154),plt.imshow(img4,cmap="gray"),plt.axis("off"),plt.title("format:JPG")
plt.subplot(155),plt.imshow(img4,cmap="gray"),plt.axis("off"),plt.title("format:BMP")
plt.show()
hist1 = cv2.calcHist([img1],[0],None,[255],[0,255])
hist2 = cv2.calcHist([img2],[0],None,[255],[0,255])
hist3 = cv2.calcHist([img3],[0],None,[255],[0,255])
hist4 = cv2.calcHist([img4],[0],None,[255],[0,255])
hist5 = cv2.calcHist([img5],[0],None,[255],[0,255])

plt.subplot(511),plt.plot(hist1),plt.title("format:TIFF")
plt.subplot(512),plt.plot(hist2),plt.title("format:PNG")
plt.subplot(513),plt.plot(hist3),plt.title("format:GIF")
plt.subplot(514),plt.plot(hist4),plt.title("format:JPG")
plt.subplot(515),plt.plot(hist5),plt.title("format:BMP")
plt.show()
cdf1 = np.cumsum(hist1)
cdf2 = np.cumsum(hist2)
cdf3 = np.cumsum(hist3)
cdf4 = np.cumsum(hist4)
cdf5 = np.cumsum(hist5)
plt.subplot(511),plt.plot(cdf1),plt.title("format:TIFF")
plt.subplot(512),plt.plot(cdf2),plt.title("format:PNG")
plt.subplot(513),plt.plot(cdf3),plt.title("format:GIF")
plt.subplot(514),plt.plot(cdf4),plt.title("format:JPG")
plt.subplot(515),plt.plot(cdf5),plt.title("format:BMP")
plt.show()






