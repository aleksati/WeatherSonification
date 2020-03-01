from PIL import ImageGrab
#import matplotlib.pyplot as plt
import numpy as np
import cv2
import tkinter as tk
import utils

# Specify smaller screen dim. If so, add the variables to ImageGrab: "ImageGrab.grab(bbox=(0, 0, inputdimx, inputdimy))"
inputdimx = 300
inputdimy = 300

while True:

    # Grayscale histogram. outputs 255 numbers which correspond to the X axis, the value of every number corresponds to the Y axis.
    screen = ImageGrab.grab()
    r, g, b, a = screen.split() 
    len(r.histogram())
    histlist = r.histogram()
    N = 6 # Specify how many of the largest Y-values in the histogram to extract 
    #print(f'histogram = {histlist}')
    histlist_highvalues_indices = utils.Nmaxoflist(histlist, N)

    print(f' the {N} largest Y-values in the histogram are located here: {histlist_highvalues_indices} on the x-axis.')

    # Calculate average RGB values for 9 screen sections. From top left to bottom right. 
    screen_rgba_array = np.array(screen)
    screen_rgb_array = screen_rgba_array[:,:,:3] # Removes Alpha from RGBA frame array

    first_section_rgb_avg = utils.screensplit_rgb_avg(screen_rgb_array, 1)
    first_section_color_temp = utils.rgb2colortemp(first_section_rgb_avg)
    #print(f'rgb-avg section 1 = {first_section_rgb_avg}')
    #print(f'colortemp section 1= {first_section_color_temp}')

    second_section_rgb_avg = utils.screensplit_rgb_avg(screen_rgb_array, 2)
    second_section_color_temp = utils.rgb2colortemp(second_section_rgb_avg)
    #print(f'rgb-avg section 2 = {second_section_rgb_avg}')
    #print(f'colortemp section 2 = {second_section_color_temp}')

    third_section_rgb_avg = utils.screensplit_rgb_avg(screen_rgb_array, 3)
    third_section_color_temp = utils.rgb2colortemp(third_section_rgb_avg)
    #print(f'rgb-avg section 3 = {third_section_rgb_avg}')
    #print(f'colortemp section 3 = {third_section_color_temp}')

    #Generates array of screen color temp. low values = warm colors, high values = cold colors.
    colortemp_array = np.array((first_section_color_temp, second_section_color_temp, third_section_color_temp))
    print(colortemp_array)

    colortemp_list = first_section_color_temp + second_section_color_temp + third_section_color_temp
    #print(f'colortemp screen {colortemp_list}')



