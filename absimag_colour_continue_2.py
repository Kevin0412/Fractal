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
c=-1.25+1/(2*m)*1j
n=0+0j
#img=np.ones((4*m,4*m,3),np.uint8)*255
#cv2.imwrite('absimag_colour_'+str(m)+'_'+str(C)+'_'+str(t)+'.png',img)
img=cv2.imread('absimag_colour_'+str(m)+'.png')
for y in range(12879,-1,-1):
    print(y)
    for x in range(4*m):
        c=(x+0.5)/m-2+((y+0.5)/m-2)*1j
        n=0+0j
        for z in range(1531):
            if abs(n)<=2:
                n=(n.real+abs(n.imag)*1j)**2+c
                if abs(n)>2:
                    img[4*m-y-1][x]=color(z-1)
                    break
        c=(x+0.5)/m-2-((y+0.5)/m-2)*1j
        n=0+0j
        for z in range(1531):
            if abs(n)<=2:
                n=(n.real+abs(n.imag)*1j)**2+c
                if abs(n)>2:
                    img[y][x]=color(z-1)
                    break
    if y%8==0 and y>m:
        cv2.imwrite('absimag_colour_'+str(m)+'.png',img)
        file=open('absimag.txt','w+')
        file.write(str(y-1))
        file.close()
cv2.imwrite('absimag_colour_'+str(m)+'.png',img)
