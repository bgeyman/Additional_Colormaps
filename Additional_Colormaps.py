from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.colors as clr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

path = '/Users/bengeyman/Documents/Github/Additional_Colormaps/colormap_files/'

def load_colormap(path=path, filename='WhiteBlueGreenYellowRed.rgb', output_name='test'):

    data = pd.read_csv(path+filename, sep="/", header=1)

    new_data = []
    for row in range(len(data)):
        tmp = data.iloc[row].values.item().split(' ')
        tmp_row = []
        for color in tmp:
            if color.isnumeric()==True:
                tmp_row.append(float(color)/255.) # normalize 255 values to 1
        tmp_row.append(1.) # add A (in RGBA)
        new_data.append(tmp_row)

    newcmp = ListedColormap(new_data, name=output_name)
    return newcmp

def load_all_cmaps():
    ## import cmap from NCL gallery
    ## many more here: https://www.ncl.ucar.edu/Document/Graphics/color_table_gallery.shtml
    
    modis_ndvi      = load_colormap(filename='NEO_modis_ndvi.rgb', output_name='new_cmap')
    WBGYR           = load_colormap(filename='WhiteBlueGreenYellowRed.rgb', output_name='WBGYR')
    BGYORV          = load_colormap(filename='BlGrYeOrReVi200.rgb', output_name='BGYORV')
    precip3_16lev   = load_colormap(filename='precip3_16lev.rgb', output_name='precip3_16lev')
    perc2_9lev      = load_colormap(filename='perc2_9lev.rgb', output_name='perc2_9lev')
    wind_17lev      = load_colormap(filename='wind_17lev.rgb', output_name='wind_17lev')
    cmocean_curl    = load_colormap(filename='cmocean_curl.rgb', output_name='cmocean_curl')
    cmocean_ice     = load_colormap(filename='cmocean_ice.rgb', output_name='cmocean_ice')
    cmocean_thermal = load_colormap(filename='cmocean_thermal.rgb', output_name='cmocean_thermal')
    USGS            = load_colormap(filename='USGS_rainbow_13lev.rgb', output_name='USGS_rainbow')
    USGS_15lev_a    = load_colormap(filename='USGS_rainbow_15lev_handmod.rgb', output_name='USGS_rainbow_15_a')
    USGS_15lev_b    = load_colormap(filename='USGS_rainbow_15lev_handmod_b.rgb', output_name='USGS_rainbow_15_b')
    USGS_16lev      = load_colormap(filename='USGS_rainbow_16lev_handmod.rgb', output_name='USGS_rainbow_16')
    rafaj_10lev     = load_colormap(filename='rafaj_2021_air_quality.rgb', output_name='rafaj_AQ.rgb') # from Peter Rafaj et al 2021 Environ. Res. Lett. 16 045005
    
    maps = {'ndvi': modis_ndvi, 'WBGYR': WBGYR, 'BGYORV':BGYORV, 'precip3_16lev':precip3_16lev,  
            'perc2_9lev': perc2_9lev, 'wind_17lev':wind_17lev, 'cmocean_curl':cmocean_curl,
            'cmocean_ice':cmocean_ice, 'cmocean_thermal':cmocean_thermal, 'USGS_rainbow':USGS, 
            'USGS_rainbow_15lev_a':USGS_15lev_a, 'USGS_rainbow_15lev_b':USGS_15lev_b,
            'USGS_rainbow_16lev':USGS_16lev, 'rafaj_AQ':rafaj_10lev}
    
    return maps

def plot_cmap_example(cmap):
    """
    helper function to plot colormap swatch
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)
    fig, axs = plt.subplots(1, 1, figsize=(3, 3), constrained_layout=True)
    psm = axs.pcolormesh(data, cmap=cmap, rasterized=True, vmin=-4, vmax=4)
    fig.colorbar(psm, ax=axs)
    plt.show()
    return

def get_hex_color(rgb_code):
    # returns hex code corresponding to list of rgb values
    # example call: get_hex_color(rgb_code=[80, 80, 80])
    hex_color = '#%02x%02x%02x' % (rgb_code[0], rgb_code[1], rgb_code[2])
    return hex_color

def make_hex_list(rgb_list):
    # returns list of hex codes from input list of rgb values
    # example call: get_hex_color(rgb_list=[[80,80,80], [10,20,30]])
    assert np.shape(rgb_list)[1] == 3 # assert second dimension of list is rgb set of 3 values
    hex_list = []
    for rgb in rgb_list:
        hex_tmp = get_hex_color(rgb)
        hex_list.append(hex_tmp)
    return hex_list

def make_custom_cmap_from_hex_list(hex_list:list, n_colors:int, cmap_name:str):
    cmap = clr.LinearSegmentedColormap.from_list(cmap_name, hex_list, N=n_colors)
    return cmap
