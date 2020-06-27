# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 13:16:13 2020

@author: chmar
"""


#a script for running the geos2wrf utilities after geos2wps (GEOS_wrapper) has processed the raw data.


# Import necessary libraries
from datetime import datetime, timedelta
import os

#take the start and end date from the namelist
from namelist_geos_scripts import util_start, util_end
start = util_start
end= util_end


#first, we want to process a single time-slice of SST to use as a constant
#geos2wps should already be here, if not remove the pound sign
#os.system('ln -s /scratch/cm5515/NASA/shenglong/geos2wrf_merra2wrf/geos2wps')

sst_directory='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/MET2' 
os.chdir(sst_directory)
then=start+timedelta(0,15*60)
namelist=open('namelist.geos2wps', 'w') 
filename = 'c1440_NR' +'.' 'tavg30mn_2d_met2_Nx' +'.' + then.strftime('%Y%m%d_%H%Mz') + '.' +'nc4'
timestamp=start.strftime('%Y-%m-%d_%H:%M') 
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
namelist.write("variableRanks(1) = 3,\n")
namelist.write("variableLevelTypes(1) = 4,\n")
namelist.write("variableNamesIn(1)='TSH',\n")
namelist.write("variableNamesOut(1)='SST',\n")
namelist.write("variableUnits(1)='K',\n")
namelist.write("variableDescriptions(1)='sea_surface_temperature',\n")
namelist.write("/\n")
namelist.write("&subsetData\n")
namelist.write("subset=.true.,\n")
namelist.write("iLonMin=1121,\n") 
namelist.write("iLonMax=2721,\n") 
namelist.write("jLatMin=1601,\n") 
namelist.write("jLatMax=2241,\n")
namelist.write("kVertMin=1,\n") 
namelist.write("kVertMax=72,\n")
namelist.write("/")
namelist.close()

#processing this one thing should be quick, but it is likely easier to do it on a compute node so we write an sbatch script and submit the job:


sbatch=open("SST.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=GEOS_SST \n")
sbatch.write("#SBATCH --output=GEOS_SST.out \n")
sbatch.write("#SBATCH --error=GEOS_SST.err\n")
sbatch.write("#SBATCH --time=1:00:00\n")
sbatch.write("#SBATCH --mem=80GB\n")
sbatch.write("#SBATCH --ntasks-per-node=25\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
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
sbatch.write("module load hdf/intel/4.2.6 \n")
sbatch.write("module load netcdf/intel/4.1.1\n")
sbatch.write("module load zlib/intel/1.2.8 \n")
sbatch.write("module load jpeg/intel/9b\n")
sbatch.write("module load python3/intel/3.7.3\n")
sbatch.write("cd " + str(sst_directory) +"\n")
sbatch.write("srun ./geos2wps")
sbatch.close()
sbatch=open("SST.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch SST.sbatch'
os.system(command)

# Change working directory
os.chdir('/scratch/cm5515/scripts')

############################################################################################
#now run createSOILHGT

#first, so createSOILHGT and createLANDSEA can run simultaneously, we move soil into a subfolder
const_directory=sst_directory='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/const' 
soil_directory=sst_directory='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/const/soil' 
os.mkdir(soil_directory)
os.chdir(const_directory)
os.system('mv PHIS* soil/')
os.chdir('/scratch/cm5515/scripts')
command='sbatch createSOILHGT.sbatch'
os.system(command)



############################################################################################
#now run createLANDSEA
command='sbatch createLANDSEA.sbatch'
os.system(command)
############################################################################################
#now run createRH


#first, make a folder called RH
RH_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/RH' 
os.mkdir(RH_folder)

# now move everything that createRH needs into the RH folder
t_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/T'
os.chdir(t_folder)
command='mv TT* ' +str(RH_folder)
os.system(command)

qv_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/QV'
os.chdir(qv_folder)
command='mv SPECHUMD* ' +str(RH_folder)
os.system(command)

met1_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/MET1'
os.chdir(met1_folder)
command1='mv TT* ' +str(RH_folder)
command2='mv PSFC* ' +str(RH_folder)
command3='mv SPECHUMD* ' +str(RH_folder)
os.system(command1)
os.system(command2)
os.system(command3)

pressure_folder='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/PL'
os.chdir(pressure_folder)
command='mv PRES* ' +str(RH_folder)
os.system(command)

#now run createRH
os.chdir('/scratch/cm5515/scripts')
command='sbatch createRH.sbatch'
os.system(command)
