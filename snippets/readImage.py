# Python program to read image using OpenCV 

# importing OpenCV(cv2) module 
import cv2 

# Save image in set directory 
# Read RGB image 
img = cv2.imread('2.jpg') 

# Output img with window name as 'image' 
cv2.imshow('image', img) 

# Maintain output window utill 
# user presses a key 
cv2.waitKey(0)

# Destroying present windows on screen 
cv2.destroyAllWindows() 


# Python program to read  
# image using matplotlib 
  
# importing matplotlib modules 
import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
  
# Read Images 
img = mpimg.imread('2.jpg') 
  
# Output Images 
plt.imshow(img) 


# Python progrm to read 
# image using PIL module 

# importing PIL 
from PIL import Image 

# Read image 
img = Image.open('2.jpg') 

# Output Images 
img.show() 

# prints format of image 
print(img.format) 

# prints mode of image 
print(img.mode) 
