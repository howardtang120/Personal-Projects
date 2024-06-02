from PIL import Image
from colorsys import rgb_to_hls
import os
from plot import *

# Used to resize the image into an square image
# Small value for speed, large value for accuracy
dimensions = 100

def main():
    filename = input("enter filename: ")  # your own image

    # filename = "images/dog.png"               # bright and purple
    # filename = "images/flowers.png"           # medium and yellow/purple
    # filename = "images/parrot.png"            # bright and colorful, saturated
    # filename = "images/rainbow.png"           # bright and colorful, saturated
    # filename = "images/the_dress.png"         # white/gold or black/blue??
    # filename = "images/the_dress_green.png"   # with (0, 255, 0) background

    ### Single image mode ###
    with Image.open(filename) as file:
        print("\n", filename)
        img = file.resize((dimensions, dimensions))
        color_count, light_count, saturation_count = color_analyze(img)
        plot_color(color_count)
        plot_light(light_count)
        plot_saturation(saturation_count)
        plt.show()

    ### iterate over all images in "images" folder ###
    # for filename in os.listdir("images"):
    #     file_path = os.path.join("images", filename)
    #     if os.path.isfile(file_path):
    #         with Image.open(file_path) as file:
    #             print("\n", filename)
    #             img = file.resize((dimensions, dimensions))
    #             color_analyze(img)


def color_analyze(img):
    colors_count = {
        "red": 0, "yellow": 0, "green" : 0, "cyan" : 0, "blue" : 0, "purple" : 0, "black" : 0, "grey" : 0, "white" : 0
    }
    light_count = {
        "bright": 0, "neutral": 0, "dark": 0
    }
    saturation_count = {
        "high": 0, "mid": 0, "low": 0
    }


    for x in range(dimensions):
        for y in range(dimensions):
            if img.mode in ('RGBA', 'LA'):
                r, g, b, a = img.getpixel((x, y))
            else:
                r, g, b = img.getpixel((x, y))
            # print(f"x{x:3d}, y{y:3d},,,r{r:3d}, g{g:3d}, b{b:3d}")

            # Filter the "greenscreen" (0, 255, 0)
            if r == 0 and g == 255 and b == 0:
                continue

            # low values of rgb breaks colorsys.rgb_to_hls
            # s = rangec / (2.0 - sumc), where sumc is sum of min/max of rgb
            # if sumc = 2, it causes ZeroDivisionError
            if (r < 10 and g < 10 and b < 10):
                colors_count["black"] += 1
                light_count["dark"] += 1
                saturation_count["low"] += 1
                continue

            h, l, s = rgb_to_hls(r/255, g/255, b/255)


            color = color_sort(h, l, s)
            colors_count[color] += 1

            light = light_sort(l)
            light_count[light] += 1

            saturation = saturation_sort(s)
            saturation_count[saturation] += 1

    print("colors_count =", colors_count)
    print("light_count =", light_count)
    print("saturation_count =", saturation_count)

    return colors_count, light_count, saturation_count


def color_sort(h, l, s):
    if l < 0.1:                 return "black"
    if l > 0.9:                 return "white"
    if s < 0.1:                 return "grey"

    # h value is between 0 and 1
    if h < 0.083 or h > 0.917:  return "red"
    elif h < 0.25:              return "yellow"
    elif h < 0.417:             return "green"
    elif h < 0.583:             return "cyan"
    elif h < 0.75:              return "blue"
    else:                       return "purple"

def light_sort(l):
    # l value is between 0 and 1
    if l > 0.7:     return "bright"
    elif l < 0.3:   return "dark"
    else:           return "neutral"

def saturation_sort(s):
    # s value is between 0 and 1
    if s > 0.7:     return "high"
    elif s < 0.3:   return "low"
    else:           return "mid"


if __name__ == "__main__":
    main()


