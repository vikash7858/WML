#!/usr/bin/python3

import cv2

img_data=cv2.imread('kat.jpeg')
print(img_data)

print (type(img_data))

new_kat=img_data-50
cv2.imwrite('newkat.jpeg',new_kat)
cv2.imshow('katrina',new_kat)
cv2.waitKey(0)
cv2.destroyAllWindows()
