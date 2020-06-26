# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:27:43 2020

@author: chmar
"""


#a script for processing GEOS data using GEOS2WRF. It is designed to use the same folder structure as the download_wrapper
#This script runs GEOSWPS but does not run any of the utilities because of timing issues. That will be yet another high level script. 
#This is a fairly uninteresting script


# Import necessary libraries
import os
# Change working directory
os.chdir('/scratch/cm5515/scripts')




#sbatch scripts that run the lower-level python scripts are already written, now submit them

command1='sbatch GEOS_CONST.sbatch'
command2='sbatch GEOS_H.sbatch'
command3='sbatch GEOS_MET1.sbatch'
command4='sbatch GEOS_met2.sbatch'
command5='sbatch GEOS_PL.sbatch'
command6='sbatch GEOS_QV.sbatch'
command7='sbatch GEOS_T.sbatch'
command8='sbatch GEOS_U.sbatch'
command9='sbatch GEOS_V.sbatch'


os.system(command1)
os.system(command2)
os.system(command3)
os.system(command4)
os.system(command5)
os.system(command6)
os.system(command7)
os.system(command8)
os.system(command9)


