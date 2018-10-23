import numpy as np
import math
import cv2

from matplotlib import pyplot as plt

def Conv(img,kernal):
        row = np.size(img,0)
        col = np.size(img,1)
        rowk = np.size(kernal,0)
        colk = np.size(kernal,1) 
        point = (colk-1)//2
        img=cv2.copyMakeBorder(img,point,point,point,point,cv2.BORDER_REPLICATE)
        img_conv =np.zeros((row,col),dtype="float32")
        
        
        for u in range(point,row+point):
            for v in range(point,col+point):
                section=img[u-point:u+point+1,v-point:v+point+1]
                k_sum = (section*kernal).sum();
                if(k_sum>255):
                        k_sum=255
                elif(k_sum<0):
                        k_sum=0
                img_conv[u-point,v-point]=k_sum
        
        img_conv=img_conv.astype("uint8")
        return  img_conv 

img = cv2.imread('logo.jpg',0)
Box_kernal=np.array([[1,1,1],[1,1,1],[1,1,1]],dtype="float32")
Box_kernal=Box_kernal/9
Gussian_kernal=np.array([[0,1,2,1,0],[1,3,5,3,1],[2,5,9,5,2],[1,3,5,3,1],[0,1,2,1,0]],dtype="float32")
Gussian_kernal=Gussian_kernal/57
Difference_kernal=np.array([[0,0,-1,0,0],[0,-1,-2,-1,0],[-1,-2,16,-2,-1],[0,-1,-2,-1,0],[0,0,-1,0,0]],dtype="float32")
BoxImg=Conv(img,Box_kernal)
GImg=Conv(img,Gussian_kernal)
DImg=Conv(img,Difference_kernal)
plt.subplot(221),plt.imshow(img,cmap="gray"),plt.axis("off"),plt.title("before")
plt.subplot(222),plt.imshow(BoxImg,cmap="gray"),plt.axis("off"),plt.title("Box filters")
plt.subplot(223),plt.imshow(GImg,cmap="gray"),plt.axis("off"),plt.title("Gussian filters")
plt.subplot(224),plt.imshow(DImg,cmap="gray"),plt.axis("off"),plt.title("Difference filters")
plt.show()

"""
kernal=kernal.astype("int8")
print(kernal)
"""
