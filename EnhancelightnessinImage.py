#two method to smooth the lightness:
#    1.equalizehist
#    2.clahe


import cv2
import numpy as np

image=cv2.imread('lightness.jpg',0)
image=cv2.imread('image44.jfif',0)
print(image.shape)
#image=cv2.resize(image2,(480,670))
equ=cv2.equalizeHist(image)
image_equalizeHist = np.hstack((image,equ))
#image=cv2.resize(image,(500,500))
#image2=cv2.resize(image2,(500,500))

cv2.imshow('image_equalizeHist',image_equalizeHist)
#cv2.imshow('image2',image2)

# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(image)
image_clahe = np.hstack((image,cl1))
cv2.imshow('image_clahe',image_clahe)

cv2.waitKey(0)
cv2.destroyAllWindows()
#
#
#
#from PIL import Image, ImageEnhance
#
##read the image
#im = Image.open("sample-image.png")#image brightness enhancer
#enhancer = ImageEnhance.Contrast(im)
#
#factor = 1 #gives original image
#im_output = enhancer.enhance(factor)
#im_output.save('original-image.png')
#
#factor = 0.5 #decrease constrast
#im_output = enhancer.enhance(factor)
#im_output.save('less-contrast-image.png')
#
#factor = 1.5 #increase contrast
#im_output = enhancer.enhance(factor)
#im_output.save('more-contrast-image.png')