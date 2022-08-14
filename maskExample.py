import numpy as np
import cv2


image=cv2.imread('Image1.png',cv2.IMREAD_COLOR)
image=cv2.resize(image,(500,500))

hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_range=np.array([0,50,50])
upper_range=np.array([180,255,255])
lower_range=np.array([150,50,50])
upper_range=np.array([180,255,255])
#lower_range=np.array([0,0,0])
#upper_range=np.array([20,255,255])
mask=cv2.inRange(hsv,lower_range,upper_range)

cv2.imshow('image',image)
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()