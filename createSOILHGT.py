# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:57:30 2020

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
out_folder = 'storm_'+ start.strftime('%Y%m%d') +'/const'
# Go inside the out folder
os.chdir(out_folder)
#go through and iterate each variable over every time step, by creating a namelist for each timestep and running geos2wps

command='ln -s /scratch/cm5515/NASA/shenglong/geos2wrf_merra2wrf/createSOILHGT'
os.system(command)

#%% Now run createSOILHGT, which gives WRF terrain heights 
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
    command3=('cat PHIS_GROUND_LEVEL:' + str(timestamp) + ' > GEOS:' +str(timestamp))
    print(command1)
    print(command2)
    print(command3)
    os.system(command1)
    os.system(command2)
    os.system(command3)
    #write the namelist.createSOILHGT
    namelist=open('namelist.createSOILHGT', 'w')
    namelist.write("&input\n")
    namelist.write("directory='./',\n")
    namelist.write("prefix='GEOS',\n")
    namelist.write("year=" + str(year)+",\n")
    namelist.write("month=" + str(month)+",\n")
    namelist.write("day=" +str(day) + ",\n")
    namelist.write("hour=" + str(hour)+",\n")
    namelist.write("minute=" + str(minute) + ",\n")
    namelist.write("includeMinute=.true.,\n")
    namelist.write("surfaceGeopotentialName='PHIS',\n")
    namelist.write("/")
    namelist.close()
    namelist=open("namelist.createSOILHGT", "r")
    print(namelist)
    test=namelist.read()
    print(test)
    namelist.close()
   # link="ln -s /scratch/cm5515/NASA/shenglong/geos2wrfmerra2wrf/createSOILHGT"
    #os.system(link)
    #now run createLANDSEA
    command="srun ./createSOILHGT"
    os.system(command)
    #move on down the line
    now += timedelta(0, 30*60)
