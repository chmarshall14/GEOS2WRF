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
#take the start and end date from the namelist
from namelist_geos_scripts import storm_folder, util_start, util_end, path_to_storm, path_to_createRH
start = util_start
end= util_end

out_folder = storm_folder + '/RH'
# Go inside the out folder
os.chdir(out_folder)
#go through and iterate each variable over every time step, by creating a namelist for each timestep and running geos2wps 
ls_command='ln -s ' + path_to_createRH


#first check if the files you need are there
now=start
while now<= end:
    timestamp=now.strftime('%Y-%m-%d_%H:%M')
    filename1 = 'PSFC_GROUND_LEVEL:' + str(timestamp)
    command1 = 'mv ' + storm_folder + '/MET1/' + filename1 + ' ' + out_folder
    if not os.path.exists(filename1):
        print("getting" + filename1)
        os.system(command1)
    filename2 = 'TT_2M_ABOVE_GROUND_LEVEL:' + str(timestamp)
    command2 = 'mv ' + storm_folder + '/MET1/' + filename2 + ' ' + out_folder
    if not os.path.exists(filename2):
        print("getting" + filename2)
        os.system(command2)
    filename3 = 'SPECHUMD_2M_ABOVE_GROUND_LEVEL:' + str(timestamp)
    command3 = 'mv ' + storm_folder + '/MET1/' + filename3 + ' ' + out_folder
    if not os.path.exists(filename3):
        print("getting" + filename3)
        os.system(command3)
    filename4 = 'PRES_MODEL_LEVEL:' + str(timestamp)
    command4 = 'mv ' + storm_folder + '/PL/' + filename4 + ' ' + out_folder
    if not os.path.exists(filename4):
        print("getting" + filename4)
        os.system(command4)
    filename5 = 'SPECHUMD_MODEL_LEVEL:' + str(timestamp)
    command5 = 'mv ' + storm_folder + '/QV/' + filename5 + ' ' + out_folder
    if not os.path.exists(filename5):
        print("getting" + filename5)
        os.system(command5)
    filename6 = 'TT_MODEL_LEVEL:' + str(timestamp)
    command6 = 'mv ' + storm_folder + '/T/' + filename6 + ' ' + out_folder
    if not os.path.exists(filename6):
        print("getting" + filename6)
        os.system(command6)
    now += timedelta(0, 30*60)
os.system(ls_command)
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
