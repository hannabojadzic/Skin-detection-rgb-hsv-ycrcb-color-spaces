import cv2
import numpy as np

#Open a simple image
img=cv2.imread("C:/Users/wetan/Desktop/POOS-dataset/1.jpg")

img_HSV = cv2.cvtColor(img,  cv2.COLOR_BGR2HSV)

HSV_mask = cv2.inRange(img_HSV, (0, 15, 0), (17,170,255)) 
HSV_mask = cv2.morphologyEx(HSV_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))


img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
 
YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))


global_mask=cv2.bitwise_and(YCrCb_mask,HSV_mask)
global_mask=cv2.medianBlur(global_mask,3)
global_mask = cv2.morphologyEx(global_mask, cv2.MORPH_OPEN, np.ones((4,4), np.uint8))



global_result=cv2.bitwise_not(global_mask)

img2=cv2.imread("C:/Users/wetan/Desktop/POOS-dataset/1.jpg")
for i in range(img2.shape[0]):
    for j in range(img2.shape[1]):
        if global_result[i,j] != 0:
            img2[i,j,0] = 0
            img2[i,j,1] = 0
            img2[i,j,2] = 0
cv2.imwrite("C:/Users/wetan/Desktop/POOS-dataset/4_global4.jpg",img2)
#show results
# cv2.imshow("1_HSV.jpg",HSV_result)
# cv2.imshow("2_YCbCr.jpg",YCrCb_result)
# cv2.imshow("3_global_result.jpg",global_result)
# cv2.imshow("Image.jpg",img)

cv2.imwrite("C:/Users/wetan/Desktop/POOS-dataset/3_global_result4.jpg",global_result)
#cv2.imwrite("C:/Users/wetan/Desktop/POOS-dataset/4_rgb.jpg",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()  