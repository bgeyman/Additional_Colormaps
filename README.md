# Additional_Colormaps
**Description**: A simple set of functions to load and use a collection of my favorite colormaps

------------------
### Part 1: Instructions for loading functions in a python script

**Option 1: add path to list of directories for python interpreter to search**
```
import sys
sys.path.append('/PATHNAME/Additional_Colormaps/')
from Additional_Colormaps import load_colormap, load_all_cmaps, plot_cmap_example
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

**get_hex_color()** : accepts a list of rgb values (3) and returns the corresponding hex code (string)

Example Call:
```
test_blue = get_hex_color(rgb_code=[40,65,122])
plt.plot([0,1], [0,1], c=test_blue, lw=20);
```

Output:

<img src="https://user-images.githubusercontent.com/56602673/190018375-5184f80f-9e42-478d-860c-dd73bf922ce9.png" width="300" height="250" />

**`make_hex_list()`** : accepts a list of rgb values (list of lists) and returns list of hex values (list of strings)

The above function is useful for preparing the input to `make_custom_cmap_from_hex_list()` which accepts the output of `make_hex_list()` in addition to an integer number of colors and a name (string) and creates a matplotlib **LinearSegmentedColormap** object

Example Call:
```
rgb_list = [[175,162,116], [30,72,105]]
test_hex_list = make_hex_list(rgb_list)
make_custom_cmap_from_hex_list(hex_list=test_hex_list, n_colors=256, cmap_name='test')
```

Output:

<img width="500" alt="example_cbar" src="https://user-images.githubusercontent.com/56602673/190019079-4d97c5f5-d107-4c25-b789-85ab17e0c43a.png">

## Other resources:

**color lists:**
 - https://xkcd.com/color/rgb/ (gallery of named colors from xkcd)



