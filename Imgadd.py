#!/usr/bin/python3

import  cv2
import numpy  as  np
print(cv2.__version__)

# now reading image 
#  image flags                       1
dog_img=cv2.imread('dog1.jpeg')
cat_img=cv2.imread('cat1.jpeg')
adimg=cv2.add(dog_img,cat_img)
cat_dog=dog_img+cat_img         # gamma -- 0 /  1
cat_dog=cv2.addWeighted(dog_img,0.5,cat_img,0.5,0)
cv2.imshow('td',cat_dog)
cv2.imshow('td1',adimg)
cv2.waitKey(0)

