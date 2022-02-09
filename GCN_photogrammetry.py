#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 07:39:56 2022

@author: jason

YOUNG Model 05103 Wind Monitor height: 37 cm, length: 55 cm, Propeller: 18 cm, https://www.youngusa.com/product/wind-monitor/

info on height adjustments from aws_qc.pro
; -------------------------------------------------------- Begin ADJUST Z

if (stnum(jx) eq '01') then begin
  for i=0,nlines-1 do begin
    if ((year eq 1997) and (d2(2,i) ge 141.9583))then begin
      temp=0.
	temp=d2(18,i)
	d2(18,i)=d2(17,i)
	d2(17,i)=temp
    endif
  endfor
    adjust_z,d2,nlines,18,18,2001,1,2.372
    adjust_z,d2,nlines,17,17,2001,1,1.172

   plotpair,ppp,nlines,varname,stnames,layot,plot_prompt,d2,icol,fcol,jx,yr
endif

if (stnum(jx) eq '02') then begin

  if year eq '1997' then begin
    for i=0,nlines-1 do begin
      if i ge 7378 then begin
        if d2(17,i) ne 999. then d2(17,i)=d2(17,7378)-d2(17,i)+1.7
        if d2(18,i) ne 999. then d2(18,i)=d2(18,7378)-d2(18,i)+2.7
      endif
    endfor
  adjust_z,d2,nlines,icol,icol,1997,309.2917,-0.85
  endif ; 1997

    adjust_z,d2,nlines,17,18,1997,133.375,1.9
    adjust_z,d2,nlines,17,17,1998,151.7083,-2.3
    adjust_z,d2,nlines,17,17,1999,1,-1.6
    adjust_z,d2,nlines,17,18,1999,1,4.8
    adjust_z,d2,nlines,17,17,2000,1,0.7539
    adjust_z,d2,nlines,18,18,2000,1,1.546
    adjust_z,d2,nlines,17,18,2001,148.,2.2

plotpair,ppp,nlines,varname,stnames,layot,plot_prompt,d2,icol,fcol,jx,yr

endif

if (stnum(jx) eq '03') then begin
  adjust_z,d2,nlines,17,17,1997,139.8333,-0.5
  adjust_z,d2,nlines,18,18,1997,139.8333,0.25
  adjust_z,d2,nlines,17,17,1998,1.,-0.5
  adjust_z,d2,nlines,18,18,1998,1.,0.25
  adjust_z,d2,nlines,17,17,1999,133.6667,2.8
  adjust_z,d2,nlines,18,18,1999,133.6667,2.67
  adjust_z,d2,nlines,18,18,1999,1.,0.48
  adjust_z,d2,nlines,17,17,2000,1.,2.29
  adjust_z,d2,nlines,18,18,2000,1.,2.8774
endif

if (stnum(jx) eq '04') then begin
  adjust_z,d2,nlines,17,17,1997,137.4583,2.
  adjust_z,d2,nlines,18,18,1997,137.4583,2.5
  adjust_z,d2,nlines,17,17,1999,1,6.45
  adjust_z,d2,nlines,18,18,1999,1,7.25
  adjust_z,d2,nlines,17,17,2000,1,0.6721
  adjust_z,d2,nlines,18,18,2000,1,1.5192
endif

if (stnum(jx) eq '06') then begin
  adjust_z,d2,nlines,17,17,1998,136.5417,+0.37
  adjust_z,d2,nlines,18,18,1998,136.5417,-0.4
  adjust_z,d2,nlines,17,17,1999,130.625,1.22
  adjust_z,d2,nlines,17,17,1999,1,0.55
  adjust_z,d2,nlines,18,18,1999,130.625,2.38
  adjust_z,d2,nlines,17,18,2001,161.666,2.26
endif

if (stnum(jx) eq '07') then begin
  adjust_z,d2,nlines,17,18,1998,139.0000,0.3
  adjust_z,d2,nlines,17,17,1999,1,0.359
  adjust_z,d2,nlines,18,18,1999,1,0.4719
  adjust_z,d2,nlines,17,18,2000,1,0.27
  adjust_z,d2,nlines,17,18,2001,1,0.26
  adjust_z,d2,nlines,17,17,2001,159.7917,2.15
  adjust_z,d2,nlines,18,18,2001,159.7917,2.45
endif

if (stnum(jx) eq '08') then begin
  adjust_z,d2,nlines,17,17,1998,118.8750,0.95
  adjust_z,d2,nlines,18,18,1998,118.8750,2.25
  adjust_z,d2,nlines,17,17,1999,1.,0.95
  adjust_z,d2,nlines,18,18,1999,1.,2.25
  adjust_z,d2,nlines,17,17,2000,1.,1.022
  adjust_z,d2,nlines,18,18,2000,1.,2.1993
  adjust_z,d2,nlines,icol,fcol,2000,134.,2.4
  adjust_z,d2,nlines,icol,fcol,2003,129.8333,2.3
endif

if (stnum(jx) eq '09') then begin
  adjust_z,d2,nlines,17,17,1998,146.5833,-.85
  adjust_z,d2,nlines,17,17,1999,151.9167,-1.77
  adjust_z,d2,nlines,17,17,1999,1,-.85
  adjust_z,d2,nlines,18,18,1999,151.9167,-2.58
  adjust_z,d2,nlines,17,17,2000,1,2.55
  adjust_z,d2,nlines,18,18,2000,1,2.75
  adjust_z,d2,nlines,17,17,2002,130.9167,-1.63
  adjust_z,d2,nlines,18,18,2002,130.9167,-1.708
endif

if (stnum(jx) eq '10') then begin
  adjust_z,d2,nlines,17,17,1998,107.5833,0.45
  adjust_z,d2,nlines,17,17,1999,1,0.45
  adjust_z,d2,nlines,17,17,1999,105.667,2.15
  adjust_z,d2,nlines,18,18,1999,105.667,2.85
  adjust_z,d2,nlines,17,17,2000,1,2.55
  adjust_z,d2,nlines,18,18,2000,1,2.75
 ; adjust_z,d2,nlines,17,17,2001,1,2.4134
 ; adjust_z,d2,nlines,18,18,2001,1,2.7481
  adjust_z,d2,nlines,17,18,2001,156.625,2.35
 ; adjust_z,d2,nlines,17,17,2003,125,1.


endif

if (stnum(jx) eq '11') then begin
  adjust_z,d2,nlines,17,17,1998,108.,2.45
  adjust_z,d2,nlines,18,18,1998,108.,2.45
  adjust_z,d2,nlines,17,18,1999,1.,2.446
  adjust_z,d2,nlines,17,17,1999,112.9167,1.6
  adjust_z,d2,nlines,18,18,1999,112.9167,2.6
  adjust_z,d2,nlines,17,18,2001,158.4167,2.9
endif

if (stnum(jx) eq '13') then begin
  adjust_z,d2,nlines,17,18,1998,152.,1.12
  ;adjust_z,d2,nlines,18,18,1998,152.,1.12
  adjust_z,d2,nlines,17,17,1999,1.,0.84
  adjust_z,d2,nlines,18,18,1999,1.,1.147
  adjust_z,d2,nlines,17,17,1999,160.25,1.15
  adjust_z,d2,nlines,17,17,1999,148.,0.8
  adjust_z,d2,nlines,18,18,1999,148.,2.
  adjust_z,d2,nlines,17,17,2000,155.75,2.464
  adjust_z,d2,nlines,18,18,2000,155.75,1.7
  adjust_z,d2,nlines,18,18,2000,155.75,1.7
endif

if (stnum(jx) eq '14') then begin
  adjust_z,d2,nlines,17,17,1999,170.5,.30
  adjust_z,d2,nlines,17,17,2000,167.8,2.7
  adjust_z,d2,nlines,18,18,2000,167.8,2.7

endif

if (stnum(jx) eq '15') then begin
  adjust_z,d2,nlines,17,17,1999,111.875,1.58
  adjust_z,d2,nlines,17,17,2000,1.,1.62
  adjust_z,d2,nlines,17,18,2000,137.7083,3.012
  adjust_z,d2,nlines,17,17,2003,130.7083,2.86
  adjust_z,d2,nlines,18,18,2003,130.7083,2.92
endif

if (stnum(jx) eq '17') then begin
  adjust_z,d2,nlines,17,17,2000,148.0417,-2.1
  adjust_z,d2,nlines,17,17,2001,142.0833,-2.31
  adjust_z,d2,nlines,17,17,2002,127.6667,-2.84
  adjust_z,d2,nlines,17,17,2003,121.75,-2.79
endif

if (stnum(jx) eq '19') then begin
  adjust_z,d2,nlines,17,17,2001,140.1667,-2.817
  adjust_z,d2,nlines,17,17,2002,126.25,-2.43

endif

if (stnum(jx) eq '20') then begin
  adjust_z,d2,nlines,17,17,2000,148.0417,0.52
endif
if (stnum(jx) eq '26') then begin
  adjust_z,d2,nlines,17,18,2003,126.7083,-1.05
endif
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
if os.getlogin() == 'Maiken':
    base_path = '/Users/Maiken/OneDrive/PUK/GCNet_photogrammetry/'
elif os.getlogin() == 'jason':
    base_path = '/Users/jason/Dropbox/GCNet_photogrammetry/'

os.system('ls -lF '+base_path)

#%% close the window
cv2.destroyAllWindows()

#%%
#img_filename='DY2 1996 05 28a J Box'
#img_filename='DY2 1997 04 18a J Box'
#img_filename='DY2 1998 04 27b pre2 J Box'
#img_filename='DY2 1998 04 27a pre1 J Box' # Maiken pls do this one - DONE
#img_filename='DY2 1998 04 29b post J Box'
#img_filename='DY2 1998 04 29a post J Box' # Maiken pls do this one - DONE
#img_filename='DY2 2006 05 07a pre'
#img_filename='DY2 2006 05 07a post'
#img_filename='DY2 2006 05 07b pre' # Maiken pls redo DY2 2006 05 07a and b pre and compare if you get similar results. If the results are very different, ideas why? - DONE
#img_filename='DY2 2006 05 07b post' # Maiken pls do this one - DONE
#img_filename='DY2 2007 04 25a' # Maiken pls do this one - DONE
#img_filename='DY2 2007 04 25b' # Maiken pls do this one - DONE
#img_filename='DY2 2007 04 25c' # Maiken pls do this one - DONE
#img_filename='DY2 2007 04 25d' # Maiken pls do this one - DONE
#img_filename='DY2 2008 05 03a' # Maiken pls do this one - DONE
#img_filename='DY2 2008 05 03b' # Maiken pls do this one - DONE
img_filename='DY2 2008 05 03c' # Maiken pls do this one - DONE

do_image=1

if do_image:
    img=cv2.imread(base_path+'/img/'+img_filename+'.jpg', 0)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL) # need this to be able to resize image to fit to screen
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
            #cv2.imshow('image', imS)
     
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
            #cv2.imshow('image', imS)
            # return(x,y)
    
    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)
    cv2.waitKey(0)   # pop-up window doesnt respond, trying this

# # %% image scale
wind_sensor_dz=0.277 # meters

if img_filename=='DY2 1996 05 28a J Box':
    profile_lower_y=1517 ; profile_upper_y=1109 # to check profile dz
    bottom_of_sonic_1=1230 ; ground_under_sonic1=1995
    bottom_of_sonic_2=1167 ; ground_under_sonic2=1933
    Wz1=1410 ; ground_under_wind_1=2030
    Wz2=974 ; ground_under_wind_2=ground_under_wind_1
    THz1=1401 ; ground_under_TH_1=2050
    THz2=989 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1053 ; top_of_wind_sensor_body=974 

if img_filename=='DY2 1997 04 18a J Box':
    profile_lower_y=2384 ; profile_upper_y=1889 # to check profile dz
    bottom_of_sonic_1=2015 ; ground_under_sonic1=2553
    bottom_of_sonic_2=1905 ; ground_under_sonic2=2498
    Wz1=2232 ; ground_under_wind_1=2672
    Wz2=1733 ; ground_under_wind_2=ground_under_wind_1
    THz1=2238 ; ground_under_TH_1=2669
    THz2=1755 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1825 ; top_of_wind_sensor_body=1735 

# if img_filename=='DY2 1998 04 27a pre1 J Box': #template
#     profile_lower_y=0 ; profile_upper_y=0 # to check profile dz
#     bottom_of_sonic_1=0 ; ground_under_sonic1=0
#     bottom_of_sonic_2=0 ; ground_under_sonic2=0
#     Wz1=0 ; ground_under_wind_1=0
#     Wz2=0 ; ground_under_wind_2=ground_under_wind_1
#     THz1=0 ; ground_under_TH_1=0
#     THz2=0 ; ground_under_TH_2=ground_under_TH_1
#     bottom_of_wind_sensor=0 ; top_of_wind_sensor_body=0 
    
if img_filename=='DY2 1998 04 27a pre1 J Box': 
    profile_lower_y=1845 ; profile_upper_y=1339 # to check profile dz
    bottom_of_sonic_1=1506 ; ground_under_sonic1=1974
    bottom_of_sonic_2=1328 ; ground_under_sonic2=2248
    Wz1=1624 ; ground_under_wind_1=1942
    Wz2=1145 ; ground_under_wind_2=ground_under_wind_1
    THz1=1657 ; ground_under_TH_1=2006
    THz2=1145 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1242 ; top_of_wind_sensor_body=1135 

if img_filename=='DY2 1998 04 27b pre2 J Box':
    profile_lower_y=2129 ; profile_upper_y=1505 # to check profile dz
    bottom_of_sonic_1=1635 ; ground_under_sonic1=1979
    bottom_of_sonic_2=1455 ; ground_under_sonic2=1916
    Wz1=1933 ; ground_under_wind_1=2253
    Wz2=1253 ; ground_under_wind_2=ground_under_wind_1
    THz1=1908 ; ground_under_TH_1=2229
    THz2=1266 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1398 ; top_of_wind_sensor_body=1241 
    
if img_filename=='DY2 1998 04 29a post J Box':
    profile_lower_y=1261 ; profile_upper_y=950 # to check profile dz
    bottom_of_sonic_1=1065 ; ground_under_sonic1=1543
    bottom_of_sonic_2=585 ; ground_under_sonic2=1667
    Wz1=1132 ; ground_under_wind_1=1672
    Wz2=818 ; ground_under_wind_2=ground_under_wind_1
    THz1=1149 ; ground_under_TH_1=1535
    THz2=845 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1202 ; top_of_wind_sensor_body=1127 

if img_filename=='DY2 1998 04 29b post J Box':
    profile_lower_y=1095 ; profile_upper_y=870 # to check profile dz
    bottom_of_sonic_1=943 ; ground_under_sonic1=1358
    bottom_of_sonic_2=637 ; ground_under_sonic2=1297
    Wz1=1010 ; ground_under_wind_1=1357
    Wz2=781 ; ground_under_wind_2=ground_under_wind_1
    THz1=1013 ; ground_under_TH_1=1334
    THz2=783 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1061 ; top_of_wind_sensor_body=1004

# if img_filename=='DY2 2006 05 07a pre': # Jasons numbers
#     profile_lower_y=1579 ; profile_upper_y=1164 # to check profile dz
#     bottom_of_sonic_1=1297 ; ground_under_sonic1=1635
#     bottom_of_sonic_2=1120 ; ground_under_sonic2=1560
#     Wz1=1460 ; ground_under_wind_1=1819
#     Wz2=987 ; ground_under_wind_2=ground_under_wind_1
#     THz1=1435 ; ground_under_TH_1=1708
#     THz2=1039 ; ground_under_TH_2=ground_under_TH_1
#     bottom_of_wind_sensor=1089 ; top_of_wind_sensor_body=975

if img_filename=='DY2 2006 05 07a pre': # Maikens numbers
    profile_lower_y=1578 ; profile_upper_y=1159 # to check profile dz
    bottom_of_sonic_1=1288 ; ground_under_sonic1=1651
    bottom_of_sonic_2=1116 ; ground_under_sonic2=1596
    Wz1=1460 ; ground_under_wind_1=1811
    Wz2=981 ; ground_under_wind_2=ground_under_wind_1
    THz1=1433 ; ground_under_TH_1=1708
    THz2=1032 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1086 ; top_of_wind_sensor_body=984 
    
if img_filename=='DY2 2006 05 07a post': # Jasons numbers
    profile_lower_y=811 ; profile_upper_y=550 # to check profile dz
    bottom_of_sonic_1=643 ; ground_under_sonic1=1653
    bottom_of_sonic_2=449 ; ground_under_sonic2=1645
    Wz1=724 ; ground_under_wind_1=1635
    Wz2=460 ; ground_under_wind_2=ground_under_wind_1
    THz1=730 ; ground_under_TH_1=1653
    THz2=472 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=783 ; top_of_wind_sensor_body=716

# if img_filename=='DY2 2006 05 07a post': # Maikens numbers
#     profile_lower_y=810 ; profile_upper_y=549 # to check profile dz
#     bottom_of_sonic_1=637 ; ground_under_sonic1=1560
#     bottom_of_sonic_2=448 ; ground_under_sonic2=1693
#     Wz1=722 ; ground_under_wind_1=1685
#     Wz2=458 ; ground_under_wind_2=ground_under_wind_1
#     THz1=728 ; ground_under_TH_1=1667
#     THz2=469 ; ground_under_TH_2=ground_under_TH_1
#     bottom_of_wind_sensor=781 ; top_of_wind_sensor_body=714 
    
if img_filename=='DY2 2006 05 07b pre': # Jasons numbers
    profile_lower_y=1642 ; profile_upper_y=1180 # to check profile dz
    bottom_of_sonic_1=1358 ; ground_under_sonic1=1846
    bottom_of_sonic_2=1139 ; ground_under_sonic2=1989
    Wz1=1458 ; ground_under_wind_1=1888
    Wz2=990 ; ground_under_wind_2=ground_under_wind_1
    THz1=1487 ; ground_under_TH_1=1876
    THz2=1044 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1092 ; top_of_wind_sensor_body=977
    
# if img_filename=='DY2 2006 05 07b pre': # Maikens numbers
#     profile_lower_y=1635 ; profile_upper_y=1175 # to check profile dz
#     bottom_of_sonic_1=1352 ; ground_under_sonic1=1926
#     bottom_of_sonic_2=1129 ; ground_under_sonic2=1982
#     Wz1=1458 ; ground_under_wind_1=1859
#     Wz2=991 ; ground_under_wind_2=ground_under_wind_1
#     THz1=1487 ; ground_under_TH_1=1859
#     THz2=1041 ; ground_under_TH_2=ground_under_TH_1
#     bottom_of_wind_sensor=1076 ; top_of_wind_sensor_body=977 

if img_filename=='DY2 2006 05 07b post': # One of the sonics is missing
    profile_lower_y=937 ; profile_upper_y=703 # to check profile dz
    bottom_of_sonic_1=852 ; ground_under_sonic1=1553
    bottom_of_sonic_2=math.nan ; ground_under_sonic2=math.nan
    Wz1=791 ; ground_under_wind_1=1655
    Wz2=533 ; ground_under_wind_2=ground_under_wind_1
    THz1=885 ; ground_under_TH_1=1567
    THz2=668 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=849 ; top_of_wind_sensor_body=791 
    
if img_filename=='DY2 2007 04 25a': # One of the sonics is missing
    profile_lower_y=716 ; profile_upper_y=519 # to check profile dz
    bottom_of_sonic_1=601 ; ground_under_sonic1=1115
    bottom_of_sonic_2=math.nan ; ground_under_sonic2=math.nan
    Wz1=623 ; ground_under_wind_1=1211
    Wz2=409 ; ground_under_wind_2=ground_under_wind_1
    THz1=652 ; ground_under_TH_1=1143
    THz2=467 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=670 ; top_of_wind_sensor_body=621
    
if img_filename=='DY2 2007 04 25b': 
    profile_lower_y=1047 ; profile_upper_y=745 # to check profile dz
    bottom_of_sonic_1=810 ; ground_under_sonic1=1895
    bottom_of_sonic_2=745 ; ground_under_sonic2=1744
    Wz1=930 ; ground_under_wind_1=1753
    Wz2=634 ; ground_under_wind_2=ground_under_wind_1
    THz1=933 ; ground_under_TH_1=1830
    THz2=625 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=998 ; top_of_wind_sensor_body=936 
    
if img_filename=='DY2 2007 04 25c':
    profile_lower_y=981 ; profile_upper_y=731 # to check profile dz
    bottom_of_sonic_1=797 ; ground_under_sonic1=1669
    bottom_of_sonic_2=740 ; ground_under_sonic2=1480
    Wz1=883 ; ground_under_wind_1=1607
    Wz2=623 ; ground_under_wind_2=ground_under_wind_1
    THz1=886 ; ground_under_TH_1=1618
    THz2=639 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=946 ; top_of_wind_sensor_body=883 
    
if img_filename=='DY2 2007 04 25d':
    profile_lower_y=1068 ; profile_upper_y=770 # to check profile dz
    bottom_of_sonic_1=763 ; ground_under_sonic1=1971
    bottom_of_sonic_2=592 ; ground_under_sonic2=2013
    Wz1=987 ; ground_under_wind_1=1757
    Wz2=689 ; ground_under_wind_2=ground_under_wind_1
    THz1=935 ; ground_under_TH_1=1864
    THz2=582 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1048 ; top_of_wind_sensor_body=983 
    
if img_filename=='DY2 2008 05 03a': # This one is difficult, probably inaccurate
    profile_lower_y=1627 ; profile_upper_y=1022 # to check profile dz
    bottom_of_sonic_1=1185 ; ground_under_sonic1=2426
    bottom_of_sonic_2=1387 ; ground_under_sonic2=2276
    Wz1=1391 ; ground_under_wind_1=2632
    Wz2=876 ; ground_under_wind_2=ground_under_wind_1
    THz1=1499 ; ground_under_TH_1=2203
    THz2=1065 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1507 ; top_of_wind_sensor_body=1387 
    
if img_filename=='DY2 2008 05 03b':
    profile_lower_y=1645 ; profile_upper_y=1192 # to check profile dz
    bottom_of_sonic_1=1385 ; ground_under_sonic1=2526
    bottom_of_sonic_2=1231 ; ground_under_sonic2=2757
    Wz1=1449 ; ground_under_wind_1=2710
    Wz2=936 ; ground_under_wind_2=ground_under_wind_1
    THz1=1509 ; ground_under_TH_1=2492
    THz2=1073 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1560 ; top_of_wind_sensor_body=1436 
    
if img_filename=='DY2 2008 05 03c': # very difficult to see TH instruments
    profile_lower_y=1718 ; profile_upper_y=1253 # to check profile dz
    bottom_of_sonic_1=1508 ; ground_under_sonic1=2591
    bottom_of_sonic_2=1271 ; ground_under_sonic2=2658
    Wz1=1450 ; ground_under_wind_1=2743
    Wz2=922 ; ground_under_wind_2=ground_under_wind_1
    THz1=1602 ; ground_under_TH_1=2417
    THz2=1199 ; ground_under_TH_2=ground_under_TH_1
    bottom_of_wind_sensor=1571 ; top_of_wind_sensor_body=1445 


image_scale=(bottom_of_wind_sensor-top_of_wind_sensor_body)/wind_sensor_dz # pixels per m
print("image_scale = {:.0f}".format(image_scale)+' pixels per m')

profile_dz=(profile_lower_y-profile_upper_y)/image_scale # pixels per m
print("profile_dz = {:.3f}".format(profile_dz)+' m')

SH1=(ground_under_sonic1-bottom_of_sonic_1)/image_scale # pixels per m
print("distancez_to_ground_sonic_1 = {:.3f}".format(SH1)+' m')

SH2=(ground_under_sonic2-bottom_of_sonic_2)/image_scale # pixels per m
print("distancez_to_ground_sonic_2 = {:.3f}".format(SH2)+' m')

Wz1=(ground_under_wind_1-Wz1)/image_scale # pixels per m
print("wind 1 z = {:.3f}".format(Wz1)+' m')

Wz2=(ground_under_wind_2-Wz2)/image_scale # pixels per m
print("wind 2 z = {:.3f}".format(Wz2)+' m')

print("wind dz = {:.3f}".format(Wz2-Wz1)+' m, should equal '+"profile_dz = {:.3f}".format(profile_dz)+' m')

ErrorW=abs((Wz2-Wz1)-profile_dz)
print("ErrorW= {:.3f}".format(ErrorW)+" m")

THz1=(ground_under_TH_1-THz1)/image_scale # pixels per m
print("TH 1 z = {:.3f}".format(THz1)+' m')

THz2=(ground_under_TH_2-THz2)/image_scale # pixels per m
print("TH 2 z = {:.3f}".format(THz2)+' m')

print("TH dz = {:.3f}".format(THz2-THz1)+' m, should equal '+"profile_dz = {:.3f}".format(profile_dz)+' m')

ErrorTH=abs((THz2-THz1)-profile_dz)
print("ErrorTH= {:.3f}".format(ErrorTH)+" m")

site=img_filename[0:3]
year=img_filename[4:8]
month=img_filename[9:11]
day=img_filename[12:14]
abc=img_filename[14:]
abc=abc.replace(' J Box','')
abc=abc.replace(' via D Houtz','')

df2 = pd.DataFrame(columns = ['site', 'year','month','day','abc','SH1','SH2','Wz1','Wz2','THz1','THz2','ErrorW','ErrorTH']) 
# df2.index.name = 'index'
df2["site"]=pd.Series(site)
df2["year"]=pd.Series(year)
df2["month"]=pd.Series(month)
df2["day"]=pd.Series(day)
df2["abc"]=pd.Series(abc)
df2["SH1"]=pd.Series(SH1)
df2["SH2"]=pd.Series(SH2)
df2["Wz1"]=pd.Series(Wz1)
df2["Wz2"]=pd.Series(Wz2)
df2["THz1"]=pd.Series(THz1)
df2["THz2"]=pd.Series(THz2)
df2["ErrorW"]=pd.Series(ErrorW)
df2["ErrorTH"]=pd.Series(ErrorTH)

# df2 = df2.loc[:, ~df2.columns.str.contains('^Unnamed')]
# -------------------------------- chdir
if os.getlogin() == 'Maiken':
    ofile = '/Users/Maiken/OneDrive/PUK/GCNet_photogrammetry/output/'+site+'_'+year+'_'+month+'_'+day+abc+'.csv'
elif os.getlogin() == 'jason':
    ofile='/Users/jason/Dropbox/GCNet_photogrammetry/output/'+site+'_'+year+'_'+month+'_'+day+abc+'.csv'
df2.to_csv(ofile,index=None, float_format="%.3f")

#%% close the window
cv2.destroyAllWindows()


#%%

 
# driver function
# if __name__=="__main__":
 
#     # reading the image
#     img = cv2.imread('lena', 1)
 
#     # displaying the image
#     cv2.imshow('image', img)
 
#     # setting mouse handler for the image
#     # and calling the click_event() function
#     cv2.setMouseCallback('image', click_event)
 
#     # wait for a key to be pressed to exit
#     cv2.waitKey(0)
 
#     # close the window
#     cv2.destroyAllWindows()
