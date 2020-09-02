# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 14:32:11 2020

@author: chmar
"""


import numpy as np
from netCDF4 import Dataset
wrfout=Dataset('control0_hist_d02_0.nc', 'r')
p_level=np.copy(wrfout.variables['P'][0, :, 122, 67])
print(p_level)