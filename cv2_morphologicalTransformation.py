
import numpy as np
import cv2 as cv


image=cv.imread('morph.png',cv.IMREAD_GRAYSCALE)
#image=cv.resize(image,(500,500))

image=cv.imread('test1.jpg',cv.IMREAD_GRAYSCALE)
image=cv.resize(image,(500,500))
kernel = np.ones((2,2),np.uint8)
thrregaussian=cv.adaptiveThreshold(image,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,9,2)

erosion = cv.erode(thrregaussian,kernel,iterations = 1)
cv.imshow('image',image)
cv.imshow('erosion',erosion)

cv.waitKey(0)
cv.destroyAllWindows()

dilation = cv.dilate(thrregaussian,kernel,iterations = 1)
cv.imshow('dilation',dilation)

cv.waitKey(0)
cv.destroyAllWindows()

opening = cv.morphologyEx(thrregaussian, cv.MORPH_OPEN, kernel)

cv.imshow('opening',opening)

cv.waitKey(0)
cv.destroyAllWindows()


closing = cv.morphologyEx(thrregaussian, cv.MORPH_CLOSE, kernel)
cv.imshow('closing',closing)

cv.waitKey(0)
cv.destroyAllWindows()

gradient = cv.morphologyEx(thrregaussian, cv.MORPH_GRADIENT, kernel)
cv.imshow('gradient',gradient)

cv.waitKey(0)
cv.destroyAllWindows()


tophat = cv.morphologyEx(thrregaussian, cv.MORPH_TOPHAT, kernel)
cv.imshow('tophat',tophat)

cv.waitKey(0)
cv.destroyAllWindows()

blackhat = cv.morphologyEx(thrregaussian, cv.MORPH_BLACKHAT, kernel)
cv.imshow('blackhat',blackhat)

cv.waitKey(0)
cv.destroyAllWindows()


# Rectangular Kernel
cv.getStructuringElement(cv.MORPH_RECT,(5,5))
np.array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]])
# Elliptical Kernel
cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
np.array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]])
# Cross-shaped Kernel
cv.getStructuringElement(cv.MORPH_CROSS,(5,5))
np.array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]])