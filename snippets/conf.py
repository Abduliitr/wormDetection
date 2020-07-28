### This file stores all the configuration constants for the operation to run and should be check once before starting the operation.

## Location for this file /home/leon/Documents/Intern/TTU/nema-life/conf_files/conf.py


## Test images dir:  /home/leon/Documents/Intern/TTU/nema-life/test_images/
## Video files dir: /home/leon/Documents/Intern/TTU/nema-life/video/
## Mobile Edited Image: /home/leon/Documents/Intern/TTU/nema-life/test_images/mobile

### Parameters for main.py file

base_dir 		    = "/home/cadbury/Documents/"
code_files_dir	    = base_dir + "nema-life/" 
raw_image_dir 	    = code_files_dir + "images/"
result_dir 		    = code_files_dir + "results/"
log_dir             = code_files_dir + "logs/"
output_dir          = code_files_dir + "output/"
output_dataSet_dir  = output_dir + "dataSet/"

### Parameters for thresholding to convert to binary image from grayscale.
threshold_value = 170

## test threshold:-
# threshold_value = 180

### Parameters for image displaying