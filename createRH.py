# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:47:31 2020

@author: chmar
"""


# Import necessary libraries
from datetime import datetime, timedelta
import os
# Change working directory
os.chdir('/scratch/cm5515')
#Use same start and end date as fetcher.py
from util_wrapper import start, end 


#%% 
# make and go to outfolder 
out_folder = out_folder = 'storm_'+ start.strftime('%Y%m%d') +'/RH'
# Go inside the out folder
os.chdir(out_folder)
#go through and iterate each variable over every time step, by creating a namelist for each timestep and running geos2wps

command='ln -s /scratch/cm5515/NASA/shenglong/geos2wrf_merra2wrf/createRH'
os.system(command)

#%% Now run createRH, for relative humidity 
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
    command3=('cat PSFC_GROUND_LEVEL:' + str(timestamp) + ' TT_MODEL_LEVEL:' \
              + str(timestamp) + ' SPECHUMD_MODEL_LEVEL:' + str(timestamp) + \
                  ' TT_2M_ABOVE_GROUND_LEVEL:' + str(timestamp) + \
                      ' SPECHUMD_2M_ABOVE_GROUND_LEVEL:' + str(timestamp) + \
                          ' PRES_MODEL_LEVEL:' + str(timestamp) +' > GEOS:' +str(timestamp))
    print(command1)
    print(command2)
    print(command3)
    os.system(command1)
    os.system(command2)
    os.system(command3)
    #write the namelist.createRH
    namelist=open('namelist.createRH', 'w')
    namelist.write("&input\n")
    namelist.write("directory='./',\n")
    namelist.write("prefix='GEOS',\n")
    namelist.write("year=" + str(year)+",\n")
    namelist.write("month=" + str(month)+",\n")
    namelist.write("day=" +str(day) + ",\n")
    namelist.write("hour=" + str(hour)+",\n")
    namelist.write("includeMinute=.true.,\n")
    namelist.write("minute=" +str(minute) +",\n")
    namelist.write("processSurfacePressure=.true.,\n")
    namelist.write("surfacePressureName='PSFC',\n")
    namelist.write("pressureName='PRES',\n")
    namelist.write("temperatureName='TT',\n")
    namelist.write("specificHumidityName='SPECHUMD',\n")
    namelist.write("/")
    namelist.close()
    namelist=open("namelist.createRH", "r")
    print(namelist)
    test=namelist.read()
    print(test)
    namelist.close()
    #now run createLANDSEA
    command="srun ./createRH"
    os.system(command)
    now += timedelta(0, 30*60)
