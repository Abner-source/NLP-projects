import cv2
import os
image_path=r"C:\Users\Abner\Pictures\OIP.jpeg"
directory=r"C:\Users\Abner\Pictures"
img=cv2.imread(image_path)
#changing the current diretory to a specified directory
os.chdir(directory)
#listing files and directories in the directory
print("before saving image:")
print(os.listdir(directory))
filename='savedImage.jpg'
#using cv2.imwrite method to save the image to a specific location
cv2.imwrite(filename, img)
print("After saving image:")
print(os.listdir(directory))
print("successfully saved")