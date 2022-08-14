import numpy as np
import cv2


image=cv2.imread('test1.jpg',cv2.IMREAD_GRAYSCALE)
image=cv2.resize(image,(500,500))

ret,thre1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
ret,thre2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
ret,thre3=cv2.threshold(image,127,255,cv2.THRESH_TOZERO)
ret,thre4=cv2.threshold(image,127,255,cv2.THRESH_TOZERO_INV)
ret,thre5=cv2.threshold(image,127,255,cv2.THRESH_TRUNC)

cv2.imshow('thre1',thre1)
cv2.imshow('thre2',thre2)
cv2.imshow('thre3',thre3)
cv2.imshow('thre4',thre4)
cv2.imshow('thre5',thre5)

cv2.waitKey(0)
cv2.destroyAllWindows()
ret,th1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY)
thrregaussian=cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,9,2)
thremean = cv2.adaptiveThreshold(image,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
cv2.imshow('thrregaussian',thrregaussian)
cv2.imshow('thremean',thremean)

cv2.waitKey(0)
cv2.destroyAllWindows()

blur1=cv2.blur(image,(9,9),0)

cv2.imshow('blur1',blur1)
blur_gausian=cv2.GaussianBlur(image,(9,9),0)
blur_median=cv2.medianBlur(image,9,0)
cv2.imshow('blur_gausian',blur_gausian)
cv2.imshow('blur_median',blur_median)

cv2.waitKey(0)
cv2.destroyAllWindows()