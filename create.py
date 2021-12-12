import cv2
import numpy as np
m=14
#img=np.zeros((4*m,4*m),np.uint8)
#for y in range(2*m-1,-1,-1):
for y in range(4*m-1,-1,-1):
    for x in range(4*m):
        c=(x+0.5)/m-2+((y+0.5)/m-2)*1j
        n=0+0j
        for z in range(10):
            if abs(n)<=2:
                n=n**2+c
                if abs(n)>2:
                    '''img[y][x]=z
                    img[4*m-y-1][x]=z'''
                    print(z,end='')
                    break
            if z==9:
                print('.',end='')
    print()
    #print(y)
#cv2.imwrite('result_'+str(m)+'.png',img)
