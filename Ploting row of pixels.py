
import pandas as pd 
import numpy as np
import astropy.io.fits as  fits 
from astropy import wcs 
import matplotlib.pyplot as plt
import photoutils as photo
from matplotlib.colors import LogNorm

Star = fits.open('Star(1).fits') #python reads fits file 

Header = (Star[0].header)
Data = Star[0].data 

for i in range (30) :
    plt.scatter(Data [1, i], i)

# plt.imshow(Data)
plt.grid()
plt.xlim(0 , 30)
plt.ylim(0, 30 )

plt.show()
