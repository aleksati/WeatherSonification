from PIL import ImageGrab
import numpy as np
import cv2
import utils
from pythonosc import udp_client
import argparse
import datetime

# Specify smaller screen dim. If so, add the variables to ImageGrab: "ImageGrab.grab(bbox=(0, 0, inputdimx, inputdimy))"
inputdimx = 300
inputdimy = 300

current_time = utils.time('CET')

while True:

    # Grayscale histogram. outputs 255 numbers which correspond to the X axis, the value of every number corresponds to the Y axis.

    screen = ImageGrab.grab()
    r, g, b, a = screen.split() 
    len(r.histogram())
    histlist = r.histogram()


    # Calculate where the peaks are in the histogram.
    N = 10 # Specify how many of the histograms largest Y-values to extract 
    histlist_x_values = utils.Nmaxoflist(histlist, N)
    histlist_x_values_avg = utils.average(histlist_x_values)
    #print(f'The {N} largest Y-values in the histogram are located at: {histlist_x_values} on the x-axis.')
    #print(f'The average of these values are = {histlist_x_values_avg}')


    # Calculate average RGB values for 9 screen sections. From top left to bottom right. 
    screen_rgba_array = np.array(screen)
    screen_rgb_array = screen_rgba_array[:,:,:3] # Removes Alpha from RGBA screen capture

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
    #print(colortemp_array)

    colortemp_list = first_section_color_temp + second_section_color_temp + third_section_color_temp
    #print(f'colortemp screen {colortemp_list}')


    #Send UDP to PureData
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="127.0.0.1",
                        help="The ip of the OSC server")
    parser.add_argument("--port", type=int, default=8888,
                        help="The port the OSC server is listening on")
    args = parser.parse_args()
    client = udp_client.SimpleUDPClient(args.ip, args.port)

    client.send_message('/colortemp', colortemp_list)
    client.send_message('/histogram_avg', histlist_x_values_avg)
    client.send_message('/time', 'PUT VARIABLE HERE')

    break
    #time.sleep(0.4)