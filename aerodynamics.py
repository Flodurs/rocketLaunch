import numpy as np


#Source: https://www.grc.nasa.gov/www/k-12/airplane/atmosmet.html
# h = altitude 
def getAtmosphereDensity(h):
    #Upper Stratosphere
    
    # if h < 10:
        # return 1
    
    if h > 25000:
        T = -131.21 + 0.00299*h
        p = 2.448* ((T+273.1)/216.6)**(-11.388)
    
    
    #lower Stratosphere
    if h > 11000 and h <= 25000:
        T = -56.46
        p = 22.65*np.exp(1.73-0.000157*h)
    
    
    #Troposphere
    if h <= 11000:
        T = 15.04-0.00649*h
        p = 101.29 * ((T+273.1)/288.08)**5.256
    
       
    #not 100% sure with the units here 
    return p/(0.2869*(T+273.1))
    

    