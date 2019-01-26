import cv2
import numpy as np

#Open a simple image
img=cv2.imread("C:/Users/wetan/Desktop/POOS-dataset/1.jpg")


img2=cv2.imread("C:/Users/wetan/Desktop/POOS-dataset/1.jpg")
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        if img2[i,j,2] > 94 and img2[i,j,1]>40 and img2[i,j,0] >20 and max(img2[i,j,2],img2[i,j,1],img2[i,j,0])- min(img2[i,j,2],img2[i,j,1],img2[i,j,0]) > 15 and abs(img2[i,j,2]-img2[i,j,1]) > 15 and img2[i,j,2]>img2[i,j,1] and img2[i,j,2]> img2[i,j,0]:
            #print('pixel')
            a = 1
        else:
            img2[i,j,0] = 0
            img2[i,j,1] = 0
            img2[i,j,2] = 0 
cv2.imwrite("C:/Users/wetan/Desktop/POOS-dataset/4_rgb4.jpg",img2)

img2=cv2.imread("C:/Users/wetan/Desktop/POOS-dataset/1.jpg")
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        if img2[i,j,2] > 94 and img2[i,j,1]>40 and img2[i,j,0] >20 and max(img2[i,j,2],img2[i,j,1],img2[i,j,0])- min(img2[i,j,2],img2[i,j,1],img2[i,j,0]) > 15 and abs(img2[i,j,2]-img2[i,j,1]) > 15 and img2[i,j,2]>img2[i,j,1] and img2[i,j,2]> img2[i,j,0]:
            #print('pixel')
            img2[i,j,0] = 0
            img2[i,j,1] = 0
            img2[i,j,2] = 0 
        else:
            img2[i,j,0] = 255
            img2[i,j,1] = 255
            img2[i,j,2] = 255
cv2.imwrite("C:/Users/wetan/Desktop/POOS-dataset/4_rgb_neg4.jpg",img2)

#cv2.imwrite("C:/Users/wetan/Desktop/POOS-dataset/4_rgb.jpg",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()  