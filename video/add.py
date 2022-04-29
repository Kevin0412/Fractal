import cv2
import numpy as np
img=cv2.imread('video2/37_1.png')
img1=cv2.imread('video2/38.png')
img[540:1620,960:2880]=cv2.resize(img1,(1920,1080))
cv2.imwrite('video2/37.png',img)
