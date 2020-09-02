# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 23:22:03 2020

@author: chmar
"""


# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 21:49:20 2020

@author: chmar
"""


import datetime 
from datetime import timedelta, datetime 
import os
import numpy as np 
from netCDF4 import Dataset
import netCDF4 
# import xarray as xr
# from namelist_geos_scripts import download_start, path_to_storm, download_end, start_lat, start_lon, end_lat, end_lon
# now=download_start
 #%%
# A script that finds SLP minimum in the domain at each time-step. 
download_start = datetime(2005, 9, 21, 4, 00)
download_end = datetime(2005, 9, 26, 9, 00)  
file='tracktest'
wrfout=Dataset(file, 'r')




# Now look at 500 hPa lows:
now=download_start
end=download_end
# hfile = 'https://opendap.nccs.nasa.gov/dods/OSSE/G5NR/Ganymed/7km/0.0625_deg/inst/inst30mn_3d_H_Nv'
# height=Dataset(hfile, 'r')
# #subset it to the domain
# H= np.copy(height.variables['h'][moment, 50, lat_inds, lon_inds])
#now look only over the ocea]
oceanfrac= wrfout.variables['XLAND'][0, :, :]
slp= wrfout.variables['PSFC'][:,: ,:]
lats = wrfout.variables['XLAT'][:] 
lons = wrfout.variables['XLONG'][:]
subset=(oceanfrac>1.8)
#you have found the first vortex location--now search over the whole storm:
#%%
while now <= end:
    #we can use the same ocean file because that does not vary with time)
    #the geos-5 time variable is weird, this handles that:
    d1=now 
    d2=download_start
    d=(d1-d2)
    moment=int(d.total_seconds() / 1800)
    slp= wrfout.variables['PSFC'][moment,: ,:]
    #the process is the same, we are just varying the time we are looking at now
    
    #now get the sea-level pressure at the minimum
    
    index=np.argmin(slp[subset])
    lat_min=np.where(subset)[0][index]
    lon_min=np.where(subset)[1][index]
    slp_min=slp[lat_min, lon_min]
    #print the minimum and its location:
    print( )
    print('time:', now.strftime('%Y-%m-%d %H:%M'))
    # print('height=', H[lat_min,lon_min])
    #print pressure in hPa instead of Pa
    print('SLP=', slp_min*.01)
    print('lat=', lats[lat_min])
    print('lon=',  lons[lon_min])
    
    #now move to the new center
    # ilat=lats[lat_inds][lat_min]
    # jlon=lons[lon_inds][lon_min]
    #move to the next timestep:
    now += timedelta(0, 30*60)