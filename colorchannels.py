import cv2
img=cv2.imread(r"C:\Users\Abner\Desktop\Python programs\cmyk_paint.png")
B,G,R=cv2.split(img)
cv2.imshow('original', img)
cv2.waitKey(0)
cv2.imshow('blue',B)
cv2.waitKey(0)
cv2.imshow('Green', G)
cv2.waitKey(0)
cv2.imshow('Red', R)
cv2.waitKey(0)
cv2.destroyAllWindows()

