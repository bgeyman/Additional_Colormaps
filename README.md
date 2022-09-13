# Additional_Colormaps
**Description**: Collection of a few of my favorite colormaps

------------------
### Part 1: Instructions for loading functions in a python script

**Option 1: add path to list of directories for python interpreter to search**
```
import sys
sys.path.append('/PATHNAME/Additional_Colormaps/')
from Additional_Colormaps import make_colormap, load_all_cmaps, plot_cmap_example
```
**Option 2: Install python package in "development mode"**

Step 1: In terminal, activate conda environment, then execute following command:

`conda develop PATHNAME/Additional_Colormaps/`

Step 2: import functions without needing to add path to sys.path as below:

`from Additional_Colormaps import make_colormap, load_all_cmaps, plot_cmap_example`

------------------
### Part 2: Calling functions

**`load_all_cmaps()`** : returns a dictionary with the key containing the name of each colormap and the value containing a matplotlib.colors.ListedColormap object

Example Call:
```
new_cmaps = load_all_cmaps()
```

**`plot_cmap_example()`** : accepts a cmap (matplotlib.colors.ListedColormap object) as the only argument and returns a quick visualization of the colormap. Function plots a grid of random numbers using matplotlib pcolormesh() method

Example Call:
```
new_cmaps = load_all_cmaps()
plot_cmap_example(new_cmaps['rafaj_AQ'])
```

Output:

<img src="https://user-images.githubusercontent.com/56602673/190008674-40fdb61f-6b18-4bf7-a82c-e7761578f51d.png" width="300" height="250" />

