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



while True:
    frame_babel = ImageGrab.grab(bbox=(0, 0, inputdimx, inputdimy))
    frame_array = np.array(frame_babel)
    frame = cv2.cvtColor(frame_array, cv2.COLOR_BGR2RGB)

    first_row_rgb_avg = utils.screensplit_rgb_avg(frame, 1)
    second_row_rgb_avg = utils.screensplit_rgb_avg(frame, 2)
    third_row_rgb_avg = utils.screensplit_rgb_avg(frame, 3)
    
    print(first_row_rgb_avg) 
    #screen_rgb_avg_array


# If frame[y, x].all() == frame[y, x-1].all(): Remove consecutive duplicate indexes.
# Histograms based on avg. 