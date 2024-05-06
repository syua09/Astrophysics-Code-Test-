import astropy.io.fits as fits 
import numpy as np 
import matplotlib.pyplot as plt 
from photutils.background import Background2D , MedianBackground
from photutils.segmentation import detect_sources
from astropy.convolution import convolve
from photutils.segmentation import make_2dgaussian_kernel
from photutils.segmentation import deblend_sources
from skimage.transform import rescale  , resize 
from matplotlib import gridspec 
from astropy.modeling import models , fitting
import matplotlib.image as mpimg
import os 

#files from the loop go through get_Data 
#callback is initialized here for deblend_Data()

def get_Data (files , callback):
        
        #opening fits file and reading data
        Star = fits.open(files) 
        Data = Star[0].data
        plt.imshow(Data , origin = 'lower')
        plt.show()

        star_x = 15 #go somewhere near the center of image
        star_y = 15
        #set the max value to this point 
        maxpix = Data[star_x,star_y] 

        #look around to see if we can find a greater max val 
        for pixx in range (star_x - 5 , star_x + 5):
                for pixy in range (star_y - 5 , star_y + 5):
                        if maxpix < Data[pixx , pixy]:
                                #new max val
                                Newmaxpix = Data[pixx , pixy]

        print(Newmaxpix)
                        
        #deblend the image by using deblend funciton  
        result = deblend_Data(Data) 
        if result > 1:
               print("yippeee")
               
        #set the result of the deblend as a variable
        Pic = plt.imshow(result , origin = 'lower')
        plt.show()
        
        #close fits file 
        Star.close()

        #return Deblended Image
        return(Pic , result)

def gaussian_factory (Data , Newmaxpixel):
       #gaussian model making 
        #shape of the image
        nx , ny = Data.shape 

        y , x = np.mgrid[:ny , :nx] 

        fit_prod = fitting.LevMarLSQFitter() #fitting choices 

        #fixed value for the objects that are detected, in this case two 
        FWHMGuess = 1.5 

        #insert any fixed settings here 
        fixedsettings = {}

        #Creating a Gaussian model 
        Img_Gaussian = models.Gaussian2D (x_mean= Newmaxpixel , y_mean= Newmaxpixel , x_stddev= FWHMGuess , y_stddev= FWHMGuess,
                                        amplitude = Newmaxpixel , fixed = fixedsettings)

        #fitting the model 
        Gaussian_fit = fit_prod(Img_Gaussian , x , y, Data)

        return(Gaussian_fit)
       
        
        
#deblend function, returns a deblended version of fits image

def deblend_Data (Data):
        #setting threshold value for out detect sources function
        threshhold = 0.9
    

      #rescale image by a factor of 3 
        data_scaleup = rescale(Data , 5) 


        kernel = make_2dgaussian_kernel (1.5, size = 15)
        convolved_data = convolve(Data , kernel)

        #detecting how many sources there are in the image
        segment_mp = detect_sources(data_scaleup , threshhold , npixels = 2 )

        #deblend the sources found in the image
        deblend = deblend_sources(data_scaleup , segment_mp , npixels = 2 , 
                                nlevels = 50, contrast = 0.007, progress_bar = False)
        
        #return deblended Image
        return (deblend , segment_mp) 
    

#Main function, loops through files and goes through get_data() and Utilizes a callback for deblend_Data()
for Images in os.listdir('C:/Users/Neuron Upload/Star_Images'):
    get_Data(Images , deblend_Data)
    

    


    