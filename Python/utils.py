import numpy as np
import colour

# Finds the N largest values in a list.
# Returns the index of the N biggest values, from highest to lowest. 
def Nmaxoflist(list1, N):
    maxes = []
    index_of_max_in_list = []

    for x in range(0, N):
        max_value = 0
        for y in range(len(list1)):
            if list1[y] > max_value:
                max_value = list1[y]

        # Since we delete indices from list1 to find multiple max numbers, we have to check-
        # how many indices with lower values then the current one have been deleted and add that number to index writing in index_of_max_in_list.
        if len(index_of_max_in_list) == 0:
            index_of_max_in_list.append(list1.index(max_value))
        else:
            count = 0
            for z in range(0, len(index_of_max_in_list)):
                if list1.index(max_value) > index_of_max_in_list[z]:
                    count = count + 1
            #print(count)
            index_of_max_in_list.append(list1.index(max_value) + count)
        
        del list1[list1.index(max_value)]
        maxes.append(max_value)

    #print(f'max numbers {maxes} and where they are {index_of_max_in_list}')

    return index_of_max_in_list

# Average over a list.
def average(rgblist):
    frame_color_average = int(round((sum(rgblist)) / len(rgblist)))
    return frame_color_average

# 1st argument = ndarray, 2nd arguement = select which section to iterate on. 1, 2 or 3
def screensplit_rgb_avg(ndarray, row_section_number): 

    source = ndarray
    dimscale = row_section_number

    red1 = []
    green1 = []
    blue1 = []
    red2 = []
    green2 = []
    blue2 = []
    red3 = []
    green3 = []
    blue3 = []
    section = []
    
    for y1 in range(round(int(((source.shape[1]) / 3) * (dimscale - 1))), round(int(((source.shape[1]) / 3) * dimscale)) ):
        for x1 in range(0, round(int((source.shape[0]) / 3)) ):
            rgb1 = source[x1, y1]
            red1.append(rgb1[0])
            green1.append(rgb1[1])
            blue1.append(rgb1[2])

    redavg1 = average(red1)
    greenavg1 = average(green1)
    blueavg1 = average(blue1)
    rgbavg1 = [redavg1, greenavg1, blueavg1]

    for y1 in range(round(int(((source.shape[1]) / 3) * (dimscale - 1))), round(int(((source.shape[1]) / 3) * dimscale)) ):
        for x2 in range(round(int(source.shape[0]) / 3), round(int((source.shape[0]) / 3) * 2 )):
            rgb2 = source[x2, y1]
            red2.append(rgb2[0])
            green2.append(rgb2[1])
            blue2.append(rgb2[2])

    redavg2 = average(red2)
    greenavg2 = average(green2)
    blueavg2 = average(blue2)
    rgbavg2 = [redavg2, greenavg2, blueavg2]

    for y1 in range(round(int(((source.shape[1]) / 3) * (dimscale - 1))), round(int(((source.shape[1]) / 3) * dimscale)) ):
        for x3 in range(round((int(source.shape[0]) / 3) * 2), round(int((source.shape[0]) / 3) * 3)):
            rgb3 = source[x3, y1]
            red3.append(rgb3[0])
            green3.append(rgb3[1])
            blue3.append(rgb3[2])
            
    redavg3 = average(red3)
    greenavg3 = average(green3)
    blueavg3 = average(blue3)
    rgbavg3 = [redavg3, greenavg3, blueavg3]

    section.append(rgbavg1)
    section.append(rgbavg2)
    section.append(rgbavg3)

    return section

# Takes a matrix with 3 lists (rgb averages over a screen section) and output a list with one color temperature value for each list.
def rgb2colortemp (rgbsection):

    temp = []
    for ele in range (0, 3):
        sec_array = np.array(rgbsection[ele])
        XYZ = colour.sRGB_to_XYZ(sec_array / 255)
        xy = colour.XYZ_to_xy(XYZ)
        CCT = colour.xy_to_CCT(xy, 'hernandez1999')

        temp.append(CCT)

    colortemp = []
    for i in range(0, 3):
        value = int(round(temp[i]))
        colortemp.append(value)
    
    return colortemp
 