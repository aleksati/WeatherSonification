> ## Sonification Project
> Make music with the weather! This was the objective of our MCT sonification project, presented at UiO Mar 7, 2020. We sonified the weather, based on online webcam-feeds, with spatialized audio. This was a collaborative project by Jarle Foldeson Steinhovden, Aleksander Tidemann, Gaute Timian Dahl Wardenær & Tom Ignatius Wee  

## Color extraction

The code splits your screen into 9 sections and extracts information (color temperature, RGB-values, histogram, Time-zone, coordiantes etc.). The data is then sent to Pure Data via UDP for sonification.

![one city](onecity.png) 

## Requirements

- PIL (Pillow)
- numpy
- openCV 2
- color-science
- pythonosc & argparse
- datetime
- time
- pytz
