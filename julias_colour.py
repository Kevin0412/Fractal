import cv2
import numpy as np
def color(n):
    if int((n%1530)/255)==0:
        return(0,n%255,255)
    if int((n%1530)/255)==1:
        return(0,255,255-n%255)
    if int((n%1530)/255)==2:
        return(n%255,255,0)
    if int((n%1530)/255)==3:
        return(255,255-n%255,0)
    if int((n%1530)/255)==4:
        return(255,0,n%255)
    if int((n%1530)/255)==5:
        return(255-n%255,0,255)
m=270
C=int(1530/17/3)
c=-1.25+1/(2*m)*1j
n=0+0j
t=0
while(True):
    if abs(n)<=2:
        n=n**2+c
        if abs(n)>2:
            break
    t+=1
t=int((t-1)/C)+1
print(t)
img=np.zeros((4*m,4*m,3),np.uint8)
#img=cv2.imread('result_colour_8192_30_859.png')
for y in range(2*m-1,-1,-1):
    for x in range(4*m):
        n=(x+0.5)/m-2+((y+0.5)/m-2)*1j
        c=-0.4+0.6j
        for z in range(C*t):
            if abs(n)<=2:
                n=n**2+c
                if abs(n)>2:
                    img[4*m-y-1][x]=color(int(z*1530/C))
                    break
        n=(x+0.5)/m-2-((y+0.5)/m-2)*1j
        for z in range(C*t):
            if abs(n)<=2:
                n=n**2+c
                if abs(n)>2:
                    img[y][x]=color(int(z*1530/C))
                    break
    print(y)
cv2.imwrite('julia_colour_'+str(m)+'_'+str(C)+'_'+str(t)+'_'+str(c)+'.png',img)
