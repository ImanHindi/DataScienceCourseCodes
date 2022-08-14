from cv2 import COLOR_BGR2GRAY, COLOR_BGR2HLS, COLOR_BGR2HSV
import numpy as np
import cv2


image=cv2.imread('test1.jpg',cv2.IMREAD_COLOR)
#r,g,b=cv2.split(image)
#cv2.imshow("r",r)
#
#cv2.imshow("g",g)
#
#cv2.imshow("b",b)
#
#cv2.imshow("image",image)
#cv2.waitKey()
#print(image.shape)
#image=cv2.cvtColor(image,COLOR_BGR2HSV)
#image=cv2.cvtColor(image,COLOR_BGR2HLS)
#
#cv2.imshow("image",image)
#cv2.waitKey()
#image=cv2.resize(image,(300,300))
#cv2.imshow("image",image)
#cv2.waitKey()
#cv2.imwrite("test22.png",image)
#
white_image=np.ones((512,512,3))*255
black_image=np.zeros((512,512,3))
#
#cv2.imshow("white image",white_image)
#cv2.imshow("black image",black_image)
#
#cv2.waitKey()
#
image11=cv2.imread('image11.png',cv2.IMREAD_COLOR)
image22=cv2.imread('image22.png',cv2.IMREAD_COLOR)

#image11=cv2.resize(image11,(250,250))
#image22=cv2.resize(image22,(250,250))


addedimage=cv2.add(image22,image11)
addedimage=cv2.addWeighted(image11,0.9,image22,.5,.1)

cv2.imwrite("image33.png",addedimage)
cv2.imshow("Added image",addedimage)
cv2.waitKey()
cv2.destroyAllWindows()

