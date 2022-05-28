import cv2
import numpy as np
import tqdm
img=np.zeros((256,256),np.complex128)
img2=np.zeros((256,256),np.int16)-32768
img3=np.zeros((256,256),np.complex128)
for y in tqdm.tqdm(range(255,-1,-1)):
    for x in range(256):
        c=(x+0.5)/64-2+((y+0.5)/64-2)*1j
        #c=(x+0.5)/2**16+1/4+((y+0.5)/2**16+3/8)*1j
        #c=(x+0.5)/2**18+1/4+1/32+((y+0.5)/2**18+3/8+3/32)*1j
        #c=(x+0.5)/2**20+1/4+1/32+1/128+((y+0.5)/2**20+3/8+3/32+1/128)*1j
        #c=(x+0.5)/2**22+1/4+1/32+1/128+2/512+((y+0.5)/2**22+3/8+3/32+1/128+2/512)*1j
        #c=(x+0.5)/2**24+1/4+1/32+1/128+2/512+((y+0.5)/2**24+3/8+3/32+1/128+2/512+1/2048)*1j
        #c=(x+0.5)/2**26+1/4+1/32+1/128+2/512+3/8192+((y+0.5)/2**26+3/8+3/32+1/128+2/512+1/2048+3/8192)*1j
        #c=(x+0.5)/2**28+1/4+1/32+1/128+2/512+3/8192+2/2**15+((y+0.5)/2**28+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15)*1j
        #c=(x+0.5)/2**28+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+((y+0.5)/2**28+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17)*1j
        #c=(x+0.5)/2**30+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+((y+0.5)/2**30+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19)*1j
        #c=(x+0.5)/2**32+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+((y+0.5)/2**32+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19)*1j
        #c=(x+0.5)/2**34+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+((y+0.5)/2**34+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23)*1j
        #c=(x+0.5)/2**36+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+((y+0.5)/2**36+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25)*1j
        #c=(x+0.5)/2**38+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+3/2**27+((y+0.5)/2**38+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25+2/2**27)*1j
        #c=(x+0.5)/2**40+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+3/2**27+1/2**29+((y+0.5)/2**40+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25+2/2**27+1/2**29)*1j
        #c=(x+0.5)/2**42+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+3/2**27+1/2**29+1/2**31+((y+0.5)/2**42+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25+2/2**27+1/2**29+2/2**31)*1j
        #c=(x+0.5)/2**44+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+3/2**27+1/2**29+1/2**31+3/2**33+((y+0.5)/2**44+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25+2/2**27+1/2**29+2/2**31)*1j
        #c=(x+0.5)/2**46+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+3/2**27+1/2**29+1/2**31+3/2**33+3/2**35+((y+0.5)/2**46+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25+2/2**27+1/2**29+2/2**31+1/2**35)*1j
        #c=(x+0.5)/2**48+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+3/2**27+1/2**29+1/2**31+3/2**33+3/2**35+2/2**37+((y+0.5)/2**48+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25+2/2**27+1/2**29+2/2**31+1/2**35)*1j
        #c=(x+0.5)/2**50+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+3/2**27+1/2**29+1/2**31+3/2**33+3/2**35+2/2**37+0.5/2**39+((y+0.5)/2**50+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25+2/2**27+1/2**29+2/2**31+1/2**35+2/2**39)*1j
        #c=(x+0.5)/2**52+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+3/2**27+1/2**29+1/2**31+3/2**33+3/2**35+2/2**37+0.5/2**39+2.5/2**41+0.25/2**43+((y+0.5)/2**52+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25+2/2**27+1/2**29+2/2**31+1/2**35+2/2**39+1.375/2**41+1.5/2**43)*1j
        #c=x/2**54+1/4+1/32+1/128+2/512+3/8192+2/2**15+3/2**17+2/2**21+1/2**25+3/2**27+1/2**29+1/2**31+3/2**33+3/2**35+2/2**37+0.5/2**39+2.5/2**41+0.25/2**43+1.5/2**45+(y/2**54+3/8+3/32+1/128+2/512+1/2048+3/8192+1/2**15+1/2**17+2/2**19+1/2**23+3/2**25+2/2**27+1/2**29+2/2**31+1/2**35+2/2**39+1.375/2**41+1.5/2**43+1.5/2**45)*1j
        #c=(x+0.5)/2**32+1/4+1/32+1/128+2/512+2/2**19+((y+0.5)/2**32+3/8+3/32+1/128+2/512+1/2048)*1j
        #c=(x+0.5)/2**34+1/4+1/32+1/128+2/512+2/2**19+((y+0.5)/2**34+3/8+3/32+1/128+2/512+1/2048)*1j
        #c=(x+0.5)/2**36+1/4+1/32+1/128+2/512+2/2**19+((y+0.5)/2**36+3/8+3/32+1/128+2/512+1/2048)*1j
        #c=(x+0.5)/2**38+1/4+1/32+1/128+2/512+2/2**19+1/2**25+((y+0.5)/2**38+3/8+3/32+1/128+2/512+1/2048+2/2**25)*1j
        #c=(x+0.5)/2**40+1/4+1/32+1/128+2/512+2/2**19+1/2**25+((y+0.5)/2**40+3/8+3/32+1/128+2/512+1/2048+2/2**25)*1j
        #c=(x-128)/2**54+0.29341989288727477+((y-128)/2**54+0.481365430202407)*1j
        img[255-y][x]=c
for n in tqdm.tqdm(range(65536)):
    img3=img3**2+img
    img4=cv2.inRange((abs(img3)-2**-52).astype(np.uint8),2,255)
    #cv2.imshow('frame',img4)
    #cv2.waitKey(1)
    img2-=(img4/255).astype(np.uint8)
    img3=img3*(255-img4)/255+(2+2**-51)*img4/255
with open('2.csv','w+') as F:
    for x in tqdm.tqdm(range(256)):
        for y in range(256):
            F.write(str(img2[x][y]+32768))
            F.write(',')
        F.write('\n')
#cv2.imwrite('36.png',img2)
