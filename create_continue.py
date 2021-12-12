import cv2
import numpy as np
'''def color(n):
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
        return(255-n%255,0,255)'''
m=20000
#C=int(1530/17/3)
#c=-1.25+1/(2*m)*1j
#n=0+0j
#t=0
'''while(True):
    if abs(n)<=2:
        n=n**2+c
        if abs(n)>2:
            break
    t+=1
t=int((t-1)/C)+1
print(t)'''
img=np.zeros((4*m,4*m),np.uint8)
img=cv2.imread('result_16384.png')
print(img[0][0])
'''for y in range(39619,-1,-1):
    print(y)
    for x in range(4*m):
        c=(x+0.5)/m-2+((y+0.5)/m-2)*1j
        n=0+0j
        for z in range(256):
            if abs(n)<=2:
                n=n**2+c
                if abs(n)>2:
                    img[y][x]=z
                    img[4*m-y-1][x]=z
                    break
    if y%20==0:
        cv2.imwrite('result_'+str(m)+'.png',img)
        file=open('continue_grey.txt','w+')
        file.write(str(y-1))
        file.close()
cv2.imwrite('result_'+str(m)+'.png',img)'''
