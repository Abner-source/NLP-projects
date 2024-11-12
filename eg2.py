import cv2
import matplotlib.pyplot as plt
import numpy as np
img=cv2.imread(r"C:\Users\Abner\Pictures\OIP.jpeg")
#to convert the color from rgb to bgr
Rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(Rgb)
plt.waitforbuttonpress()
plt.close('all')
