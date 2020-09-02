# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 09:15:03 2020

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
    
print(wrfout)