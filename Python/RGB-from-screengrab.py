from PIL import ImageGrab
import numpy as np
import cv2
import tkinter as tk
import utils

root = tk.Tk()
screen_width = root.winfo_screenwidth() - 1
screen_height = root.winfo_screenheight() - 1

inputdimx = 300
inputdimy = 300

while True: #gets the previous frames rgbavg values.
    red1 = []
    green1 = []
    blue1 = []
    frame_babel = ImageGrab.grab(bbox=(0, 0, inputdimx, inputdimy))
    frame_array = np.array(frame_babel)
    frame = cv2.cvtColor(frame_array, cv2.COLOR_BGR2RGB)
 
    for y1 in range(0, inputdimy): #First first third of the height
        for x1 in range(0, (inputdimx/3 * 1)): #Second first third of the width
            rgb1 = frame[y1, x1]
            red1.append(rgb1[0])
            green1.append(rgb1[1])
            blue1.append(rgb1[2])

    redavg1 = int(utils.average(red1))
    greenavg1 = int(utils.average(green1))
    blueavg1 = int(utils.average(blue1))
    rgbavg1 = [redavg1, greenavg1, blueavg1]

    for y1 in range(0, inputdimy): #Second first third of the height.
        for x2 in range(((inputdimx/3)*1), (inputdimx/3 * 2)): #Second first third of the width
            rgb2 = frame[y1, x2]
            red2.append(rgb2[0])
            green2.append(rgb2[1])
            blue2.append(rgb2[2])

    redavg2 = int(utils.average(red2))
    greenavg2 = int(utils.average(green2))
    blueavg2 = int(utils.average(blue2))
    rgbavg2 = [redavg2, greenavg2, blueavg2]

    for y1 in range(0, inputdimy): #Second first third of the height.
        for x3 in range(((inputdimx/3) * 2), (inputdimx/3 * 3)): #Second first third of the width
            rgb3 = frame[y3, x3]
            red3.append(rgb3[0])
            green3.append(rgb3[1])
            blue3.append(rgb3[2])

    redavg3 = int(utils.average(red3))
    greenavg3 = int(utils.average(green3))
    blueavg3 = int(utils.average(blue3))
    rgbavg3 = [redavg3, greenavg3, blueavg3]

    section = []
    section.append(rgbavg1)
    section.append(rgbavg2)
    section.append(rgbavg3)
    
    print(section)


# Gjennomsnitts verdier i soner. 

#if frame[y, x].all() == frame[y, x-1].all():  #Remove consecutive duplicate indexes.


#print (f'red = {red}  green = {green}  blue = {blue}')


# Caculate average RGB from each ImageGrab
#histogram