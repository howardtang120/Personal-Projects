from project import *
from colorsys import rgb_to_hls as hls

# test values against:
# https://www.w3schools.com/colors/colors_hsl.asp

# All values are in in RGB, functions only take HLS
# When testing, modify functions to take RGB and convert within function instead

def test_color():
    # between 0 and 1
    assert color_sort(0, 0, 0) == "black"
    assert color_sort(255, 255, 255) == "white"
    assert color_sort(128, 128, 128) == "grey"
    assert color_sort(255, 255, 0) == "yellow"
    assert color_sort(0, 200, 200) == "cyan"
    assert color_sort(125, 59, 125) == "purple"

def test_light():
    # between 0 and 1
    assert light_sort(0, 0, 0) == "dark"
    assert light_sort(255, 255, 255) == "bright"
    assert light_sort(128, 128, 128) == "neutral"

    assert light_sort(71, 71, 0) == "dark"          # dark yellow
    assert light_sort(179, 255, 255) == "bright"    # bright cyan
    assert light_sort(255, 0, 255) == "neutral"     # neutral purple


def test_saturation():
    # between -1 and 0
    assert saturation_sort(0, 0, 0) == "low"
    assert saturation_sort(255, 255, 255) == "low"
    assert saturation_sort(147, 108, 108) == "low"

    assert saturation_sort(159, 96, 96) == "low"    # 25%
    assert saturation_sort(64, 191, 64) == "mid"    # 50%
    assert saturation_sort(32, 32, 223) == "high"    # 75%

    assert saturation_sort(236, 236, 19) == "high"  # 85%
    assert saturation_sort(6, 249, 249)  == "high"  # 95%
    assert saturation_sort(0, 128, 255)  == "high"  #100%


