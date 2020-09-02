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
import xarray as xr
from namelist_geos_scripts import download_start, path_to_storm, download_end, start_lat, start_lon, end_lat, end_lon
# download_start = datetime(2005, 10, 9, 0, 00)
# download_end = datetime(2005, 10, 13, 0, 00)
now=download_start
 #%%
#the way geos-5 indexes time is weird, this find the right time coordinate
d1=now
#don't change this
d2=datetime(2005,5,15,21,30)
d=(d1-d2)
moment=int(d.total_seconds() / 1800)
# start_lat=16
# start_lon=135
# os.chdir(path_to_storm)
#we want to find minima in the Pressure at the 500 hPa height.
#%%
#we need to make sure we are only looking over the ocean, so look at oceanfrac first
#this is constant so we don't need to look at multiple start times

oceanfile= 'https://opendap.nccs.nasa.gov/dods/OSSE/G5NR/Ganymed/7km/0.0625_deg/const/const_2d_asm_Nx'
#look at the ocean frac:
ocean=Dataset(oceanfile, 'r')

#subset to look in a narrow domain around your guess of where the storm is
lat_bnds, lon_bnds = [start_lat-2, start_lat+2], [start_lon-4, start_lon+4]
lats = ocean.variables['lat'][:] 
lons = ocean.variables['lon'][:]
lat_inds = np.where((lats > lat_bnds[0]) * (lats < lat_bnds[1]))[0]
lon_inds = np.where((lons > lon_bnds[0]) * (lons < lon_bnds[1]))[0]

oceanfrac= ocean.variables['frocean'][0, lat_inds, lon_inds]

# Now look at 500 hPa lows:
now=download_start
end=download_end
# hfile = 'https://opendap.nccs.nasa.gov/dods/OSSE/G5NR/Ganymed/7km/0.0625_deg/inst/inst30mn_3d_H_Nv'
# height=Dataset(hfile, 'r')
# #subset it to the domain
# H= np.copy(height.variables['h'][moment, 50, lat_inds, lon_inds])
#now look only over the ocean

#now get the sea-level pressure at the minimum
met1_file =  'https://opendap.nccs.nasa.gov/dods/OSSE/G5NR/Ganymed/7km/0.0625_deg/inst/inst30mn_2d_met1_Nx'
met1= Dataset(met1_file, 'r')
slp= np.copy(met1.variables['slp'][moment, lat_inds, lon_inds])
subset=(oceanfrac>.9)
index=np.argmin(slp[subset])
lat_min=np.where(subset)[0][index]
lon_min=np.where(subset)[1][index]
#print the minimum and its location:
ilat=lats[lat_inds][lat_min]
jlon=lons[lon_inds][lon_min]
print('time:', now.strftime('%Y-%m-%d %H:%M'))
print('lat=' +str(ilat))
print('lon=' +str(jlon))
slp_min=slp[lat_min, lon_min]
# print('height=', H[lat_min,lon_min])
#print pressure in hPa instead of Pa
print('SLP=', slp_min*.01)


#you have found the first vortex location--now search over the whole storm:
#%%
while now <= end:
    #we can use the same ocean file because that does not vary with time)
    #the geos-5 time variable is weird, this handles that:
    d1=now 
    d2=datetime(2005,5,15,21,30)
    d=(d1-d2)
    moment=int(d.total_seconds() / 1800)
    lat_bnds, lon_bnds = [ilat-1, ilat+1], [jlon-1, jlon+1]
    lats = ocean.variables['lat'][:] 
    lons = ocean.variables['lon'][:]
    lat_inds = np.where((lats > lat_bnds[0]) * (lats < lat_bnds[1]))[0]
    lon_inds = np.where((lons > lon_bnds[0]) * (lons < lon_bnds[1]))[0]

    oceanfrac= ocean.variables['frocean'][0, lat_inds, lon_inds]
    #the process is the same, we are just varying the time we are looking at now
    

    

    
    #now get the sea-level pressure at the minimum
    slp= np.copy(met1.variables['slp'][moment, lat_inds, lon_inds])
    subset=(oceanfrac>.9)
    index=np.argmin(slp[subset])
    lat_min=np.where(subset)[0][index]
    lon_min=np.where(subset)[1][index]
    #print the minimum and its location:
    print( )
    print('time:', now.strftime('%Y-%m-%d %H:%M'))
    print('lat=', lats[lat_inds][lat_min])
    print('lon=',  lons[lon_inds][lon_min])
    slp_min=slp[lat_min, lon_min]
    # print('height=', H[lat_min,lon_min])
    #print pressure in hPa instead of Pa
    print('SLP=', slp_min*.01)
    # now move to the new center
    ilat=lats[lat_inds][lat_min]
    jlon=lons[lon_inds][lon_min]
    #move to the next timestep:
    now += timedelta(0, 30*60)