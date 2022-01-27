#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 07:39:56 2022

@author: jason

YOUNG Model 05103 Wind Monitor height: 37 cm, length: 55 cm, Propeller: 18 cm, https://www.youngusa.com/product/wind-monitor/

"""

import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
# from matplotlib.pyplot import figure
# import matplotlib.dates as mdates
# from datetime import datetime
# import sys

import cv2 # OpenCV

# -------------------------------- chdir
if os.getlogin() == 'maiken':
    base_path = '/Users/jason/Dropbox/GCNet_photogrammetry/'
elif os.getlogin() == 'jason':
    base_path = '/Users/jason/Dropbox/GCNet_photogrammetry/'

#%%
img=cv2.imread(base_path+'/img/DY2 1997 J Box.jpg', 0)

cv2.imshow('image', img)


# function to display the coordinates of
# of the points clicked on the image
def click_event(event, x, y, flags, params):
 
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
 
    # checking for right mouse clicks    
    if event==cv2.EVENT_RBUTTONDOWN:
 
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
 
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        cv2.putText(img, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', img)
        # return(x,y)

# setting mouse handler for the image
# and calling the click_event() function
cv2.setMouseCallback('image', click_event)

#%% image scale
wind_sensor_height=0.37 # meters
image_scale=(1825-1735)/wind_sensor_height # pixels per m
print("image_scale = {:.0f}".format(image_scale)+' pixels per m')

profile_lower_y=2384
profile_upper_y=1889

profile_separation=(profile_lower_y-profile_upper_y)/image_scale # pixels per m
print("profile_separation = {:.3f}".format(profile_separation)+' m')

#%%

 
# driver function
if __name__=="__main__":
 
    # reading the image
    img = cv2.imread('lena.jpg', 1)
 
    # displaying the image
    cv2.imshow('image', img)
 
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
 
    # wait for a key to be pressed to exit
    cv2.waitKey(0)
 
    # close the window
    cv2.destroyAllWindows()