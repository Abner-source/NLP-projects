import cv2
img=cv2.imread(r"C:\Users\Abner\Pictures\OIP.jpeg", cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
print('image shape',img.shape)