# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 09:51:03 2020

@author: chmar
"""


"""
Define options
"""

# CONTROL SIMULATION
# ==================

# Folders
wrf = '~/wrf-4.0/WRF/main'
scratch = '/scratch/cm5515'
home = '/home/rwebber/Build_WRF/SCRIPTS/control/'
data = scratch + "/Kangaroo_Jack"
storage = '/archive/c/cm5515/Kangaroo_Jack'

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

# PLOTTING
# ========

# Define quantiles, colors and labels
xils = [.05, .25, .75, .95]
cols = ['orange', 'red', 'orange']
labels = ['5% - 25%', '25% - 75%', '75% - 95%']