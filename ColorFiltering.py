import cv2 as cv
import numpy as np

#Import image
img = cv.imread('colorpic.jpg')
cv.imshow('Image',img)
cv.waitKey(0)
cv.destroyWindow('Image')

#Print image data type and dimensions
print(type(img))
print(np.shape(img))

#Perform bitwise_and operation on image
lower_range = np.array([0,0,0])
upper_range = np.array([100,70,255])
mask = cv.inRange(img,lower_range,upper_range)
result = cv.bitwise_and(img,img,mask = mask)
cv.imshow('Image1',result)
cv.waitKey(0)
cv.destroyWindow('Image1')

#Convert image to gray and then into BGR format
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
bgr = cv.cvtColor(gray,cv.COLOR_GRAY2BGR)
result2 = cv.bitwise_or(bgr,result)
cv.imshow('Image2',result2)
cv.waitKey(0)
cv.destroyWindow('Image2')