import cv2
#checking opencv version
print("cv2 version:",cv2.__version__)
#checking to see if opencv works correctly
img=cv2.imread(r"C:\Users\Abner\Pictures\OIP.jpeg")
if img is None:
    print('image not loaded correctly')
else:
    print('cv2 is working successfully')
cv2.imshow('Loaded image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()