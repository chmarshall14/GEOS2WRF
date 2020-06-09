# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:25:10 2020

@author: chmar
"""
# Import necessary libraries
from datetime import datetime, timedelta
import os
# Change working directory
os.chdir('/scratch/cm5515')
#Use same start and end date as fetcher.py
start = datetime(2005, 8, 13, 19, 00)
end = datetime(2005, 8, 17, 22, 30) 

#%% 
# Create a new outfolder for each storm (just do this in the folder with all the data? Call that storm_n?)
out_folder = 'storm_'+ start.strftime('%Y%m%d') +'/QV'
# Go inside the out folder
os.chdir(out_folder)
#go through and iterate each variable over every time step, by creating a namelist for each timestep and running geos2wps

command='ln -s /scratch/cm5515/NASA/shenglong/geos2wrf_merra2wrf/geos2wps'
os.system(command)

#%% QV, or specific humidity 
now = start
#create a namelist
while now <= end:
   namelist=open('namelist.geos2wps', 'w') 
   filename = 'c1440_NR' +'.' 'inst30mn_3d_QV_Nv' +'.' + now.strftime('%Y%m%d_%H%Mz') + '.' +'nc4'
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
   namelist.write("numberofVariables=1\n")
   namelist.write("\n")
   namelist.write("variableRanks(1) = 4,\n") 
   namelist.write("variableLevelTypes(1) = 11,\n") 
   namelist.write("variableNamesIn(1)='QV',\n") 
   namelist.write("variableNamesOut(1)='SPECHUMD',\n") 
   namelist.write("variableUnits(1)='kg kg-1',\n") 
   namelist.write("variableDescriptions(1)='specific humidity',\n") 
   namelist.write("\n")
   namelist.write("/\n")
   namelist.write("&subsetData\n")
   namelist.write("subset=.true.,\n")
   namelist.write("iLonMin=0921,\n") 
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
