# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 14:07:32 2020

@author: chmar
"""


#a file that prepares the GEOS files to be concatenated and runs catGEOS
# Import necessary libraries
from datetime import datetime, timedelta
import os
#import the start and end time from the namelist
#take the start and end date from the namelist
from namelist.geos_scripts import cat_start, cat_end
start = cat_start
end= cat_end

# create a working directory
cat_directory='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/CAT' 
os.mkdir(cat_directory)


#now move everything you need to concatenate into the cat folder

#first get everything you used for RH
RH_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/RH' 
os.chdir(RH_folder)

command1='mv RH* ' + str(cat_directory)
command2='mv TT* '  + str(cat_directory)
command3='mv PSFC* ' + str(cat_directory)
command4='mv PRES* ' + str(cat_directory)

os.system(command1)
os.system(command2)
os.system(command3)
os.system(command4)

#now get HGT
H_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/H' 
os.chdir(H_folder)

command='mv HGT* ' + str(cat_directory)
os.system(command)

#now get SOILHGT and LANDSEA 
const_directory=sst_directory='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/const' 
soil_directory=sst_directory='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/const/soil' 
os.chdir(const_directory)
command='mv LANDSEA* ' + str(cat_directory)
os.system(command)

os.chdir(soil_directory)
command='mv SOILHGT* ' + str(cat_directory)

#now its time for the reamining met1 fields
met1_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/MET1'
os.chdir(met1_folder)
command1='mv UU* ' +str(cat_directory)
command2='mv VV* ' +str(cat_directory)
command3='mv PMSL* ' +str(cat_directory)
os.system(command1)
os.system(command2)
os.system(command3)

#now the met 2 fields
met2_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/MET2'
os.chdir(met2_folder)
command1='mv ST* ' +str(cat_directory)
command2='mv SM* ' +str(cat_directory)
command3='mv SKINTEMP* ' +str(cat_directory)
os.system(command1)
os.system(command2)
os.system(command3)

#now get model level winds:
U_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/U' 
os.chdir(U_folder)

command='mv UU* ' + str(cat_directory)
os.system(command)

V_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/V' 
os.chdir(U_folder)

command='mv VV* ' + str(cat_directory)
os.system(command)


#now run the catGEOS Script 
os.chdir('/scratch/cm5515/scripts')
command='sbatch catGEOS.sbatch'
os.system(command)

