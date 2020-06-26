# -*- coding: utf-8 -*-
"""
Created on Fri May  8 00:03:41 2020

@author: chmar
"""


# Import necessary libraries
from datetime import datetime, timedelta
#take the start and end date from the namelist
from namelist.geos_scripts import util_start, util_end
start = util_start
end= util_end


#%% 
# The outfolder for this field was created by the download_wrapper
import os
# Change working directory
cat_directory='/scratch/cm5515/storm_' + start.strftime('%Y%m%d') +'/CAT' 
os.chdir(cat_directory)


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
    # print(command1)
    # print(command2)
    # print(command3)
    
    now += timedelta(0, 30*60)
