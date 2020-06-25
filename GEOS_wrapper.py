# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 15:27:43 2020

@author: chmar
"""


#a script for processing GEOS data using GEOS2WRF. It is designed to use the same file structure as the download_wrapper
#This script runs GEOSWPS but does not run any of the utilities because of timing issues. That will be yet another high level script. 
#This is a fairly uninteresting script


# Import necessary libraries
from datetime import datetime, timedelta
import os
# Change working directory
os.chdir('/scratch/cm5515/scripts')

#input the start and endtime of your storm--the low-level geos2wps scripts will read this in
start = datetime(2005, 8, 13, 19, 00)
end = datetime(2005, 8, 17, 22, 30)  

#sbatch and low-level scripts to process are already written. Now submit those jobs. 

command1='sbatch GEOS_CONST.sbatch'
command2='sbatch GEOS_H.sbatch'
command3='sbatch GEOS_MET1.sbatch'
command4='sbatch GEOS_met2.sbatch'
command5='sbatch GEOS_PL.sbatch'
command6='sbatch GEOS_QV.sbatch'
command7='sbatch GEOS_T.sbatch'
command8='sbatch GEOS_U.sbatch'
command9='sbatch GEOS_V.sbatch'


