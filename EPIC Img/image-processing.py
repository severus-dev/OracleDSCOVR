# Remove the magic commands
# %pylab inline
# %matplotlib inline

from ipy_table import *
import h5py
import numpy as np
from matplotlib.pyplot import imshow
import matplotlib.pyplot as plt

# Remove the line causing the error if not running in IPython
# h5py.enable_ipython_completer()

img = h5py.File("D:\\Data\\Science\\Астрономія\\Nasa Space Apps 2023\\EPIC Img\\epic_1b_20231005195659_03.h5")

# Assuming you want to print the keys of the HDF5 file
print(list(img))
list(img['Band317nm'])

make_table([("Attribute", "Value")] + list(img['Band317nm']['Geolocation']['Earth'].attrs.items()))

fig = plt.figure(figsize=(15, 25))

i = 1
for band in img:
    a = fig.add_subplot(5, 3, i)
    plt.imshow(img[band]['Image'])
    plt.colorbar()
    a.set_title(band)
    i += 1
    
plt.show()



