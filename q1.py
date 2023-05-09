import cv2
import numpy as np

img = cv2.imread('duck-lab7.png')

b, g, r = cv2.split(img)

cv2.imshow('Blue channel', b)
cv2.imshow('Green channel', g)
cv2.imshow('Red channel', r)

img[:, :, 1] = 0

cv2.imshow('Only red & blue channels', img)

new_img = cv2.merge([b, g, r])

cv2.imshow('Merged Image', new_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
