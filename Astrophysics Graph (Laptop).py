
#This will be to practice finding that graph

import pandas as pd 
import numpy as np
import astropy.io.fits as  fits 
from astropy import wcs 
import matplotlib.pyplot as plt
import photoutils as photo

Star = fits.open('Star(1).fits')
Header = (Star[0].header)
Data = Star[0].data

y = Data[15]
x = [1 , 2 , 3 ,4 ,5 ,6 ,7 ,8 , 9 ,10 , 11 ,12,13 , 14 ,15 ,16, 17 , 18, 19, 20 ,21, 22 ,23 ,24 ,25 ,26 , 27 , 28, 29, 30 , 31]

print(len(x) , len(y))

plt.scatter(x , y)
plt.plot(x , y)


# for i in range (29) :
#     plt.scatter(i, Row_15)

    


plt.show()