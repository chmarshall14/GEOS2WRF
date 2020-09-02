# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:03:41 2020

@author: chmar
"""


# Import necessary libraries
from datetime import datetime, timedelta
#take the start and end date from the namelist
from namelist_geos_scripts import storm_folder, cat_start, cat_end, path_to_storm, script_folder, net_id
start = cat_start
end= cat_end
storm_directory=storm_folder

#%% 
# The outfolder for this field was created by the download_wrapper
import os
# Change working directory
cat_directory=storm_folder +'/CAT' 
os.chdir(cat_directory)

#first make sure you have all the files you need:
RH_folder=storm_directory +'/RH' 
U_folder=storm_directory +'/U' 
V_folder=storm_directory +'/V' 
met2_folder=storm_directory +'/MET2'
const_directory=storm_directory +'/const' 
soil_directory=storm_directory +'/const/soil' 
met1_folder=storm_directory +'/MET1'
H_folder=storm_directory +'/H' 

now=start
while now<= end:
    timestamp=now.strftime('%Y-%m-%d_%H:%M')
    filename1 = 'RH_2M_ABOVE_GROUND_LEVEL:' + str(timestamp)
    command1 = 'mv ' + RH_folder + '/' + filename1 + ' ' + cat_directory
    if not os.path.exists(filename1):
        print("getting" + filename1)
        os.system(command1)
    filename2 = 'RH_MODEL_LEVEL:' + str(timestamp)
    command2 = 'mv ' + RH_folder + '/' +  filename2 + ' ' + cat_directory
    if not os.path.exists(filename2):
        print("getting" + filename2)
        os.system(command2)
    filename3 = 'UU_10M_ABOVE_GROUND_LEVEL:' + str(timestamp)
    command3 = 'mv ' + met1_folder + '/'  + filename3 + ' ' + cat_directory
    if not os.path.exists(filename3):
        print("getting" + filename3)
        os.system(command3)
    filename4 = 'PRES_MODEL_LEVEL:' + str(timestamp)
    command4 = 'mv ' + storm_folder + '/PL/' + filename4 + ' ' + cat_directory
    if not os.path.exists(filename4):
        print("getting" + filename4)
        os.system(command4)
    filename5 = 'SPECHUMD_MODEL_LEVEL:' + str(timestamp)
    command5 = 'mv ' + storm_folder + '/QV/' + filename5 + ' ' + cat_directory
    if not os.path.exists(filename5):
        print("getting" + filename5)
        os.system(command5)
    filename6 = 'TT_MODEL_LEVEL:' + str(timestamp)
    command6 = 'mv ' + storm_folder + '/T/' + filename6 + ' ' + cat_directory
    if not os.path.exists(filename6):
        print("getting" + filename6)
        os.system(command6)
    filename7 = 'VV_10M_ABOVE_GROUND_LEVEL:' + str(timestamp)
    command7 = 'mv ' + met1_folder + '/' + filename7 + ' ' + cat_directory
    if not os.path.exists(filename7):
        print("getting" + filename7)
        os.system(command7)
    filename8 = 'SOILHGT_GROUND_LEVEL:' + str(timestamp)
    command8 = 'mv ' + soil_directory + '/' + filename8 + ' ' + cat_directory
    if not os.path.exists(filename8):
        print("getting" + filename8)
        os.system(command8)
#all the soil stuff is number 9, should be fine)
    filename9 = 'ST000010_GROUND_LEVEL:' + str(timestamp)
    command9 = 'mv ' + met2_folder + '/' + filename9 + ' ' + cat_directory
    if not os.path.exists(filename9):
        print("getting" + filename9)
        os.system(command9)
    filename9 = 'ST010040_GROUND_LEVEL:' + str(timestamp)
    command9 = 'mv ' + met2_folder + '/' + filename9 + ' ' + cat_directory
    if not os.path.exists(filename9):
        print("getting" + filename9)
        os.system(command9)
    filename9 = 'ST040100_GROUND_LEVEL:' + str(timestamp)
    command9 = 'mv ' + met2_folder + '/' + filename9 + ' ' + cat_directory
    if not os.path.exists(filename9):
        print("getting" + filename9)
        os.system(command9)
    filename9 = 'ST100200_GROUND_LEVEL:' + str(timestamp)
    command9 = 'mv ' + met2_folder + '/' + filename9 + ' ' + cat_directory
    if not os.path.exists(filename9):
        print("getting" + filename9)
        os.system(command9)
    filename9 = 'SM000010_GROUND_LEVEL:' + str(timestamp)
    command9 = 'mv ' + met2_folder + '/' + filename9 + ' ' + cat_directory
    if not os.path.exists(filename9):
        print("getting" + filename9)
        os.system(command9)
    filename9 = 'SM010040_GROUND_LEVEL:' + str(timestamp)
    command9 = 'mv ' + met2_folder + '/' + filename9 + ' ' + cat_directory
    if not os.path.exists(filename9):
        print("getting" + filename9)
        os.system(command9)
    filename9 = 'SM040100_GROUND_LEVEL:' + str(timestamp)
    command9 = 'mv ' + met2_folder + '/' + filename9 + ' ' + cat_directory
    if not os.path.exists(filename9):
        print("getting" + filename9)
        os.system(command9)
    filename9 = 'SM100200_GROUND_LEVEL:' + str(timestamp)
    command9 = 'mv ' + met2_folder + '/' + filename9 + ' ' + cat_directory
    if not os.path.exists(filename9):
        print("getting" + filename9)
        os.system(command9)
    filename10 = 'H_MODEL_LEVEL:' + str(timestamp)
    command10 = 'mv ' + H_folder + '/' + filename10 + ' ' + cat_directory
    if not os.path.exists(filename10):
        print("getting" + filename10)
        os.system(command10)
    filename11 = 'UU_MODEL_LEVEL:' + str(timestamp)
    command11 = 'mv ' + U_folder + '/' + filename11 + ' ' + cat_directory
    if not os.path.exists(filename11):
        print("getting" + filename11)
        os.system(command11)
#you don't actually need to number these so I am going to stop now...
    filename11 = 'VV_MODEL_LEVEL:' + str(timestamp)
    command11 = 'mv ' + V_folder + '/' + filename11 + ' ' + cat_directory
    if not os.path.exists(filename11):
        print("getting" + filename11)
        os.system(command11)
    filename11 = 'PMSL_MEAN_SEA_LEVEL:' + str(timestamp)
    command11 = 'mv ' + met1_folder + '/' + filename11 + ' ' + cat_directory
    if not os.path.exists(filename11):
        print("getting" + filename11)
        os.system(command11)
    filename11 = 'LANDSEA_GROUND_LEVEL:' + str(timestamp)
    command11 = 'mv ' + const_directory + '/' + filename11 + ' ' + cat_directory
    if not os.path.exists(filename11):
        print("getting" + filename11)
        os.system(command11)
    filename11 = 'LANDSEA_GROUND_LEVEL:' + str(timestamp)
    command11 = 'mv ' + V_folder + '/' + filename11 + ' ' + cat_directory
    if not os.path.exists(filename11):
        print("getting" + filename11)
        os.system(command11)
    filename11 = 'SOILHGT_GROUND_LEVEL:' + str(timestamp)
    command11 = 'mv ' + soil_directory + '/' + filename11 + ' ' + cat_directory
    if not os.path.exists(filename11):
        print("getting" + filename11)
        os.system(command11)
    filename11 = 'SKINTEMP_GROUND_LEVEL:' + str(timestamp)
    command11 = 'mv ' + met2_folder + '/' + filename11 + ' ' + cat_directory
    if not os.path.exists(filename11):
        print("getting" + filename11)
        os.system(command11)
    now += timedelta(0, 30*60)



#now concatenate the files together into GEOS:TIMESTAMP
now = start
while now <= end:
    timestamp=now.strftime('%Y-%m-%d_%H:%M')
    #create the GEOS files that the utilities expect(
    command1='rm GEOS:' +str(timestamp)
    command2='touch GEOS:' +str(timestamp)
    command3=('cat HGT_MODEL_LEVEL:' + str(timestamp) + ' LANDSEA_GROUND_LEVEL:' + str(timestamp) + \
        ' PMSL_MEAN_SEA_LEVEL:' + str(timestamp) + ' PRES_MODEL_LEVEL:' + str(timestamp) + ' \
            PSFC_GROUND_LEVEL:' + str(timestamp) + ' RH_MODEL_LEVEL:' + str(timestamp) + \
                ' RH_2M_ABOVE_GROUND_LEVEL:' + str(timestamp) + \
                    ' SOILHGT_GROUND_LEVEL:' + str(timestamp) + ' TT_2M_ABOVE_GROUND_LEVEL:' + str(timestamp) + \
                        ' TT_MODEL_LEVEL:' + str(timestamp) + ' UU_10M_ABOVE_GROUND_LEVEL:' + str(timestamp) + \
                            ' UU_MODEL_LEVEL:' + str(timestamp) + ' VV_10M_ABOVE_GROUND_LEVEL:' + str(timestamp) + \
                                ' VV_MODEL_LEVEL:' + str(timestamp) + ' ST000010_GROUND_LEVEL:' + str(timestamp) +\
                                    ' ST010040_GROUND_LEVEL:' + str(timestamp) + ' ST040100_GROUND_LEVEL:' + \
                                        str(timestamp) + ' ST100200_GROUND_LEVEL:' + str(timestamp) + \
                                            '  SM000010_GROUND_LEVEL:' + str(timestamp) + \
                                                ' SM010040_GROUND_LEVEL:' + str(timestamp) + \
                                                    ' SM040100_GROUND_LEVEL:' + str(timestamp) + \
                                                        ' SM100200_GROUND_LEVEL:' + str(timestamp) + ' SKINTEMP_GROUND_LEVEL:' + str(timestamp) + \
                                                            ' > GEOS:' + str(timestamp))
    # command4='cp GEOS:' + str(timestamp) +' /scratch/cm5515/wrf-4.0/WPS' 
    os.system(command1)
    os.system(command2)
    os.system(command3)
   # os.system(command4)
    print(command1)
    print(command2)
    print(command3)
    
    now += timedelta(0, 30*60)
