##Simple image thresholding

import cv2
import numpy as np
from matplotlib import pyplot as plt

import sys
dir = "/home/cadbury/Documents/nema-life/conf_files/conf"
# print(dir)
sys.path.insert(0,dir)
import conf

output_dir = conf.output_dir
# print(output_dir)
output_image_counter = 0

thresh_val = conf.threshold_value

plt.rc("figure", dpi = 400)
img = cv2.imread('../test_images/mobile/image2.jpg',0)
# img = cv2.imread('../test_images/mobile/image1.jpeg',0)

ret,thresh1 = cv2.threshold(img,thresh_val,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,thresh_val,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,thresh_val,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,thresh_val,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,thresh_val,255,cv2.THRESH_TOZERO_INV)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

print(type(thresh1))

for i in range(6):
    
    output_image_counter += 1
    # new_file_name = str(output_dir) + "out_image_" + str(output_image_counter) + ".png"
    new_file_name = str(output_dir) + str(titles[i]) + ".png"
    # print(new_file_name)
    
    plt.subplot(2,3,i+1),
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
    
    cv2.imwrite(new_file_name, images[i]) 
    # cv2.imwrite('localsa.png', images[i])

plt.show()