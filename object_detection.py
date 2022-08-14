import cv2
import numpy as np
img1=cv2.imread("image11.png")
img2=cv2.imread("image33.png")
#read color
#use absdiff
#convert diff to grayscale
#apply threshold
#convert threshold to bgr
#apply using bitwise and
#img2=cv2.bitwise_or(img1,img2)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
mask=cv2.absdiff(img2,img1)
mask=cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
ret,mask=cv2.threshold(mask,120,255,cv2.THRESH_BINARY)
mask=cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

bitwise_and=cv2.bitwise_and(mask,img2)
cv2.imshow('bitwise_and',bitwise_and)
cv2.waitKey(0)
cv2.destroyAllWindows()

#canned1=cv2.Canny(img1,150,190)
#canned2=cv2.Canny(img2,150,190)
#
#cv2.imshow('canned1',canned1)
#cv2.imshow('canned2',canned2)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#
#bitwise_and=cv2.bitwise_xor(canned1,canned2)
#cv2.imshow('bitwise_and',bitwise_and)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#
#kernel = np.ones((2,2),np.uint8)
#dilation = cv2.dilate(bitwise_and,kernel,iterations = 1)
#
#
##closing = cv2.morphologyEx(dilation, cv2.MORPH_CLOSE, kernel)
##cv2.imshow('closing',closing)
#
##cv2.waitKey(0)
##cv2.destroyAllWindows()
#mask=cv2.cvtColor(dilation,cv2.COLOR_GRAY2BGR)
#
#cv2.imshow('mask',mask)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#detected_object=cv2.bitwise_and(mask,img2)
#
#cv2.imshow('detected_object',detected_object)
#
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#

