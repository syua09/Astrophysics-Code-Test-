
#This will be to practice finding that graph

import pandas as pd 
import numpy as np
import astropy.io.fits as  fits 
from astropy import wcs 
import matplotlib.pyplot as plt
import photoutils as photo

Star = fits.open('Star(0).fits')
Header = (Star[0].header)
Data = Star[0].data

Row_15 = pd.DataFrame(Data[15])

print(Row_15)



# for i in range (15) :
#     plt.scatter(Data[i], Data[15])

    #print(Data[1 , i] , i)


plt.show()