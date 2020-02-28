from PIL import ImageGrab
import numpy as np
import cv2
import tkinter as tk
import utils

root = tk.Tk()
screen_width = root.winfo_screenwidth() - 1
screen_height = root.winfo_screenheight() - 1

while True: #gets the previous frames rgbavg values.
    red = []
    green = []
    blue = []
    frame_babel = ImageGrab.grab()
    frame_array = np.array(frame_babel)
    frame = cv2.cvtColor(frame_array, cv2.COLOR_BGR2RGB)
 
    for y in range(0, screen_height):
        for x in range(0, screen_width):
            rgb = frame[y, x]
            red.append(rgb[0])
            green.append(rgb[1])
            blue.append(rgb[2])

    redavg = int(utils.average(red))
    greenavg = int(utils.average(green))
    blueavg = int(utils.average(blue))
    rgbavg = [redavg, greenavg, blueavg]
    if rgbavg == 

    print()



# Gjennomsnitts verdier i soner. 

#if frame[y, x].all() == frame[y, x-1].all():  #Remove consecutive duplicate indexes.


#print (f'red = {red}  green = {green}  blue = {blue}')


# Caculate average RGB from each ImageGrab
#histogram