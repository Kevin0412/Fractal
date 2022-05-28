import cv2
import numpy as np
import tqdm
name='video2/'
video = cv2.VideoWriter("video.mp4", cv2.VideoWriter_fourcc('I', '4', '2', '0'), 24, (1920,1080))
for m in tqdm.tqdm(range(9,55)):
    img=cv2.imread(name+str(m)+'.png')
    for n in range(36,0,-1):
        video.write(cv2.resize(img[int(1080-540*2**(n/36)):int(1080+540*2**(n/36)),int(1920-960*2**(n/36)):int(1920+960*2**(n/36))],(1920,1080)))
video.write(cv2.resize(img[1080-540:1080+540,1920-960:1920+960],(1920,1080)))
video.release()