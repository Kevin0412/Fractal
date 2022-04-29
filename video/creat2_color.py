import cv2
import numpy as np
import tqdm
def color(n):
    if n==15300:
        return(255,255,255)
    else:
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
for k in range(34,8,-1):
    img=np.zeros((2160,3840),np.complex128)
    img2=np.zeros((2160,3840),np.int16)+15300
    img3=np.zeros((2160,3840),np.complex128)
    img5=np.zeros((2160,3840,3),np.uint8)
    for y in tqdm.tqdm(range(2159,-1,-1)):
        for x in range(3840):
            c=(x-1920)/2**k+0.29341989288727477+((y-1080)/2**k+0.481365430202407)*1j
            if c.real<-2:
                img[2159-y][x]=-2+1j
            else:
                img[2159-y][x]=c
    for m in range(2):
        for n in tqdm.tqdm(range(1530)):
            img3=img3**2+img
            img4=cv2.inRange((abs(img3)-2**-52).astype(np.uint8),2,255)
            cv2.imshow('frame',cv2.resize(img4,(640,360)))
            cv2.waitKey(1)
            img2-=(img4/255).astype(np.uint8)
            img3=img3*(255-img4)/255+(2+2**-51)*img4/255
    for p in tqdm.tqdm(range(2160)):
        for q in range(3840):
            img5[p][q]=color(img2[p][q])
    cv2.imwrite('video2/'+str(k)+'_1.png',img5)
