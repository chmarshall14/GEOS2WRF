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
from namelist_geos_scripts import cat_start, cat_end, path_to_storm, script_folder, net_id
start = cat_start
end= cat_end


# create a working directory
storm_directory='storm_' + start.strftime('%Y%m%d')
storm_directory=path_to_storm + '/' + storm_directory
cat_directory=storm_directory + '/CAT'
os.mkdir(cat_directory)


#now move everything you need to concatenate into the cat folder

#first get everything you used for RH
RH_folder=storm_directory +'/RH' 
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
H_folder=storm_directory +'/H' 
os.chdir(H_folder)

command='mv HGT* ' + str(cat_directory)
os.system(command)

#now get SOILHGT and LANDSEA 
const_directory=storm_directory +'/const' 
soil_directory=storm_directory +'/const/soil' 
os.chdir(const_directory)
command='mv LANDSEA* ' + str(cat_directory)
os.system(command)

os.chdir(soil_directory)
command='mv SOILHGT* ' + str(cat_directory)

#now its time for the reamining met1 fields
met1_folder=storm_directory +'/MET1'
os.chdir(met1_folder)
command1='mv UU* ' +str(cat_directory)
command2='mv VV* ' +str(cat_directory)
command3='mv PMSL* ' +str(cat_directory)
os.system(command1)
os.system(command2)
os.system(command3)

#now the met 2 fields
met2_folder=storm_directory +'/MET2'
os.chdir(met2_folder)
command1='mv ST* ' +str(cat_directory)
command2='mv SM* ' +str(cat_directory)
command3='mv SKINTEMP* ' +str(cat_directory)
os.system(command1)
os.system(command2)
os.system(command3)

#now get model level winds:
U_folder=storm_directory +'/U' 
os.chdir(U_folder)

command='mv UU* ' + str(cat_directory)
os.system(command)

V_folder=storm_directory +'/V' 
os.chdir(V_folder)

command='mv VV* ' + str(cat_directory)
os.system(command)


#now run the catGEOS Script 
os.chdir(script_folder)
sbatch=open("catGEOS.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=catGEOS \n")
sbatch.write("#SBATCH --output=catGEOS.out \n")
sbatch.write("#SBATCH --error=catGEOS.err\n")
sbatch.write("#SBATCH --time=5:00:00\n")
sbatch.write("#SBATCH --mem=30GB\n")
sbatch.write("#SBATCH --ntasks-per-node=20\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user="+ str(net_id) + "@nyu.edu\n")
sbatch.write("cd " +str(script_folder) + "\n")
sbatch.write("module load openmpi/intel/3.1.3\n")
sbatch.write("module load intel/17.0.1\n")
sbatch.write("module load openmpi/intel/3.1.3\n")
sbatch.write("module load netcdf/intel/4.4.1.1\n")
sbatch.write("module load libpng/intel/1.6.29\n")
sbatch.write("module load jasper/intel/2.0.14\n")
sbatch.write("module load openjpeg/intel/2.1.2\n")
sbatch.write("module load zlib/intel/1.2.8\n")
sbatch.write("module load hdf5/intel/1.8.21\n")
sbatch.write("module load szip/intel/2.1.1\n")
sbatch.write("module load hdf/intel/4.2.12\n")
sbatch.write("module load hdf/intel/4.2.6\n")
sbatch.write("module load netcdf/intel/4.1.1\n")
sbatch.write("module load zlib/intel/1.2.8\n")
sbatch.write("module load jpeg/intel/9b\n")
sbatch.write("module load python3/intel/3.7.3\n")
sbatch.write("python catGEOS.py &> log.catGEOS\n")
sbatch.close()
command='sbatch catGEOS.sbatch'
os.system(command)

