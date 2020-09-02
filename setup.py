# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 10:05:42 2020

@author: chmar
"""


# Set up folder environment and namelists


# SETUP

# Import modules
import os
import shutil
import sys
import re

# Read in options
# sys.path.append('/scratch/cm5515/scripts')
# Folders
wrf = '/home/cm5515/wrf-4.0/WRF/main'
scratch = '/scratch/cm5515'
# home = '/home/rwebber/Build_WRF/SCRIPTS/control/'
data = scratch + "/Kangaroo_Jack"
storage = '/archive/c/cm5515/Kangaroo_Jack'
3
# Name of run
run = 'control'

# Number of trajectories
num = 100

# Start and end of simulation
startyear = 2005
startmonth = 8
startday = 13
endyear = 2005
endmonth = 8
endday = 17
# MAKE FOLDERS WITH INSTRUCTIONS TO WRF.EXE
# =========================================

# Recover reference namelist
with open(data + '/namelist.input') as file:
    namelist = file.readlines()

# Set up directories with new namelists
for i in range(num):
    runname = run + str(i)
    if runname in os.listdir(scratch):
        shutil.rmtree(scratch + '/' + runname)
    os.mkdir(scratch + '/' + runname)

    # Copy run files to directories
    for file in os.listdir(wrf):
        # The filematch avoids copying extra files
        # that would clutter the drive
        filematch = re.match('^rsl|^wrfinput|^wrfbdy|^met|^name', file)
        if not filematch:
            os.symlink(wrf + '/' + file, scratch + '/' + runname + '/' + file)
    for file in ['wrfbdy_d01', 'wrfinput_d01']:
        shutil.copy(data + '/' + file, scratch + '/' + runname + '/' + file)
    
    # Redefine namelists according to seeds
    connect = open(scratch + '/' + runname + '/namelist.input', 'w+')
    for line in range(len(namelist)):
        words = namelist[line].split()
        if len(words) > 0 and words[0] == 'nens':
            connect.write(namelist[line].replace('1', str(i + 1)))
        elif len(words) > 0 and words[0] == 'history_outname':
            connect.write(namelist[line].replace('hist_d<domain>', run + str(i) + '_hist_d<domain>_0'))
	# Output restart files every day
    	# elif len(words) > 0 and words[0] == 'restart_interval':
     #        connect.write(namelist[line].replace('14400', '1440'))
     #    elif len(words) > 0 and words[0] == 'rst_outname':
     #        connect.write(namelist[line].replace('rst_d<domain>', run + str(i) + '/rst_d<domain>_<date>'))
        else:
            connect.write(namelist[line])
    connect.close()