# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:26:56 2020

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
    
   then=now+timedelta(0,15*60)
   namelist=open('namelist.geos2wps', 'w') 
   filename = 'c1440_NR' +'.' 'tavg30mn_2d_met2_Nx' +'.' + then.strftime('%Y%m%d_%H%Mz') + '.' +'nc4'
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
   namelist.write("numberofVariables=9\n")
   namelist.write("\n")
   namelist.write("variableRanks(1) = 3,\n")
   namelist.write("variableLevelTypes(1) = 1,\n")
   namelist.write("variableNamesIn(1)='TSOIL1',\n")
   namelist.write("variableNamesOut(1)='ST000010',\n")
   namelist.write("variableUnits(1)='K',\n")
   namelist.write("variableDescriptions(1)='soil_temperatures_layer_1',\n")
   namelist.write("\n")
   namelist.write("variableRanks(2) = 3,\n")
   namelist.write("variableLevelTypes(2) = 1,\n")
   namelist.write("variableNamesIn(2)='TSOIL2',\n")
   namelist.write("variableNamesOut(2)='ST010040',\n")
   namelist.write("variableUnits(2)='K',\n")
   namelist.write("variableDescriptions(2)='soil_temperatures_layer_2',\n")
   namelist.write("\n") 
   namelist.write("variableRanks(3) = 3,\n")
   namelist.write("variableLevelTypes(3) = 1,\n")
   namelist.write("variableNamesIn(3)='TSOIL5',\n")
   namelist.write("variableNamesOut(3)='ST040100',\n")
   namelist.write("variableUnits(3)='K',\n")
   namelist.write("variableDescriptions(3)='soil_temperatures_layer_5',\n")
   namelist.write("\n") 
   namelist.write("variableRanks(4) = 3,\n")
   namelist.write("variableLevelTypes(4) = 1,\n")
   namelist.write("variableNamesIn(4)='TSOIL6',\n")
   namelist.write("variableNamesOut(4)='ST100200',\n")
   namelist.write("variableUnits(4)='K',\n")
   namelist.write("variableDescriptions(4)='soil_temperatures_layer_6',\n")
   namelist.write("\n")
   namelist.write("variableRanks(5) = 3,\n")
   namelist.write("variableLevelTypes(5) = 1,\n")
   namelist.write("variableNamesIn(5)='SFMC',\n")
   namelist.write("variableNamesOut(5)='SM000010',\n")
   namelist.write("variableUnits(5)='m-3 m-3',\n")
   namelist.write("variableDescriptions(5)='water surface layer',\n")
   namelist.write("\n")
   namelist.write("variableRanks(6) = 3,\n")
   namelist.write("variableLevelTypes(6) = 1,\n")
   namelist.write("variableNamesIn(6)='PRMC',\n")
   namelist.write("variableNamesOut(6)='SM010040',\n")
   namelist.write("variableUnits(6)='m-3 m-3',\n")
   namelist.write("variableDescriptions(6)='water profile’',\n")
   namelist.write("\n")
   namelist.write("variableRanks(7) = 3,\n")
   namelist.write("variableLevelTypes(7) = 1,\n")
   namelist.write("variableNamesIn(7)='RZMC',\n")
   namelist.write("variableNamesOut(7)='SM040100',\n")
   namelist.write("variableUnits(7)='m-3 m-3',\n")
   namelist.write("variableDescriptions(7)='water root zone',\n")
   namelist.write("\n")
   namelist.write("variableRanks(8) = 3,\n")
   namelist.write("variableLevelTypes(8) = 1,\n")
   namelist.write("variableNamesIn(8)='RZMC',\n")
   namelist.write("variableNamesOut(8)='SM100200',\n")
   namelist.write("variableUnits(8)='m-3 m-3',\n")
   namelist.write("variableDescriptions(8)='water root zone',\n")
   namelist.write("variableRanks(9) = 3,\n")
   namelist.write("variableLevelTypes(9) = 1,\n")
   namelist.write("variableNamesIn(9)='TSH',\n")
   namelist.write("variableNamesOut(9)='SKINTEMP',\n")
   namelist.write("variableUnits(9)='K',\n")
   namelist.write("variableDescriptions(9)='effective_surface_skin_temperature',\n")
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
   command = 'srun ./geos2wps'
   os.system(command)

   #move on to the next timestep
   now += timedelta(0, 30*60)
