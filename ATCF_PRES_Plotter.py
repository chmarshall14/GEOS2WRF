# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 10:33:45 2020

@author: chmar
"""

#load modules
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.pyplot import figure
from datetime import datetime 
import numpy as np

#steal rob's fonts
font = {'family' : 'sans-serif',
        'weight' : 'bold',
        'size'   : 18}
plt.rc('font', **font)
plt.rcParams['axes.linewidth'] = 2

foont = {'family' : 'sans-serif',
        'weight' : 'bold',
        'size'   : 14}
#This read in ATCF files as WRF prepares them in the following column structure:
names = ('file_number','datetime', 'lat', 'lon', 'pres', 'speed')
format = '%Y/%m/%d%H:%M:%S'
#read in the ATCF file to pandas
df = pd.read_csv('pres_list_new', delim_whitespace=True, names=names)
df=pd.DataFrame(df)
df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%d_%H:%M:%S')
#strip it to just datetime and pressure, making a different curve for each run
df=df.pivot(index='datetime', columns='file_number', values='pres')

#plot
a=df.plot(figsize=(10,5), legend=False, color='blue', alpha=.2)
a.set_xlabel('August 2005', font)
a.set_ylabel('Pressure (hPa)', font)
a.xaxis.set_ticks([datetime(2005,8, 13), datetime(2005,8, 14), datetime(2005,8, 15), datetime(2005, 8, 16), datetime(2005, 8, 17), datetime(2005, 8, 18)])
a.tick_params(labelrotation=0, width = 2, length =8, which = 'both')
for label in a.get_xticklabels():
    label.set_horizontalalignment('center')
for hPa in [945, 965]:
    a.axhline(y = hPa, linewidth = 1, linestyle = '--', color = 'black')
time=datetime(2005,8, 14, 1)
a.text(time, 960, 'Category 3', foont)
a.text(time, 940, 'Category 4', foont)
a.xaxis.set_major_formatter(DateFormatter("%d"))
a.set_xlim(datetime(2005,8, 13, 20), datetime(2005, 8, 18))
a.set_ylim(935, 1010)


