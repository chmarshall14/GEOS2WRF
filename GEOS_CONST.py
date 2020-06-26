# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:15:45 2020

@author: chmar
"""


# -*- coding: utf-8 -*-
"""
Created on Tue May  5 10:54:09 2020

@author: chmar
"""
#a script for processing GEOS data using GEOS2WRF

# Import necessary libraries
from datetime import datetime, timedelta
import os
# Change working directory
os.chdir('/scratch/cm5515')
#take the start and end date from the namelist
from namelist.geos_scripts import GEOS_start, GEOS_end
start = GEOS_start
end= GEOS_end


#%% 
# The outfolder for this field was created by the download_wrapper
out_folder = '/scratch/cm5515/storm_'+ start.strftime('%Y%m%d') + '/const'
# Go inside the out folder
os.chdir(out_folder)
#go through and iterate each variable over every time step, by creating a namelist for each timestep and running geos2wps 

#%%
#first, process the daily constants--land, ocean and lake fractions  
os.system('ln -s /scratch/cm5515/NASA/shenglong/geos2wrf_merra2wrf/geos2wps')
now = start
#create a namelist
while now <= end:
    namelist=open('namelist.geos2wps', 'w') 
    filename = 'c1440_NR' +'.' 'const_2d_asm_Nx' +'.' + now.strftime('%Y%m%d') + '.' +'nc4'
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
    namelist.write("forecastHours(1)= 1, \n")
    namelist.write("/\n")
    namelist.write("\n")
    namelist.write("&variables\n")
    namelist.write("numberofVariables=3\n")
    namelist.write("\n")
    namelist.write("variableRanks(1) = 3,\n") 
    namelist.write("variableLevelTypes(1) = 1,\n") 
    namelist.write("variableNamesIn(1)='PHIS',\n") 
    namelist.write("variableNamesOut(1)='PHIS',\n") 
    namelist.write("variableUnits(1)='m**2 s**-2',\n") 
    namelist.write("variableDescriptions(1)='Surface geopotential',\n") 
    namelist.write("\n")
    namelist.write("variableRanks(2) = 3,\n") 
    namelist.write("variableLevelTypes(2) = 1,\n") 
    namelist.write("variableNamesIn(2)='FRLAKE',\n") 
    namelist.write("variableNamesOut(2)='FRLAKE',\n") 
    namelist.write("variableUnits(2)='proprtn',\n") 
    namelist.write("variableDescriptions(2)='Lake fraction',\n") 
    namelist.write("\n")
    namelist.write("variableRanks(3) = 3,\n") 
    namelist.write("variableLevelTypes(3) = 1,\n") 
    namelist.write("variableNamesIn(3)='FROCEAN',\n") 
    namelist.write("variableNamesOut(3)='FROCEAN',\n") 
    namelist.write("variableUnits(3)='proprtn',\n") 
    namelist.write("variableDescriptions(3)='Ocean fraction',\n") 
    namelist.write("/\n")
    namelist.write("&subsetData\n")
    namelist.write("subset=.true.,\n")
    namelist.write("iLonMin=921,\n") 
    namelist.write("iLonMax=2721,\n") 
    namelist.write("jLatMin=1601,\n") 
    namelist.write("jLatMax=2241,\n") 

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
