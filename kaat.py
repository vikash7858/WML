import cv2

img_data=cv2.imread('kaat.jpg')
print(img_data)

print (type(img_data))

new_kaat=img_data-50
cv2.imwrite('newkaat.jpg',new_kaat)
cv2.imshow('katrina',new_kaat)
cv2.waitKey(0)
cv2.destroyAllWindows()
