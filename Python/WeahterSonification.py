from PIL import ImageGrab
import numpy as np
import cv2
import tkinter as tk
import utils

#specify smaller screen dim. Add the variables to ImageGrab like so: "ImageGrab.grab(bbox=(0, 0, inputdimx, inputdimy))"
inputdimx = 300
inputdimy = 300

while True:
    screen = ImageGrab.grab()
    frame_array = np.array(screen)
    frame = frame_array[:,:,:3] #Removes Alpha from RGBA frame array

    first_section_rgb_avg = utils.screensplit_rgb_avg(frame, 1)
    first_section_color_temp = utils.rgb2colortemp(first_section_rgb_avg)
    #print(f'rgb-avg section 1 = {first_section_rgb_avg}')
    #print(f'colortemp section 1= {first_section_color_temp}')

    second_section_rgb_avg = utils.screensplit_rgb_avg(frame, 2)
    second_section_color_temp = utils.rgb2colortemp(second_section_rgb_avg)
    #print(f'rgb-avg section 2 = {second_section_rgb_avg}')
    #print(f'colortemp section 2 = {second_section_color_temp}')

    third_section_rgb_avg = utils.screensplit_rgb_avg(frame, 3)
    third_section_color_temp = utils.rgb2colortemp(third_section_rgb_avg)
    #print(f'rgb-avg section 3 = {third_section_rgb_avg}')
    #print(f'colortemp section 3 = {third_section_color_temp}')

    colortemp_array = np.array((first_section_color_temp, second_section_color_temp, third_section_color_temp))
    print(colortemp_array)



