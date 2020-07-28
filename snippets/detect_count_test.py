# import the necessary packages
import numpy as np
import imutils
import cv2
# print(cv2.__version__)


# load the image
# image_orig = cv2.imread(args["image"])

image_orig = cv2.imread("./../test_images/TOZERO.png",1)
# cv2.imshow("check input",image_orig)

# dict to count colonies
counter = {}

#print (image_orig)
height_orig, width_orig = image_orig.shape[:2]
 
# output image with contours
image_contours = image_orig.copy()
 
# DETECTING WHITE COLONIES

colors = ['white']

for color in colors:
 
    # copy of original image
    image_to_process = image_orig.copy()
 
    # initializes counter
    counter[color] = 0
 
    # define NumPy arrays of color boundaries (BGR vectors)
    if color == 'white':
        # invert image colors
        image_to_process = (255-image_to_process)
        lower = np.array([ 250,  250,  240])
        upper = np.array([255, 255,  255])
 
    # find the colors within the specified boundaries
    image_mask = cv2.inRange(image_to_process, lower, upper)

    # apply the mask
    image_res = cv2.bitwise_and(image_to_process, image_to_process, mask = image_mask)
 
    ## load the image, convert it to grayscale, and blur it slightly
    image_gray = cv2.cvtColor(image_res, cv2.COLOR_BGR2GRAY)
    
    image_gray2 = cv2.GaussianBlur(image_gray, (5, 5), 0)
 
    # perform edge detection, then perform a dilation + erosion to close gaps in between object edges
    image_edgedCanny = cv2.Canny(image_gray, 50, 100)
    
    image_edgedDilate = cv2.dilate(image_edgedCanny, None, iterations=1)
    
    image_edged = cv2.erode(image_edgedDilate, None, iterations=1)
    
 
    # # FOR PROPER UNDERSTANDING (UNCOMMENT THIS):
    # cv2.imshow("image_mask",image_mask)
    # cv2.imshow("image_res",image_res)
    # cv2.imshow("img_gray",image_gray)
    # cv2.imshow("image_gray2",image_gray2)
    # cv2.imshow("canny",image_edgedCanny)
    # cv2.imshow("dilate",image_edged)
    # cv2.imshow("erode",image_edged)

    # find contours in the edge map
    cnts, _ = cv2.findContours(image_edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cnts = cnts[0] if imutils.is_cv2() else cnts[1]
    
    # loop over the contours individually
    for c in cnts:
         
        # if the contour is not sufficiently large, ignore it
        if ((cv2.contourArea(c) > 135)) :
            continue
        #  ontourArea(contours[i]);
        # compute the Convex Hull of the contour
        hull = cv2.convexHull(c)
        if color == 'white':
            # prints contours in green color
            # cv2.drawContours(image_contours,[hull],0,(0,255,0),1)

            x,y,w,h = cv2.boundingRect(c)
            cv2.rectangle(image_contours,(x,y),(x+w,y+h),(0,255,245),1)    # drawing pure rectangle contour.
 
        counter[color] += 1
        #cv2.putText(image_contours, "{:.0f}".format(cv2.contourArea(c)), (int(hull[0][0][0]), int(hull[0][0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
 
    # Print the number of colonies of each color
    print("{} {} colonies".format(counter[color],color))
 
# # Writes the output image
# cv2.imwrite(args["output"],image_contours)

cv2.imwrite("./../output/countAreaTest(upto-135).png",image_contours)

# Also shows the result image
cv2.imshow('Result_image',image_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()