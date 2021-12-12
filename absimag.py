import cv2
import numpy as np
m=16384
img=np.zeros((4*m,4*m),np.uint8)
for y in range(4*m):
    for x in range(4*m):
        c=(x+0.5)/m-2+((y+0.5)/m-2)*1j
        n=0+0j
        for z in range(256):
            if abs(n)<=2:
                n=(n.real+abs(n.imag)*1j)**2+c
                if abs(n)>2:
                    img[y][x]=z
                    break
    print(y)
cv2.imwrite('absimag_'+str(m)+'.png',img)
