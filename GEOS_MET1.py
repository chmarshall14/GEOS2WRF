# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:28:20 2020

@author: chmar
"""


# Import necessary libraries
from datetime import datetime, timedelta
import os
# Change working directory
os.chdir('/scratch/cm5515')
#Use same start and end date as fetcher.py
from GEOS_wrapper import start, end 
 

#%% 
# go inside the right subfolder
out_folder = 'storm_'+ start.strftime('%Y%m%d') +'/MET1'
# Go inside the out folder
os.chdir(out_folder)
#go through and iterate each variable over every time step, by creating a namelist for each timestep and running geos2wps
command='ln -s /scratch/cm5515/NASA/shenglong/geos2wrf_merra2wrf/geos2wps'
os.system(command)

now = start
#create a namelist
while now <= end:
   namelist=open('namelist.geos2wps', 'w') 
   filename = 'c1440_NR' +'.' 'inst30mn_2d_met1_Nx' +'.' + now.strftime('%Y%m%d_%H%Mz') + '.' +'nc4'
   timestamp=now.strftime('%Y-%m-%d_%H:%M') 
   namelist.write("&files\n")
   namelist.write("\n")
   namelist.write("geosFileFormat=2,\n")
   namelist.write("geosFileName=" +repr(filename)+ ",\n" )
   namelist.write("outputDirectory='./',\n")
   namelist.write("/\n")
   namelist.write("\n")
   namelist.write("&coordinates\n")
   namelist.write("longitudeName='lon',\n")
   namelist.write("latitudeName='lat',\n")
   namelist.write("hasVerticalDimension=.true.,\n")
   namelist.write("verticalName='lev',\n")
   namelist.write("/\n")
   namelist.write("&forecast\n")
   namelist.write("numberOfTimes=1,\n")
   namelist.write("validTimes(1)=" + repr(timestamp)+",\n")
   namelist.write("timeIndices(1)= 1, \n")
   namelist.write("forecastHours(1)= 0, \n")
   namelist.write("/\n")
   namelist.write("\n")
   namelist.write("&variables\n")
   namelist.write("numberofVariables=6\n")
   namelist.write("\n")
   namelist.write("variableRanks(1) = 3,\n") 
   namelist.write("variableLevelTypes(1) = 4,\n") 
   namelist.write("variableNamesIn(1)='PSL',\n") 
   namelist.write("variableNamesOut(1)='PMSL',\n") 
   namelist.write("variableUnits(1)='Pa',\n") 
   namelist.write("variableDescriptions(1)='mean_sea_level_pressure',\n") 
   namelist.write("\n")
   namelist.write("variableRanks(2) = 3,\n") 
   namelist.write("variableLevelTypes(2) = 2,\n") 
   namelist.write("variableNamesIn(2)='QV2M',\n") 
   namelist.write("variableNamesOut(2)='SPECHUMD',\n") 
   namelist.write("variableUnits(2)='kg kg-1',\n") 
   namelist.write("variableDescriptions(2)='2_meter_specific_humidity',\n") 
   namelist.write("\n")
   namelist.write("variableRanks(3) = 3,\n") 
   namelist.write("variableLevelTypes(3) = 2,\n") 
   namelist.write("variableNamesIn(3)='T2M',\n") 
   namelist.write("variableNamesOut(3)='TT',\n") 
   namelist.write("variableUnits(3)='K',\n") 
   namelist.write("variableDescriptions(3)='2_meter_temperature',\n") 
   namelist.write("\n")
   namelist.write("variableRanks(4) = 3,\n") 
   namelist.write("variableLevelTypes(4) = 3,\n") 
   namelist.write("variableNamesIn(4)='U10M',\n") 
   namelist.write("variableNamesOut(4)='UU',\n") 
   namelist.write("variableUnits(4)='m s-1',\n") 
   namelist.write("variableDescriptions(4)='10_meter_eastward_wind',\n") 
   namelist.write("\n")
   namelist.write("variableRanks(5) = 3,\n") 
   namelist.write("variableLevelTypes(5) = 3,\n") 
   namelist.write("variableNamesIn(5)='V10M',\n") 
   namelist.write("variableNamesOut(5)='VV',\n") 
   namelist.write("variableUnits(5)='m s-1',\n") 
   namelist.write("variableDescriptions(5)='10_meter_northward_wind',\n") 
   namelist.write("\n")
   namelist.write("variableRanks(6) = 3,\n") 
   namelist.write("variableLevelTypes(6) = 1,\n") 
   namelist.write("variableNamesIn(6)='PS',\n") 
   namelist.write("variableNamesOut(6)='PSFC',\n") 
   namelist.write("variableUnits(6)='Pa',\n") 
   namelist.write("variableDescriptions(6)='surface_pressure',\n") 
   namelist.write("/\n")
   namelist.write("&subsetData\n")
   namelist.write("iLonMin=1121,\n") 
   namelist.write("iLonMax=2721,\n") 
   namelist.write("jLatMin=1601,\n") 
   namelist.write("jLatMax=2241,\n")
   namelist.write("kVertMin=1,\n") 
   namelist.write("kVertMax=72,\n")
   namelist.write("/")
   namelist.close()
   namelist=open("namelist.geos2wps", "r")
   print(namelist)
   test=namelist.read()
   print(test)
   namelist.close()
   #now run geos2wps
   command = 'srun ./geos2wps'
   os.system(command)

   #move on to the next timestep
   now += timedelta(0, 30*60)
