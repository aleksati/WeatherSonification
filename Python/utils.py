def find_max(numbers):
    max = numbers[0]
    for count in numbers:
        if count > max:
            max = count
    return max


def average(rgblist):
    frame_color_average = int(round((sum(rgblist)) / len(rgblist)))
    return frame_color_average
