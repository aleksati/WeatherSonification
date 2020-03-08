# Weather data from image feed

> ## Sonification Project

> Make music with the weather! This was the objective of our MCT sonification project, presented at UiO Mar 7, 2020. The idea was to essentially sonify the weather based on online webcam live-feeds and spatialized audio. This was a collaborative project by:
> 
> Jarle Foldeson Steinhovden, Aleksander Tidemann, Gaute Timian Dahl Wardenær & Tom Ignatius Wee  


This repo covers the color/weather extraction process in particular.

# Color extraction

The frame extraction is based on pythons PIL and color-science libraries in particular and reads consecutive frames from your computer screen. The program extracts weather information by collecting color temperature values based on RGB-averages from nine equally large sections on your screen (as seen in the image below), color temperature average from the entire image, grayscale histogram information (if the entire image is darker or brighter on average) and time values from a specific timezone. This data gives you a good indication of what the weather is like and what the image/camera feed looks like.

![one city](img/onecity.png)

Additionally, the script features code to easily send your data via UDP to a specific local port for further processing. 

## Packages needed

- PIL (Pillow)
- numpy
- openCV 2
- color-science
- pythonosc & argparse
- datetime
- time
- pytz
