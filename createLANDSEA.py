# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:39:55 2020

@author: chmar
"""
# Import necessary libraries
from datetime import datetime, timedelta
import os
# Change working directory
os.chdir('/scratch/cm5515')
#take the start and end date from the namelist
from namelist_geos_scripts import  storm_folder, util_start, util_end, path_to_storm, path_to_createLANDSEA
start = util_start
end= util_end

out_folder = storm_folder + '/const'
# Go inside the out folder
os.chdir(out_folder)
#go through and iterate each variable over every time step, by creating a namelist for each timestep and running geos2wps 
ls_command='ln -s ' + path_to_createLANDSEA
os.system(ls_command)

#first check that the files you need are there
while now<= end:
    timestamp=now.strftime('%Y-%m-%d_%H:%M')
    filename = 'FRLAKE_GROUND_LEVEL:' + str(timestamp)
    if not os.path.exists(filename):
        print("missing" + filename)
    otherfilename='FROCEAN_GROUND_LEVEL:' + str(timestamp)
    if not os.path.exists(otherfilename):
        print('missing' + otherfilename): 
    now += timedelta(0, 30*60)

#Now run utilities 
#utilities want data combined into files with the format GEOS:TIMESTAMP
#first run createLANDSEA, which tells wrf where the land is 
now = start
while now <= end:
    
    timestamp=now.strftime('%Y-%m-%d_%H:%M')
    year=now.strftime('%Y')
    month=now.strftime('%m')
    day=now.strftime('%d')
    hour=now.strftime('%H')
    minute=now.strftime('%M')
    #create the GEOS files that the utilities expect
    command1='rm GEOS:' +str(timestamp)
    command2='touch GEOS:' +str(timestamp)
    command3='cat FRLAKE_GROUND_LEVEL:' + str(timestamp) + ' FROCEAN_GROUND_LEVEL:' + str(timestamp) + ' > GEOS:' +str(timestamp)
    print(command1)
    print(command2)
    print(command3)
    os.system(command1)
    os.system(command2)
    os.system(command3)
    #write the namelist.createLANDSEA
    namelist=open('namelist.createLANDSEA', 'w')
    namelist.write("&input\n")
    namelist.write("directory='./',\n")
    namelist.write("prefix='GEOS',\n")
    namelist.write("year=" + str(year)+",\n")
    namelist.write("month=" + str(month)+",\n")
    namelist.write("day=" +str(day) + ",\n")
    namelist.write("hour=" + str(hour)+",\n")
    namelist.write("minute=" + str(minute) + ",\n")
    namelist.write("includeminute=.true.,\n")
    namelist.write("lakeFractionName='FRLAKE',\n")
    namelist.write("oceanFractionName='FROCEAN',\n")
    namelist.write("/")
    namelist.close()
    namelist=open("namelist.createLANDSEA", "r")
    print(namelist)
    test=namelist.read()
    print(test)
    namelist.close()
    #create a symbolic link to the executable

    #now run createLANDSEA
    command="srun ./createLANDSEA"
    os.system(command)
    #move on down the line
    now += timedelta(0, 30*60)
