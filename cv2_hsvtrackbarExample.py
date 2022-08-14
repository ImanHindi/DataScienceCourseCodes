#import cv2
#import numpy as np
#
#def nothing(x):
#    pass
#
## Create a black image, a window
#img = np.zeros((512,512,3), np.uint8)
#cv2.namedWindow('image')
#
## create trackbars for color change
#cv2.createTrackbar('R','image',0,255,nothing)
#cv2.createTrackbar('G','image',0,255,nothing)
#cv2.createTrackbar('B','image',0,255,nothing)
#
#while True:
#    cv2.imshow('image',img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break
#    
#    # get current positions of three trackbars
#    r = cv2.getTrackbarPos('R','image')
#    g = cv2.getTrackbarPos('G','image')
#    b = cv2.getTrackbarPos('B','image')
#
#    img[:] = [b,g,r]
#
#cv2.destroyAllWindows()


import cv2
import numpy as np

def nothing(x):
    pass

# Create a black image, a window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('H','image',0,180,nothing)
cv2.createTrackbar('S','image',0,255,nothing)
cv2.createTrackbar('I','image',0,255,nothing)

while(True):
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # get current positions of four trackbars
    h = cv2.getTrackbarPos('H','image')
    s = cv2.getTrackbarPos('S','image')
    i = cv2.getTrackbarPos('I','image')

    img[:,:] = [h,s,i]
    img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

cv2.destroyAllWindows()