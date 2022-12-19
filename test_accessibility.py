# ----------------------------------------------------
# Colorblindness tools
# ----------------------------------------------------
from matplotlib.colors import ListedColormap
from colormath import color_diff
from colormath.color_objects import sRGBColor, LabColor, HSVColor, CMYKColor, LCHabColor
from colormath.color_conversions import convert_color
from colortools import *

def get_colormath_sRGB(rgb_old, is_upscaled=False):
    '''
    Arguments:
        - `rgb_old` (list) : a list in which the first 3 elements are [r, g, b] coordinates.
                             Coordinates are either upscaled (0.0 - 1.0) or not (0 - 255)
        - `is_upscaled` (bool) :  If True, RGB values are between 1-255. If False, 0.0-1.0.
    Returns:
        sRGB color object from colormath package
    
    Example Usage:
        rgb = get_colormath_sRGB(new_cmaps['rafaj_AQ'].colors[2], is_upscaled=False)
    '''
    #rgb_old = cmap.colors[i]
    rgb = sRGBColor(rgb_old[0], rgb_old[1], rgb_old[2], is_upscaled=is_upscaled)

    return rgb

def cmap_to_greyscale(cmap):
    ''' 
    Description: wrapper to sequentially call to_grayscale() and return greyscale `hex_list`

    Arguments:
        - `cmap` a matplotlib ListedColormap (e.g., new_cmaps['rafaj_AQ'])

    Returns:
        - `hex_list` a list of hex codes corresponding to greyscale version of input cmap
    '''

    hex_list = []
    for rgb in cmap.colors:
        sRGB = get_colormath_sRGB(rgb)
        greyscale_sRGB = to_grayscale(sRGB)
        hex = greyscale_sRGB.get_rgb_hex()
        hex_list.append(hex)

    return hex_list

def cmap_to_colorblind_g(cmap):
    ''' 
    Description: wrapper to sequentially call to_colorblind_g() and return colorblind_g `hex_list`

    Arguments:
        - `cmap` a matplotlib ListedColormap (e.g., new_cmaps['rafaj_AQ'])

    Returns:
        - `hex_list` a list of hex codes corresponding to colorblind_g version of input cmap
    '''

    hex_list = []
    for rgb in cmap.colors:
        sRGB = get_colormath_sRGB(rgb)
        colorblind_g_sRGB = to_colorblind_g(sRGB)
        hex = colorblind_g_sRGB.get_rgb_hex()
        hex_list.append(hex)

    return hex_list

def cmap_to_colorblind_r(cmap):
    ''' 
    Description: wrapper to sequentially call to_colorblind_r() and return colorblind_r `hex_list`

    Arguments:
        - `cmap` a matplotlib ListedColormap (e.g., new_cmaps['rafaj_AQ'])

    Returns:
        - `hex_list` a list of hex codes corresponding to colorblind_r version of input cmap
    '''

    hex_list = []
    for rgb in cmap.colors:
        sRGB = get_colormath_sRGB(rgb)
        colorblind_r_sRGB = to_colorblind_r(sRGB)
        hex = colorblind_r_sRGB.get_rgb_hex()
        hex_list.append(hex)

    return hex_list


def display_accessibility_comparison(cmap):
    '''
    Displays print and colorblindness accessibility for input colormap using colormath tools 
    Arguments:
        - `cmap` (matplotlib ListedColormap)
    Example Usage:
        display_colorblind_comparison(new_cmaps['rafaj_AQ'])
    '''
    display(cmap, display_id=0)
    display(ListedColormap(cmap_to_greyscale(cmap), name='greyscale'), display_id=1)
    display(ListedColormap(cmap_to_colorblind_g(cmap), name='colorblind_g'), display_id=2)
    display(ListedColormap(cmap_to_colorblind_r(cmap), name='colorblind_r'), display_id=3)
    return