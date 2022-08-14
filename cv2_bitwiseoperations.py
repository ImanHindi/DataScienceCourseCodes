import cv2
import numpy as np
img1=cv2.imread("image11.png")
img2=cv2.imread("image33.png")
#img1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
#img2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
#blur1=cv2.medianBlur(img1,7,cv2.BORDER_DEFAULT)
#blur2=cv2.medianBlur(img2,7,cv2.BORDER_DEFAULT)
#cv2.imshow('blur1',blur1)
#cv2.imshow('blur2',blur2)
cv2.waitKey(0)
cv2.destroyAllWindows()
canned1=cv2.Canny(img1,150,190)
canned2=cv2.Canny(img2,150,190)

cv2.imshow('canned1',canned1)
cv2.imshow('canned2',canned2)

cv2.waitKey(0)
cv2.destroyAllWindows()
bitwise_and=cv2.bitwise_xor(canned1,canned2)
cv2.imshow('bitwise_and',bitwise_and)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel = np.ones((2,2),np.uint8)
dilation = cv2.dilate(bitwise_and,kernel,iterations = 1)
#kernel = np.ones((5,3),np.uint8)
#erosion = cv2.erode(dilation,kernel,iterations = 1)
#opening = cv2.morphologyEx(bitwise_and, cv2.MORPH_OPEN, kernel)
#blur1=cv2.medianBlur(dilation,5,cv2.BORDER_DEFAULT)

#closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
#
#cv2.imshow('dilation',dilation)
#cv2.imshow('erosion',erosion)
#
#cv2.imshow('closing',closing)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
mask=cv2.cvtColor(dilation,cv2.COLOR_GRAY2BGR)

detected_object=cv2.bitwise_and(mask,img2)

cv2.imshow('detected_object',detected_object)

cv2.waitKey(0)
cv2.destroyAllWindows()
#
#hsv=cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)
#lower_range=np.array([170,50,50])
#upper_range=np.array([180,255,255])
##lower_range=np.array([0,0,0])
##upper_range=np.array([20,255,255])
#img2=cv2.inRange(hsv,lower_range,upper_range)
#
#
#
#bitwise_and=cv2.bitwise_and(img1,img2)
#bitwise_or=cv2.bitwise_or(img1,img2)
#bitwise_Xor=cv2.bitwise_xor(img1,img2)
#bitwise_not=cv2.bitwise_not(img1,img2)
#
#cv2.imshow('bitwise_and',bitwise_and)
#cv2.imshow('bitwise_or',bitwise_or)
#cv2.imshow('bitwise_Xor',bitwise_Xor)
#cv2.imshow('bitwise_not',bitwise_not)#
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()