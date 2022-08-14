import cv2
import numpy as np


image=cv2.imread('test1.jpg')
image=cv2.resize(image,(500,500))
#blur image:
blurred_image=cv2.medianBlur(image,9,0)
cv2.imshow('blurred_image',blurred_image)
#alpha  # Contrast control (1.0-3.0)
#beta  # Brightness control (0-100)
#using add weighted:
sharpen_image_addWeighted=cv2.addWeighted(image, 1.8, image, -0.5, 0.2, image)
cv2.imshow('sharpen_image_addWeighted',sharpen_image_addWeighted)



#Using filter2d:
kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
#kernel = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, 0]]) 
#kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
sharpen_image_filter2D = cv2.filter2D(image, -1, kernel)
cv2.imshow('sharpen_image_filter2D',sharpen_image_filter2D)

cv2.waitKey(0)
cv2.destroyAllWindows()