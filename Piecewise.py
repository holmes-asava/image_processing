import numpy as np
import math
import cv2
import imageio
from matplotlib import pyplot as plt

img = cv2.imread('1.tiff',0)
hist,bins = np.histogram([img],bins=range(256))
cdf = np.cumsum(hist)
"""
generate reference fuction
"""
img_ref = cv2.imread('ref.png',0)
hist_ref,bins = np.histogram([img_ref],bins=range(256))
cdf_ref = np.cumsum(hist_ref)
plt.subplot(121),plt.plot(cdf),plt.axis("on"),plt.title("CDF")
plt.subplot(122),plt.plot(cdf_ref),plt.axis("on"),plt.title("Ref_CDF")
plt.show()
i=0
ref_point= np.zeros((6,1),np.double)
state= np.zeros((6,1),np.uint8)
for x in range(0,255,51):
    state[i]=x
    ref_point[i]=cdf_ref[x]*100/cdf_ref[254]
    i=i+1


state[5]=254
ref_point[5]=cdf_ref[254]*100/cdf_ref[254]
"""
-----------------------
"""
row = np.size(img,0)
col = np.size(img,1)
newImg= np.zeros((row,col),np.uint8)
i=0
for x in range(0,255):
    if(cdf[x]<state[0]):
        result=0
    elif(cdf[x]>cdf[254]):
        result=255
    else:
        
        if(x>=state[4]):
            i=4
        elif(x>=state[3]):
            i=3
        elif(x>=state[2]):
            i=2
        elif(x>=state[1]):
            i=1
        elif(x<state[1]):
            i=0
       
        result= state[i]+((cdf[x]*100/cdf[254])-ref_point[i])*(state[i+1]-state[i])/(ref_point[i+1]-ref_point[i])
    newImg[img==x]=result

hist,bins = np.histogram([newImg],bins=range(256))
cdf = np.cumsum(hist)
plt.subplot(121),plt.plot(cdf*100/cdf[254]),plt.axis("on"),plt.title("New_CDF")
plt.subplot(122),plt.plot(state,ref_point),plt.axis("on"),plt.title("Ref_CDF")
plt.show()

plt.subplot(131),plt.imshow(img,cmap="gray"),plt.axis("off"),plt.title("Original pic")
plt.subplot(132),plt.imshow(newImg,cmap="gray"),plt.axis("off"),plt.title("New pic")
plt.subplot(133),plt.imshow(img_ref,cmap="gray"),plt.axis("off"),plt.title("Ref pic")

plt.show()
