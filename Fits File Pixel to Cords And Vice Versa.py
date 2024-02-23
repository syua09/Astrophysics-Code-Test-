import pandas as pd 
import numpy as np
import astropy.io.fits as  fits 
from astropy import wcs 
import matplotlib.pyplot as plt
import photoutils as photo
from matplotlib.colors import LogNorm
#from astropy.wcs.utils import pixel_to_skycoord

Star = fits.open('Star(1).fits') #python reads fits file 

Header = (Star[0].header) #mak the header a varibale to use in loop 

# for item in Header :
#     print (item, Header[item]) #prints all the items in the header 

plt.imshow(Star[0].data , origin = 'lower')  #creates image 
# plt.scatter (5 , 5)    # adds a blue point at the (5, 5) coordinates

# Image = Star[0].data # adds the image to a variable
# x , y = Image.shape # retrives x and y values from the shape of the image 

# plt.axis("off")
# plt.show()

# print(x , y) # prints height and length of image from earlier

# data = Star[0].data #retrives pixel data from image
# type(data) 

# print(data.shape) # much easier way to get dimensions of image

# print('Min: ', np.min(data))  #Using numpy to retrieve differnt pixel values
# print('Max: ', np.max(data))
# print('Mean: ', np.mean(data))
# print('Stdev: ', np.std(data))

# plt.imshow(data , cmap = 'gray' , norm = LogNorm())
# plt.colorbar()
# plt.show()

Value = wcs.WCS(Star[0].header)
print(Value.wcs.name)
# Value.wcs.print_contents() #will print the entire header

pixcrd = np.array([[0, 0], [15, 15], [31, 31]], dtype=np.float32) #going from pix to coords
#not utilizing a y value in this case since we have an array with the coordinates therefore
# its left as 0
world = Value.wcs_pix2world(pixcrd , 0) 
print("these are the coords" , world) #print the coordinates

Crdpix = np.array([[285.67326371 , 38.71840765] ,[285.67755578 , 38.71954098]], dtype = np.float32) #going from coords to pixel 
Pixel = Value.wcs_world2pix(Crdpix, 0)      #same syntax we use for pix to world 
print("These are the pixel values ", Pixel)

# plt.scatter( 0, 0)
plt.show()
