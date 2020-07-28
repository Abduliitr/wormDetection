import cv2

#namedWindow is used to name a window
#it's essentially used in --> cv2.getTrackbarPos(trackbarname, WINDOW_NAME) 
  
#  -->  cv2.namedWindow('window_name' , flags)

cv2.namedWindow(name, CV_WINDOW_AUTOSIZE) → None

#Flags of the window. The supported flags are:

    # WINDOW_NORMAL If this is set, the user can resize the window (no constraint).
    # WINDOW_AUTOSIZE If this is set, the window size is automatically adjusted to fit the displayed image (see imshow() ), and you cannot change the window size manually.
    # WINDOW_OPENGL If this is set, the window will be created with OpenGL support.

# Qt backend supports additional flags:

#     CV_WINDOW_NORMAL or CV_WINDOW_AUTOSIZE: CV_WINDOW_NORMAL enables you to resize the window, whereas CV_WINDOW_AUTOSIZE adjusts automatically the window size to fit the displayed image (see imshow() ), and you cannot change the window size manually.
#     CV_WINDOW_FREERATIO or CV_WINDOW_KEEPRATIO: CV_WINDOW_FREERATIO adjusts the image with no respect to its ratio, whereas CV_WINDOW_KEEPRATIO keeps the image ratio.
#     CV_GUI_NORMAL or CV_GUI_EXPANDED: CV_GUI_NORMAL is the old way to draw the window without statusbar and toolbar, whereas CV_GUI_EXPANDED is a new enhanced GUI.


