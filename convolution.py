import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('eljajas.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel=np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel)
blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5))
median = cv2.medianBlur(img,5)
bilateralFilter = cv2.bilateralFilter(img,9,75,75)




