from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import matplotlib.colors as clr
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json

from colortools import *

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

def make_cmap_from_rgblist(rgblist, output_name='test'):
    new_data = []
    for triple in rgblist:
        tmp_row = []
        for color in triple:
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
    
    # -- now add cmcrameri maps
    for i in ['lapazS.txt','acton.txt','actonS.txt','bam.txt','bamako.txt','bamakoS.txt',
              'bamO.txt','batlow.txt','batlowK.txt','batlowS.txt','batlowW.txt','berlin.txt',
              'bilbao.txt','bilbaoS.txt','broc.txt','brocO.txt','buda.txt','budaS.txt',
              'bukavu.txt','cork.txt','corkO.txt','davos.txt','davosS.txt','devon.txt',
              'devonS.txt','fes.txt','grayC.txt','grayCS.txt','hawaii.txt','hawaiiS.txt',
              'imola.txt', 'imolaS.txt', 'lajolla.txt', 'lajollaS.txt', 'lapaz.txt',
              'lisbon.txt', 'nuuk.txt', 'nuukS.txt', 'oleron.txt', 'oslo.txt', 'osloS.txt',
              'roma.txt', 'romaO.txt', 'tofino.txt', 'tokyo.txt', 'tokyoS.txt', 'turku.txt',
              'turkuS.txt', 'vanimo.txt', 'vik.txt', 'vikO.txt']:
        
        data = np.loadtxt(path+f'cmcrameri/{i}')
        N = data.shape[0]
        name = i.split('.')[0]

        # Create and register colormap
        maps[name] = ListedColormap(colors=data, name=name)

    # -- now add coloropt/ggsci maps
    with open('./colormap_files/coloropt_palettes.json', 'r') as openfile:
        coloropt_palettes = json.load(openfile)

    for cmap_name in list(coloropt_palettes.keys()):
        maps[cmap_name] = make_cmap_from_rgblist(coloropt_palettes[cmap_name], output_name=cmap_name)
    
    return maps

new_cmaps = load_all_cmaps()

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


## Categorize colormaps for use in function `show_cmaps()`. This section is and `show_cmaps()`
## is taken from https://github.com/callumrollo/cmcrameri and slightly adapted.
_cmap_names_sequential = (
    "batlow", "batlowW", "batlowK",
    "devon", "lajolla", "bamako",
    "davos", "bilbao", "nuuk",
    "oslo", "grayC", "hawaii", 
    "lapaz", "tokyo", "buda",
    "acton", "turku", "imola",
)

_cmap_names_diverging = (
    "broc", "cork", "vik",
    "lisbon", "tofino", "berlin",
    "roma", "bam", "vanimo",
)

_cmap_names_multi_sequential = (
    "oleron", "bukavu", "fes",
)

_cmap_names_uncategorized = (
    "ndvi",'WBGYR', 'BGYORV', 'precip3_16lev', 'perc2_9lev', 'wind_17lev', 
    'cmocean_curl', 'cmocean_ice', 'cmocean_thermal', 
    'USGS_rainbow', 'USGS_rainbow_15lev_a', 'USGS_rainbow_15lev_b', 'USGS_rainbow_16lev', 'rafaj_AQ'
)

_cmap_names_categorical = (
    'seaborn_colorblind', 'seaborn_colorblind6', 'paultol_high_contrast', 'paultol_vibrant', 
    'paultol_muted', 'paultol_light', 'okabe', 'ggsci_nature_review_cancer', 'ggsci_aaas', 
    'ggsci_new_england_journal_of_medicine', 'ggsci_lancet_oncology', 'ggsci_jama', 
    'ggsci_clinical_oncology', 'ggsci_uscs_genome', 'ggsci_d3js_cat10', 'ggsci_d3js_cat20', 
    'ggsci_d3js_cat20b', 'ggsci_d3js_cat20c', 'ggsci_igv', 'ggsci_locuszoom', 'ggsci_uchicago', 
    'ggsci_uchicago_light', 'ggsci_uchicago_dark', 'ggsci_cosmic_hallmark_1', 'ggsci_cosmic_hallmark_2', 
    'ggsci_cosmic_hallmark_3', 'ggsci_simpsons', 'ggsci_futurama', 'ggsci_rick_morty', 
    'ggsci_star_trek', 'ggsci_tron', 'coloropt_normal'
)

_cmap_base_names_uncategorized = tuple(
    name
    for name in _cmap_names_uncategorized

)

_cmap_base_names_categorical = tuple(
    name
    for name in _cmap_names_sequential
    if name not in {"batlowW", "batlowK"}
)


_cmap_base_names_cyclic = (
    "roma", "bam",
    "broc", "cork", "vik",
)
_cmap_names_cyclic = tuple(
    f"{name}O"
    for name in _cmap_base_names_cyclic
)


def show_cmaps(*, ncols=6, figwidth=8):
    """

    """
    import math

    x = np.linspace(0, 1, 256)[np.newaxis, :]

    groups = (
        ("Sequential", _cmap_names_sequential),
        ("Diverging", _cmap_names_diverging),
        ("Multi-sequential", _cmap_names_multi_sequential),
        ("Cyclic", _cmap_names_cyclic),
        ("Categorical", _cmap_names_categorical),
        ("Uncategorized", _cmap_names_uncategorized)
    )

    nrows = 1
    istarts = []
    for group_name, group in groups:
        n = len(group)
        istarts.append(nrows)
        nrows += math.ceil(n / ncols)
        if group_name != groups[-1][0]:
            nrows += 1  # group spacer row

    nrows_titles = len(groups)
    nrows_cmaps = nrows - nrows_titles

    hrel_spacer = 0.3  # spacer height relative cmap row height
    hratios = [1 for _ in range(nrows)]
    for i in istarts:
        hratios[i-1] = hrel_spacer  # group spacer row

    hrow = 0.4  # size of cmap row
    hspace = 0.7  # hspace, relative to `hrow`
    hbottom = 0.2
    htop = 0.05
    figheight = (
        hbottom + 
        htop + 
        hrow*nrows_cmaps + 
        hrow*hrel_spacer*nrows_titles + 
        hrow*hspace*(nrows - 1)
    )

    fig, axs = plt.subplots(nrows, ncols,
        figsize=(figwidth, figheight),
        gridspec_kw=dict(
            left=0.01, right=0.99,
            top=1 - htop/figheight,
            bottom=hbottom/figheight,
            hspace=hspace/np.mean(hratios),
            wspace=0.08,
            height_ratios=hratios
        )
    )
    fig.set_tight_layout(False)

    for ax in axs.flat:
        ax.set_axis_off()

    for istart, (group_name, group) in zip(istarts, groups):

        # Group label
        ax0 = axs[istart, 0]
        ax0.text(0.01, 1.02, group_name, size=24, c="0.4", style="italic", 
            va="bottom", ha="left", transform=ax0.transAxes)

        for ax, cmap_name in zip(axs[istart:].flat, group):

            cmap = new_cmaps[cmap_name]
            ax.imshow(x, cmap=cmap, aspect="auto")
            if (len(cmap_name)<12):
                ax.text(0.01 * ncols/6, -0.03, cmap_name, size=14, color="0.2",
                    va="top", transform=ax.transAxes)
            elif (len(cmap_name)<24):
                ax.text(0.01 * ncols/6, -0.03, cmap_name, size=8, color="0.2",
                    va="top", transform=ax.transAxes)    

#hex_colors = []
#for c in colors:
#    rgb_code = np.array(c)*255
#    rgb_code = rgb_code.astype(int)
#    hex_code = get_hex_color(list(rgb_code))
#    hex_colors.append(hex_code)

#if __name__ == "__main__":
#    import sys
#    fib(int(sys.argv[1]))