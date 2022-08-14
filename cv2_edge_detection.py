import numpy as np
import cv2 as cv

image=cv.imread('test1.jpg',cv.IMREAD_GRAYSCALE)
image=cv.resize(image,(500,500))
image=cv.imread("image11.png")

#lablacian
laplace=cv.Laplacian(image,cv.CV_64F)
laplace=np.uint8(np.absolute(laplace))

cv.imshow('laplace',laplace)

cv.waitKey(0)
cv.destroyAllWindows()


#Sobel:

sobel_x=cv.Sobel(image,cv.CV_64F,1,0)
sobel_y=cv.Sobel(image,cv.CV_64F,0,1)
sobel=cv.bitwise_or(sobel_x,sobel_y)
cv.imshow('sobel',sobel)

cv.waitKey(0)
cv.destroyAllWindows()


#Canny

blur=cv.GaussianBlur(image,(3,3),cv.BORDER_DEFAULT)
canned=cv.Canny(image,150,190)

cv.imshow('canned',canned)

cv.waitKey(0)
cv.destroyAllWindows()