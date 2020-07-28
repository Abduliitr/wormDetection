import cv2

fn = '../video/test.mp4'
cap = cv2.VideoCapture(fn)

# # if not cap.isOpened(): 
# #     print "could not open :",fn
# #     return

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps    = cap.get(cv2.CAP_PROP_FPS)
duration = float(total_frames/fps)

print(total_frames)
print(width)
print(height)
print(fps)
print(duration)
