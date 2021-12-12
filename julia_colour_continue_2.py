import cv2
import numpy as np
def color(n):
    if n==-1:
        return(0,0,0)
    elif int((n%1530)/255)==0:
        return(0,n%255,255)
    elif int((n%1530)/255)==1:
        return(0,255,255-n%255)
    elif int((n%1530)/255)==2:
        return(n%255,255,0)
    elif int((n%1530)/255)==3:
        return(255,255-n%255,0)
    elif int((n%1530)/255)==4:
        return(255,0,n%255)
    elif int((n%1530)/255)==5:
        return(255-n%255,0,255)
m=8000
c=-0.8+0.156j
#img=np.zeros((4*m,4*m,3),np.uint8)
#img=cv2.imread('result_colour_8192_30_859.png')
img=cv2.imread('julia_color_'+str(m)+'_'+str(c)+'.png')
for y in range(7999,-1,-1):
    print(y)
    for x in range(4*m):
        n=(x+0.5)/m-2+((y+0.5)/m-2)*1j
        for z in range(1531):
            if abs(n)<=2:
                n=n**2+c
                if abs(n)>2:
                    img[4*m-y-1][x]=color(z-1)
                    break
        n=(x+0.5)/m-2-((y+0.5)/m-2)*1j
        for z in range(1531):
            if abs(n)<=2:
                n=n**2+c
                if abs(n)>2:
                    img[y][x]=color(z-1)
                    break
    if y%80==0:
        cv2.imwrite('julia_color_'+str(m)+'_'+str(c)+'.png',img)
        file=open('julia.txt','w+')
        file.write(str(y-1))
        file.close()
cv2.imwrite('julia_color_'+str(m)+'_'+str(c)+'.png',img)
