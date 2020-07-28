### This file stores all the configuration constants for the operation to run and should be check once before starting the operation.

## Location for this file /home/leon/Documents/Intern/TTU/nema-life/conf_files/conf.py


## Test images dir:  /home/leon/Documents/Intern/TTU/nema-life/test_images/
## Video files dir: /home/leon/Documents/Intern/TTU/nema-life/video/
## Mobile Edited Image: /home/leon/Documents/Intern/TTU/nema-life/test_images/mobile

### Parameters for main.py file

# base_dir 		= "/home/cadbury/Documents/"
base_dir        = "/home/leon/Documents/Intern/TTU/"
code_files_dir	= base_dir + "nema-life/" 
raw_image_dir 	= code_files_dir + "test_images/"
result_dir 		= code_files_dir + "results/"
log_dir         = code_files_dir + "logs/"
output_dir      = code_files_dir + "output/"

frame_location  = raw_image_dir + ""

### Parameters for thresholding to convert to binary image from grayscale.
threshold_value = 175

### Parameters for image displaying