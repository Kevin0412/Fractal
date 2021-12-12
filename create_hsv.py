import cv2
import numpy as np
def color(n,a=10,b=17):
    return((n*a)%180,255,255-int(n/180*a)*b-b)
m=512
img=np.zeros((4*m,4*m,3),np.uint8)
for y in range(2*m-1,-1,-1):
    for x in range(4*m):
        c=(x+0.5)/m-2+((y+0.5)/m-2)*1j
        n=0+0j
        for z in range(243):
            if abs(n)<=2:
                n=n**2+c
                if abs(n)>2:
                    img[y][x]=color(z)
                    img[4*m-y-1][x]=color(z)
                    break
    print(y)
cv2.imwrite('result_hsv_'+str(m)+'.png',cv2.cvtColor(img,cv2.COLOR_HSV2BGR))
