from PIL import ImageGrab
import numpy as np
import cv2
import tkinter as tk
import utils

#specify smaller screen dim. Add the variables to ImageGrab like so: "ImageGrab.grab(bbox=(0, 0, inputdimx, inputdimy))"
inputdimx = 300
inputdimy = 300

while True:
    frame_babel = ImageGrab.grab()
    frame_array = np.array(frame_babel)
    frame = frame_array[:,:,:3] #Removes Alpha from RGBA
    #print(frame[0])
    #break

    #first_row_rgb_avg = utils.screensplit_rgb_avg(frame, 1)
    #print(f'rgb-avg row 1 = {first_row_rgb_avg}')
    #print(f'colortemp = {utils.rgb2colortemp(first_row_rgb_avg)}')

    second_row_rgb_avg = utils.screensplit_rgb_avg(frame, 2)
    print(f'rgb-avg row 2 = {second_row_rgb_avg}')
    print(f'colortemp = {utils.rgb2colortemp(second_row_rgb_avg)}')

    #third_row_rgb_avg = utils.screensplit_rgb_avg(frame, 3)
    #print(f'rgb-avg row 3 = {third_row_rgb_avg}')
    #print(f'colortemp = {utils.rgb2colortemp(third_row_rgb_avg)}')
