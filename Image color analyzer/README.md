# Image color analyzer
#### Video Demo:  [link](https://youtu.be/ItgnI-jzE5I)
## Introduction:
This is a Python script that analyzes the color distribution of images. It sorts the pixels into colors, brightness, and saturation, using its HLS values. This data can be used for analysis or sorting.

## Overview:
It uses the Python Imaging Library (PIL) to open and resize the image to a square with the dimensions specified by the dimensions variable. The color_analyze function loops over each pixel of the image, converting the RGB color value to a hue, lightness, and saturation (HLS) value using the colorsys.rgb_to_hls function. Based on the HLS value, the color is classified into one of nine color categories, and the brightness and saturation are classified into one of three categories each. The script then retuns the count of colors, brightness, and saturation for each image.


## Features:
This script has 2 main modes, which is changed by choosing which section of the main() code is commented out.
The single file mode analyzes a single image and plots the returned data using matplotlib. The other one automatically iterates over image inside an "image" folder.
The data is returned as a dictionary format, which can be used to tag or sort the images based on your own parameters.


## Analysis
"The dress" is neither white/gold nor black/blue.
It's yellow and blue. And a bunch of grey.

At least, the pixels in this image is yellow and blue. One interesting thing to note about this image though, is that the saturation levels are very low, which means the colors on each of the pixels is actually much closer the **grey** than yellow or blue. This makes it harder for the human eye to perceve the color boundaries, which is why people may see different colors.

For reference though, the actual physical dress is black and blue.




## Sample data output:
### flowers.png
colors_count = {'red': 4809, 'yellow': 1969, 'green': 0, 'cyan': 0, 'blue': 243, 'purple': 478, 'black': 5, 'grey': 2496, 'white': 0}

light_count = {'bright': 258, 'neutral': 8762, 'dark': 980}

saturation_count = {'high': 72, 'mid': 769, 'low': 9159}

### dog.png
colors_count = {'red': 1500, 'yellow': 545, 'green': 80, 'cyan': 0, 'blue': 199, 'purple': 2486, 'black': 2362, 'grey': 753, 'white': 2075}

light_count = {'bright': 2428, 'neutral': 2642, 'dark': 4930}

saturation_count = {'high': 1996, 'mid': 713, 'low': 7291}

### parrot.png
colors_count = {'red': 2723, 'yellow': 4046, 'green': 2765, 'cyan': 57, 'blue': 36, 'purple': 7, 'black': 270, 'grey': 85, 'white': 11}

light_count = {'bright': 219, 'neutral': 5603, 'dark': 4178}

saturation_count = {'high': 5698, 'mid': 3800, 'low': 502}

### rainbow.png
colors_count = {'red': 1216, 'yellow': 2289, 'green': 547, 'cyan': 982, 'blue': 773, 'purple': 345, 'black': 0, 'grey': 3064, 'white': 784}

light_count = {'bright': 3414, 'neutral': 6369, 'dark': 217}

saturation_count = {'high': 955, 'mid': 2647, 'low': 6398}



