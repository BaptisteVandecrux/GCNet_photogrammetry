#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 07:39:56 2022

@author: jason, bav

YOUNG Model 05103 Wind Monitor height: 37 cm, length: 55 cm, Propeller: 18 cm, https://www.youngusa.com/product/wind-monitor/

New version by Baptiste:
- Now the y value of the selected pixel is saved directly in a dataframe as we click
- The value that is prompted to click is diplayed in the shell
- You then need to click on the target and press space key
- once the 16 items clicked in the image, all the y values are being saved in df
- you can now loop through all the images contained in a folder

"""
# %matplotlib qt

import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import cv2 # OpenCV

path_to_photos = '../GCNET_photos_availability/photo_archive_of_GC-Net_AWS/'
cv2.destroyAllWindows()

def digitize_image(img_filename = 'CP1 1998 Pre J Box-2'):
    df = pd.DataFrame()
    df['site'] = [img_filename.split(' ')[0]]
    df['year'] = int(img_filename.split(' ')[1])
    df['filename'] = img_filename
    
    cols =  ['profile_lower_y', 'profile_upper_y', 'bottom_of_sonic_1',
                   'ground_under_sonic1', 'bottom_of_sonic_2', 'ground_under_sonic2',
                   'Wz1', 'ground_under_wind_1', 'Wz2', 'ground_under_wind_2',
                   'THz1', 'ground_under_TH_1', 'THz2', 'ground_under_TH_2',
                   'bottom_of_wind_sensor', 'top_of_wind_sensor_body']
    
    img=cv2.imread(path_to_photos+img_filename, 0)
    cv2.namedWindow(img_filename, cv2.WINDOW_NORMAL) # need this to be able to resize image to fit to screen
    cv2.imshow(img_filename, img)
    global ix,iy 
    ix,iy = -1,-1 
    # function to display the coordinates of the points clicked on the image   
    def click_event(event, x, y, flags, param):
        global ix, iy
        # checking for left mouse clicks
        if event == cv2.EVENT_LBUTTONDOWN:
            # displaying the coordinates on the Shell
            # print(x, ' ', y)
            # displaying the coordinates on the image window
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(x) + ',' +
                        str(y), (x,y), font,
                        0.5, (255, 0, 0), 1)
            cv2.imshow(img_filename, img)
            param=1
            ix,iy = x, y
    
    cv2.setMouseCallback(img_filename, click_event)
    i = 0
    
    print(cols[i])
    # click then press space key to save
    while True:
        k = cv2.waitKey(0)   
        if k == 32:
            print(ix,iy)
            df[cols[i]] = iy
            i=i+1
        if (k == 27)|(i == 16):
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            break
        else:
            print(cols[i])
    # scaling image
    wind_sensor_dz=0.277 # meters
    
    df['image_scale']=(df.bottom_of_wind_sensor - df.top_of_wind_sensor_body)/wind_sensor_dz
    df['SH1'] = (df.ground_under_sonic1 - df.bottom_of_sonic_1) / df.image_scale
    df['SH2'] = (df.ground_under_sonic2 - df.bottom_of_sonic_2) / df.image_scale
    df['Wz1'] = (df.ground_under_wind_1 - df.Wz1)/df.image_scale
    df['Wz2'] = (df.ground_under_wind_2 - df.Wz2)/df.image_scale
    df['THz1'] = (df.ground_under_TH_1 - df.THz1)/df.image_scale
    df['THz2'] = (df.ground_under_TH_2 - df.THz2)/df.image_scale
    df['month'] = img_filename[9:11]
    df['day'] = img_filename[12:14]
    return df

# %% Looping through the pictures in a folder
import os
ix,iy = -1,-1 
image_list = os.listdir(path_to_photos)
for img_name in image_list[:1]:
    tmp = digitize_image(img_name)
    if img_name == image_list[0]:
        df_all = tmp.copy()
    else:
        df_all = df_all.append(tmp)
from datetime import datetime
# saving to csv
df_all.to_csv('./output/'+datetime.now().strftime("%Y%m%dT%H%M%S")+'_instrument_height.csv')

