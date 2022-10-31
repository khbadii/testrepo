# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 13:29:32 2022

@author: khbad

Format:
    python filmmaker2.py <frame 1 name> <frame 2 name> <frame 3 name> <frame 4 name> <image type> <frame per sec> <video output file>
Example:
    python filmmaker2.py 1 2 3 4 PNG 15 outvideo.mp4
"""

import cv2
#import numpy as np
import sys
#import time



def motionmaker(image1, image2, image3, image4, imagetype, fps1, vidout):
    
#    frame_size = (vid1.get(cv2.CAP_PROP_FRAME_WIDTH),
  #                        vid1.get(cv2.CAP_PROP_FRAME_HEIGHT))
 #   fps = vid1.get(cv2.CAP_PROP_FPS)
    #fps = 30
    fps = int(fps1)
    out = cv2.VideoWriter(vidout,cv2.VideoWriter_fourcc(*'X264'), fps,
                          (853, 480))
                          #(int(frame_size[0]), int(frame_size[1])))

    for i in range(120):
        im1 = cv2.imread(image1 + "." + imagetype)
        im1 = cv2.resize(im1, dsize=(853, 480), interpolation=cv2.INTER_CUBIC)
        out.write(im1)
        im2 = cv2.imread(image2 + "." + imagetype)
        im2 = cv2.resize(im2, dsize=(853, 480), interpolation=cv2.INTER_CUBIC)
        out.write(im2)
        im3 = cv2.imread(image3 + "." + imagetype)
        im3 = cv2.resize(im3, dsize=(853, 480), interpolation=cv2.INTER_CUBIC)
        out.write(im3)
        im4 = cv2.imread(image4 + "." + imagetype)
        im4 = cv2.resize(im4, dsize=(853, 480), interpolation=cv2.INTER_CUBIC)
        out.write(im4)


    out.release()
    
    
if __name__ == '__main__':

    motionmaker(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]), str(sys.argv[4]), str(sys.argv[5]), str(sys.argv[6]), str(sys.argv[7]))