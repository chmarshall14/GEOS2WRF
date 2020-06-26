# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:56:48 2020

@author: chmar
"""

from datetime import datetime


#this is a namelist for you to enter the start and end date of your storm. 
#it is broken up into four sections so you can process different stages of multiple storms at once
#This should be the only file you have to edit to start processing a storm. 
#After entering in the four start times there are four high-level scripts:

#The first is the download_wrapper, which downloads the necessary GEOS fields and organizes them into a folder called storm_<startdate>
download_start = datetime(2005, 9, 21, 4, 00)
download_end = datetime(2005, 9, 26, 9, 00)  


#the next is GEOS_wrapper, which processes the raw data with the geos2wps executable
GEOS_start = datetime(2005, 9, 21, 4, 00)
GEOS_end = datetime(2005, 8, 17, 22, 30)  

#the next is the util_wrapper, which runs the GEOS utilities to create LANDSEA, SOILHGT and RH

util_start = datetime(2005, 9, 21, 4, 00)
util_end = datetime(2005, 8, 17, 22, 30)  

#then there is the cat_wrapper, which concatenates all of the disparate data files into one GEOS file per-timestep to be used in WPS
cat_start = datetime(2005, 9, 21, 4, 00)
cat_end = datetime(2005, 8, 17, 22, 30)  


