import cv2
import numpy as np

#Open a simple image
img=cv2.imread("C:/Users/wetan/Desktop/POOS-dataset/1.jpg")

img_HSV = cv2.cvtColor(img,  cv2.COLOR_BGR2HSV)

HSV_mask = cv2.inRange(img_HSV, (0, 15, 0), (17,170,255)) 
HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))



HSV_result = cv2.bitwise_not(HSV_mask)


img2=cv2.imread("C:/Users/wetan/Desktop/POOS-dataset/1.jpg")
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        if HSV_result[i,j] != 0:
            img2[i,j,0] = 0
            img2[i,j,1] = 0
            img2[i,j,2] = 0
cv2.imwrite("C:/Users/wetan/Desktop/POOS-dataset/4_hsv4.jpg",img2)

cv2.imwrite("C:/Users/wetan/Desktop/POOS-dataset/1_HSV4.jpg",HSV_result)

#cv2.imwrite("C:/Users/wetan/Desktop/POOS-dataset/4_rgb.jpg",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()  