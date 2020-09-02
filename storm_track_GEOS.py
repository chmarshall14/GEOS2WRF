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
from namelist_geos_scripts import download_start, path_to_storm, download_end
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import shapely.geometry as sgeom
import matplotlib.patches as mpatches
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
font = {'family' : 'sans-serif',
        'size'   : 14}
plt.rc('font', **font)
plt.rcParams['axes.linewidth'] = 1.5
#a script that tracks a storm's minimum sea level pressure in the raw NASA data
#first get the time right
starttime=datetime(2005, 8, 30, 17)
end=datetime(2005, 9, 15, 17)
start_lon=150
start_lat=30.5
now=starttime 
d1=now
#don't change this
d2=datetime(2005,5,15,21,30)
d=(d1-d2)
moment=int(d.total_seconds() / 1800)

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
slat=lats[lat_inds][lat_min]
slon=lons[lon_inds][lon_min]
print('time:', now.strftime('%Y-%m-%d %H:%M'))
print('lat=' +str(ilat))
print('lon=' +str(jlon))
slp_min=slp[lat_min, lon_min]
# print('height=', H[lat_min,lon_min])
#print pressure in hPa instead of Pa
print('SLP=', slp_min*.01)


#you have found the first vortex location--now search over the whole storm:
#%%
storm_lats=np.array([])
storm_slps=np.array([])
storm_lons=np.array([])
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
    storm_lats=np.append(storm_lats, lats[lat_inds][lat_min])
    print('lon=',  lons[lon_inds][lon_min])
    storm_lons=np.append(storm_lons, lons[lon_inds][lon_min])
    slp_min=slp[lat_min, lon_min]
    storm_slps=np.append(storm_slps, slp[lat_min, lon_min])
    #print pressure in hPa instead of Pa
    print('SLP=', slp_min*.01)
    # now move to the new center
    ilat=lats[lat_inds][lat_min]
    jlon=lons[lon_inds][lon_min]
    #move to the next timestep:
    now += timedelta(0, 30*60)
dt=timedelta(0,30*60)
times=starttime+np.arange(529)*dt
# plt.plot(xvals, storm)
# plt.plot(xvals, lon_save)
# plt.plot(xvals, intensities)

#%%
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())
ax.coastlines()
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                  linewidth=1, color = 'black', alpha = .7, linestyle='--')
gl.xlabels_top = False
gl.ylabels_left = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
track = sgeom.LineString(zip(storm_lons, storm_lats))
ax.set_extent([120, 160, 18, 38], ccrs.Geodetic())
ax.add_geometries([track], ccrs.PlateCarree(),
                      facecolor='none', edgecolor='k')
for t in range(times):
    slp = storm_slps[t]/100
    now = storm_times[t]
    if now.hour == 0:
        ax.text(storm_lons[t], storm_lats[t], '%i ' % slp + now.strftime('(%-m/%-d)'), 
                horizontalalignment='center', verticalalignment = 'center', rotation = 30, transform = ccrs.PlateCarree())
    if slp < 920:
        ax.plot(storm_lons[t], storm_lats[t], 'o', markersize = 4, transform=ccrs.PlateCarree(), color = '#ff6060')
    elif slp < 945:
        ax.plot(storm_lons[t], storm_lats[t], 'o', markersize = 4, transform=ccrs.PlateCarree(), color = '#ff8f20')
    elif slp < 965:
        ax.plot(storm_lons[t], storm_lats[t], 'o', markersize = 4, transform=ccrs.PlateCarree(), color = '#ffc140')
    elif slp < 980:
        ax.plot(storm_lons[t], storm_lats[t], 'o', markersize = 4, transform=ccrs.PlateCarree(), color = '#ffe775')
    elif slp < 995:
        ax.plot(storm_lons[t], storm_lats[t], 'o', markersize = 4, transform=ccrs.PlateCarree(), color = '#ffffcc')
    elif slp < 1005:
        ax.plot(storm_lons[t], storm_lats[t], 'o', markersize = 4, transform=ccrs.PlateCarree(), color = '#00faf4')        
    else:
        ax.plot(storm_lons[t], storm_lats[t], 'o', markersize = 4, transform=ccrs.PlateCarree(), color = '#5ebaff')
cat5 = mpatches.Patch(color = '#ff6060', label = 'Cat 5')
cat4 = mpatches.Patch(color = '#ff8f20', label = 'Cat 4')
cat3 = mpatches.Patch(color = '#ffc140', label = 'Cat 3')
cat2 = mpatches.Patch(color = '#ffe775', label = 'Cat 2')
cat1 = mpatches.Patch(color = '#ffffcc', label = 'Cat 1')
storm = mpatches.Patch(color = '#00faf4', label = 'Storm')
dep = mpatches.Patch(color = '#5ebaff', label = 'Depression')
leg = plt.legend(handles=[cat5, cat4, cat3, cat2, cat1, storm, dep], frameon = False)
fig.savefig('storm_paths.png', dpi = 200, bbox_inches = 'tight')

#%%

# Atlantic
real_atlantic = np.array([989, 1002, 991, 930, 929, 997, 1005, 994, 970, 998, 902, 1006, 962, 979, 976, 985, 895, 977, 1001, 988, 882, 998, 962, 1002, 980, 981, 994, 969, 1000, 1001, 999, 985, 963, 955, 955, 985])
nasa_atlantic = np.array([948, 931, 972, 975, 972, 938, 966, 952, 939, 951, 962, 925, 974, 949, 988, 949, 942, 944, 964, 962, 936, 922, 934, 946, 941, 971, 948])
fig, ax = plt.subplots(2, 1, figsize = (9, 10))
ax[0].hist(nasa_atlantic, bins = [880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980],
           edgecolor = 'black', color = '#785EF0')
ax[1].hist(real_atlantic, bins = [880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980],
           edgecolor = 'black', color = '#FE6100')
ax[0].set_title('NASA data (Atlantic)', font)
ax[1].set_title('Real-world data (Atlantic)', font)
ax[0].set_xlabel('Min pressure (hPa)', font)
ax[1].set_xlabel('Min pressure (hPa)', font)
ax[0].set_ylabel('Number storms', font)
ax[1].set_ylabel('Number storms', font)
ax[0].set_xlim([870, 980])
ax[1].set_xlim([870, 980])
ax[0].set_ylim([0, 11])
ax[1].set_ylim([0, 11])
fig.tight_layout()
fig.savefig('atlantic.png', bbox_inches = 'tight', dpi = 200)
