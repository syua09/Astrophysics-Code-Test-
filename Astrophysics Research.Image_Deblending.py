
import astropy.io.fits as fits 
import numpy as np 
import matplotlib.pyplot as plt 
from photutils.background import Background2D , MedianBackground
from photutils.segmentation import detect_sources
from astropy.convolution import convolve
from photutils.segmentation import make_2dgaussian_kernel
from photutils.segmentation import deblend_sources



Star = fits.open('Star(0).fits')
Header = (Star[0].header)
Data = Star[0].data



threshhold = 0.2
kernel = make_2dgaussian_kernel (1.5, size = 15)
convolved_data = convolve(Data , kernel)
segment_mp = detect_sources(convolved_data , threshhold , npixels = 2 )

deblend = deblend_sources(convolved_data , segment_mp , npixels = 2 , 
                          nlevels = 50, contrast = 0.007, progress_bar = False)

print(segment_mp)

# plt.imshow(Data , origin = 'lower' , cmap = 'Greys_r')

plt.imshow(segment_mp , origin = 'lower' )

plt.imshow(deblend , origin = 'lower') 

plt.show()


# bkg_est = MedianBackground()
# bkg = Background2D(Data , (1, 1), filter_size=(3 , 3), bkg_estimator=bkg_est)

# # Star -= bkg.background

# plt.imshow(Data , origin = 'lower')
# plt.show()

# print(bkg)