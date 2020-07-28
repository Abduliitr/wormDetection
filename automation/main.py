## This is the main file which is to be executed for running the whole application.
## This file shall take care of all the functions needed to call for its functioning
## This fiel clls other files as per the need arises.
## make sure you check the conf.file before starting the code.

import logging   ## For logging purpose, useful in debugging
import subprocess
import multiprocessing
import time
import json
import os, errno
import csv
import numpy as np
import imutils
import cv2
from matplotlib import pyplot as plt

import write_json

import sys
dir = "./../conf_files"
# print(dir)
sys.path.insert(0,dir)
import conf

output_dir = conf.output_dir
output_dir_data = conf.output_dataSet_dir
thresh_val = conf.threshold_value

def detect_count_Colored(image_orig , thresh):
    # dict to count colonies
    counter = {}
    height_orig, width_orig = thresh1.shape[:2]

    # output image with contours
    # image_contours = thresh1.copy()
    image_contours = image_orig.copy()

    colors = ['white']

    for color in colors:
    
        # copy of original image
        image_to_process = thresh1.copy()
    
        # initializes counter
        counter[color] = 0
    
        # define NumPy arrays of color boundaries (BGR vectors)
        if color == 'white':
            # invert image colors
            image_to_process = (255-image_to_process)
            lower = np.array([ 150,  150,  140])
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
        
        # find contours in the edge map
        cnts, _ = cv2.findContours(image_edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        
        #This list is the list of list consisting the name of frame and the 4 parameters of each rectangle i.e. x, y, w, h
        rectangle_data = []
        # loop over the contours individually

        i=1     # to change the name of the data-sets.

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

            ####  to save the dataset with different names.
                # img2crop = image_contours[x:w,y:h]
                # new_file_name = str(output_dir_data) + "dataSet" + str(i) + ".png"
                # cv2.imwrite(new_file_name , img2crop)
                # i+=1

                cnt_data = []
                cnt_data.append("frame_name") ## this has to be modified
                cnt_data.append(x)
                cnt_data.append(y)
                cnt_data.append(w)
                cnt_data.append(h)
                cv2.rectangle(image_contours,(x,y),(x+w,y+h),(0,255,245),1)    # drawing pure rectangle contour.
                
                ## Take the above 4 values and make a list of them. set the name of frame as frame_i and then the json file shall be named as that of the frame. Also frame image has also be saved separately
                rectangle_data.append(cnt_data)

    
            counter[color] += 1
            #cv2.putText(image_contours, "{:.0f}".format(cv2.contourArea(c)), (int(hull[0][0][0]), int(hull[0][0][1])), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (255, 255, 255), 2)
    
        # Print the number of colonies of each color
        print("{} {} colonies".format(counter[color],color))
    
    # # Writes the output image
    # cv2.imwrite(args["output"],image_contours)
    cv2.imwrite("./../output/countAreaColored(upto-135).png",image_contours)
    
    ### Now send the data rectangle_data to a function where it will be stored as json file on the disk.
    ##  Call a function in a separate python file and save the json.
    #   print(rectangle_data) ##working
    write_json.create_json("tempfile",rectangle_data)

    return image_contours


def main():

    print(conf.log_dir)
    # log_file_name = conf.log_dir + "nema_monitor.log"
    # print(log_file_name)
    # log_file_name = "/home/leon/Documents/Intern/TTU/nema-life/logs/nema_monitor.log"
    # logging.basicConfig(level=logging.WARNING,format='%(asctime)s%(message)s',filename=log_file_name,filemode='w')
    
    logging.basicConfig(level=logging.WARNING,format='%(asctime)s%(message)s',filename="./../logs/nema_monitor.log",filemode='w')
    logging.warning ("Logging")
    print("Logging")

    ## Function to input the frame (or Video and then read frame by frame)
        # for now this is function to get the image.

    image_orig = cv2.imread("./../test_images/mobile/image2.jpg",1) 
        # using image2.jpg currently , we will be converting image1.jpeg to image1.jpg and then will use it.   
    
    
    ##Function to binarize the frame
        #we will have binarized image here.
    ret,thresh1 = cv2.threshold(image_orig,thresh_val,255,cv2.THRESH_BINARY)
    
    
    ## function to Detect the objects, separate functions for dilating and masking (#Nested Functions)
        #We will have a python list of all the coordinates of detected objects here.
    
    detected_image = detect_count_Colored(image_orig, thresh1)   # this funtion will return the detected image.


    ## Function to send the data for JSON Parsing
        # In this a separate JSON file will be saved including the details of the detected objects: worms and non_worms. Also, a separate name will be given to each JSON file as per the name of the frame(or the video) which is to be studied. this will be used for further studies.




if __name__ == '__main__':
	main()