import cv2
import numpy as np

img_bgr = cv2.imread('/home/cadbury/Documents/nema-life/test_images/TOZERO.png')
# img_bgr = cv2.imread('test.png')
# template = cv2.imread()
# w , h = template.shape[::-1]

w = 2
h = 2

threshold = 150

loc = np.where(img_bgr >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr , (pt[0],pt[1]) , (pt[0]+w , pt[1]+h) , (0,255,255) , 1)

cv2.imshow('detected' , img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()    

#-----------------NOT DESIRED -----------------------------------
# ---------------TRY PASSING TEMPLATE OR ANY OTHER WAY-----------