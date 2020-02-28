def find_max(numbers):
    max = numbers[0]
    for count in numbers:
        if count > max:
            max = count
    return max


def average(rgblist):
    frame_color_average = int(round((sum(rgblist)) / len(rgblist)))
    return frame_color_average

# 1 should be =
# y or x 

def screensplit_rgb_avg(ndarray, row_section_number): #1st argument = ndarray , 2nd arguement = select which sections of rows to iterate on. 
    source = ndarray
    dimscale = row_section_number
    source.shape[0]

    red1 = []
    green1 = []
    blue1 = []
    red2 = []
    green2 = []
    blue2 = []
    red3 = []
    green3 = []
    blue3 = []
    
    for y1 in range(round(int(((source.shape[1]) / 3) * (dimscale - 1))), round(int(((source.shape[1]) / 3) * dimscale)) ): #First first third of the height
        for x1 in range(0, round(int((source.shape[0]) / 3))): #Second first third of the width
            rgb1 = frame[y1, x1]
            red1.append(rgb1[0])
            green1.append(rgb1[1])
            blue1.append(rgb1[2])

    redavg1 = int(utils.average(red1))
    greenavg1 = int(utils.average(green1))
    blueavg1 = int(utils.average(blue1))
    rgbavg1 = [redavg1, greenavg1, blueavg1]

    for y1 in range(round(int(((source.shape[1]) / 3) * (dimscale - 1))), round(int(((source.shape[1]) / 3) * dimscale)) ): #Second first third of the height.
        for x2 in range(round(int(((source.shape[0]) / 3), round(int(((source.shape[0]) / 3) * 2)))) ): #Second first third of the width
            rgb2 = frame[y1, x2]
            red2.append(rgb2[0])
            green2.append(rgb2[1])
            blue2.append(rgb2[2])

    redavg2 = int(utils.average(red2))
    greenavg2 = int(utils.average(green2))
    blueavg2 = int(utils.average(blue2))
    rgbavg2 = [redavg2, greenavg2, blueavg2]

    for y1 in range(round(int(((source.shape[1]) / 3) * (dimscale - 1))), round(int(((source.shape[1]) / 3) * dimscale)) ): #Second first third of the height.
        for x2 in range(round(int(((source.shape[0]) / 3) * 2), round(int(((source.shape[0]) / 3) * 3))) ): #Second first third of the width
            rgb3 = frame[y1, x3]
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
    return section