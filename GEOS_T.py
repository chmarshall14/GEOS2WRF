# -*- coding: utf-8 -*-
"""
Created on Thu May  7 18:18:12 2020

@author: chmar
"""



# Import necessary libraries
from datetime import datetime, timedelta
import os
# Change working directory

#take the start and end date from the namelist
from namelist_geos_scripts import GEOS_start, GEOS_end, path_to_storm, path_to_geos2wps, iLonMin, iLonMax, jLatMin, jLatMax
os.chdir(path_to_storm)
start = GEOS_start
end= GEOS_end


#%% 
# The outfolder for this field was created by the download_wrapper
out_folder = path_to_storm+ '/storm_'+ start.strftime('%Y%m%d') + '/MET1'
# Go inside the out folder
os.chdir(out_folder)
#go through and iterate each variable over every time step, by creating a namelist for each timestep and running geos2wps 
ls_command='ln -s ' + path_to_geos2wps

#first, process the daily constants--land, ocean and lake fractions  

os.system(ls_command)
now = start
#create a namelist
while now <= end:
   namelist=open('namelist.geos2wps', 'w') 
   filename = 'c1440_NR' +'.' 'inst30mn_3d_T_Nv' +'.' + now.strftime('%Y%m%d_%H%Mz') + '.' +'nc4'
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
   namelist.write("variableNamesIn(1)='T',\n") 
   namelist.write("variableNamesOut(1)='TT',\n") 
   namelist.write("variableUnits(1)='K',\n") 
   namelist.write("variableDescriptions(1)='air_temperature',\n") 
   namelist.write("\n")
   namelist.write("\n")
   namelist.write("/\n")
   namelist.write("&subsetData\n")
   namelist.write("subset=.true.,\n")
   namelist.write("subset=.true.,\n")
   namelist.write("iLonMin=" + str(iLonMin) + ",\n") 
   namelist.write("iLonMax=" + str(iLonMax) + ",\n") 
   namelist.write("jLatMin=" + str(jLatMin) + ",\n") 
   namelist.write("jLatMax=" + str(jLatMax) + ",\n")
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
   #now run geos2wps
   command = 'srun ./geos2wps'
   os.system(command)

   #move on to the next timestep
   now += timedelta(0, 30*60)
