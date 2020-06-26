# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 22:46:50 2020

@author: chmar
"""


#a script that downloads all the GEOS files you need to run WRF, into an intiuitive folder structure
# Import necessary libraries
from datetime import datetime, timedelta
import os
# Change working directory
os.chdir('/scratch/cm5515')

#take the start and end time from the namelist
from namelist.geos_scripts import download_start, download_end
start = download_start
end= download_end

date=start.strftime('%Y%m%d') 
#create a folder for your storm
out_folder = 'storm_'+ start.strftime('%Y%m%d') 
os.mkdir(out_folder)
os.chdir(out_folder)
date=start.strftime('%Y%m%d') 
comeback='/scratch/cm5515/' + out_folder 
print(comeback)

################################################################################################################

###########################################
#1) Daily Constant Data
###########################################
#create a subfolder
os.mkdir('const')
os.chdir('const')

#write a wget list, a text document with the urls of all the files we want to download
wget=open('wget_const', 'w')
now=start
folder = 'https://g5nr.nccs.nasa.gov/data/DATA/0.0625_deg/const/'
daily_data='const_2d_asm_Nx'
url = folder + daily_data # folder where data is kept
url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
url = url + 'c1440_NR.'
url = url + daily_data 
url = url + now.strftime('.%Y%m%d')
url = url + ".nc4"
while now.date() <= end.date():
    url = folder + daily_data # folder where data is kept
    url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
    url = url + 'c1440_NR.'
    url = url + daily_data 
    url = url + now.strftime('.%Y%m%d')
    url = url + ".nc4"
    wget.write(str(url) + "\n")
    now += timedelta(1)
wget.close()
wget=open("wget_const", "r")
test=wget.read() 
print(test)
wget.close()
#now we make an sbatch script to download all of this, so we can download everything at once
sbatch=open("CONST.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=wget_const \n")
sbatch.write("#SBATCH --output=wget_const.out \n")
sbatch.write("#SBATCH --error=wget_const.err\n")
sbatch.write("#SBATCH --time=20:00:00\n")
sbatch.write("#SBATCH --mem=10GB\n")
sbatch.write("#SBATCH --ntasks-per-node=28\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
sbatch.write("cd /scratch/cm5515/storm_"+str(date)+ "/const\n")
sbatch.write("wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_const\n")
sbatch.close()
sbatch=open("CONST.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch CONST.sbatch'
os.system(command)
#now leave this cursed subfolder 
os.chdir(comeback)

###########################################
#2) Geopotential Height 
##########################################

#create a subfolder
os.mkdir('H')
os.chdir('H')

#write a wget list, a text document with the urls of all the files we want to download
wget=open('wget_H', 'w')
folder = 'https://g5nr.nccs.nasa.gov/data/DATA/0.0625_deg/inst/'
data_field = 'inst30mn_3d_H_Nv'
now=start
while now <= end:
    url = folder + data_field # folder where data is kept
    url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
    url = url + 'c1440_NR.'
    url = url + data_field 
    url = url + now.strftime('.%Y%m%d_%H%Mz')
    url = url + ".nc4"
    wget.write(str(url) + "\n")
    now += timedelta(0, 30*60)
wget.close()
wget=open("wget_H", "r")
test=wget.read() 
print(test)
wget.close()
#now we make an sbatch script, so we can download everything at once
sbatch=open("H.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=wget_H \n")
sbatch.write("#SBATCH --output=wget_H.out \n")
sbatch.write("#SBATCH --error=wget_H.err\n")
sbatch.write("#SBATCH --time=20:00:00\n")
sbatch.write("#SBATCH --mem=10GB\n")
sbatch.write("#SBATCH --ntasks-per-node=28\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
sbatch.write("cd /scratch/cm5515/storm_"+str(date)+ "/H\n")
sbatch.write("wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_H\n")
sbatch.close()
sbatch=open("H.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch H.sbatch'
os.system(command)
#now leave this cursed subfolder 
os.chdir(comeback)


############################################
#3) MET1
############################################
#create a subfolder
os.mkdir('MET1')
os.chdir('MET1')

#write a wget list, a text document with the urls of all the files we want to download
wget=open('wget_MET1', 'w')
folder = 'https://g5nr.nccs.nasa.gov/data/DATA/0.0625_deg/inst/'
data_field = 'inst30mn_2d_met1_Nx'
now=start
while now <= end:
    url = folder + data_field # folder where data is kept
    url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
    url = url + 'c1440_NR.'
    url = url + data_field 
    url = url + now.strftime('.%Y%m%d_%H%Mz')
    url = url + ".nc4"
    wget.write(str(url) + "\n")
    now += timedelta(0, 30*60)
wget.close()
wget=open("wget_MET1", "r")
test=wget.read() 
print(test)
wget.close()
#now we make an sbatch script, so we can download everything at once
sbatch=open("MET1.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=wget_MET1 \n")
sbatch.write("#SBATCH --output=wget_MET1.out \n")
sbatch.write("#SBATCH --error=wget_MET1.err\n")
sbatch.write("#SBATCH --time=20:00:00\n")
sbatch.write("#SBATCH --mem=10GB\n")
sbatch.write("#SBATCH --ntasks-per-node=28\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
sbatch.write("cd /scratch/cm5515/storm_"+str(date)+ "/MET1\n")
sbatch.write("wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_MET1\n")
sbatch.close()
sbatch=open("MET1.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch MET1.sbatch'
os.system(command)
#now leave this cursed subfolder 
os.chdir(comeback)


############################################
#4) MET2
############################################
#create a subfolder
os.mkdir('MET2')
os.chdir('MET2')

#write a wget list, a text document with the urls of all the files we want to download
wget=open('wget_MET2', 'w')
folder = 'https://g5nr.nccs.nasa.gov/data/DATA/0.0625_deg/tavg/'
data_field = 'tavg30mn_2d_met2_Nx'
now = start + timedelta(0, 15*60) 
while now <= end + timedelta(0, 15*60):
    url = folder + data_field # folder where data is kept
    url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
    url = url + 'c1440_NR.'
    url = url + data_field 
    url = url + now.strftime('.%Y%m%d_%H%Mz')
    url = url + ".nc4"
    wget.write(str(url) + "\n")
    now += timedelta(0, 30*60)
wget.close()
wget=open("wget_MET2", "r")
test=wget.read() 
print(test)
wget.close()
#now we make an sbatch script, so we can download everything at once
sbatch=open("MET2.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=wget_MET2 \n")
sbatch.write("#SBATCH --output=wget_MET2.out \n")
sbatch.write("#SBATCH --error=wget_MET2.err\n")
sbatch.write("#SBATCH --time=20:00:00\n")
sbatch.write("#SBATCH --mem=10GB\n")
sbatch.write("#SBATCH --ntasks-per-node=28\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
sbatch.write("cd /scratch/cm5515/storm_"+str(date)+ "/MET2\n")
sbatch.write("wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_MET2\n")
sbatch.close()
sbatch=open("MET2.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch MET2.sbatch'
os.system(command)
#now leave this cursed subfolder 
os.chdir(comeback)


############################################
#5) PL
############################################
#create a subfolder
os.mkdir('PL')
os.chdir('PL')

#write a wget list, a text document with the urls of all the files we want to download
wget=open('wget_PL', 'w')
folder = 'https://g5nr.nccs.nasa.gov/data/DATA/0.0625_deg/inst/'
data_field = 'inst30mn_3d_PL_Nv'
now=start
while now <= end:
    url = folder + data_field # folder where data is kept
    url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
    url = url + 'c1440_NR.'
    url = url + data_field 
    url = url + now.strftime('.%Y%m%d_%H%Mz')
    url = url + ".nc4"
    wget.write(str(url) + "\n")
    now += timedelta(0, 30*60)
wget.close()
wget=open("wget_PL", "r")
test=wget.read() 
print(test)
wget.close()
#now we make an sbatch script, so we can download everything at once
sbatch=open("PL.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=wget_PL \n")
sbatch.write("#SBATCH --output=wget_PL.out \n")
sbatch.write("#SBATCH --error=wget_PL.err\n")
sbatch.write("#SBATCH --time=20:00:00\n")
sbatch.write("#SBATCH --mem=28GB\n")
sbatch.write("#SBATCH --ntasks-per-node=28\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
sbatch.write("cd /scratch/cm5515/storm_"+str(date)+ "/PL\n")
sbatch.write("wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_PL\n")
sbatch.close()
sbatch=open("PL.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch PL.sbatch'
os.system(command)
#now leave this cursed subfolder 
os.chdir(comeback)


############################################
#6) T
############################################
#create a subfolder
os.mkdir('T')
os.chdir('T')

#write a wget list, a text document with the urls of all the files we want to download
wget=open('wget_T', 'w')
folder = 'https://g5nr.nccs.nasa.gov/data/DATA/0.0625_deg/inst/'
data_field = 'inst30mn_3d_T_Nv'
now=start
while now <= end:
    url = folder + data_field # folder where data is kept
    url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
    url = url + 'c1440_NR.'
    url = url + data_field 
    url = url + now.strftime('.%Y%m%d_%H%Mz')
    url = url + ".nc4"
    wget.write(str(url) + "\n")
    now += timedelta(0, 30*60)
wget.close()
wget=open("wget_T", "r")
test=wget.read() 
print(test)
wget.close()
#now we make an sbatch script, so we can download everything at once
sbatch=open("T.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=wget_T \n")
sbatch.write("#SBATCH --output=wget_T.out \n")
sbatch.write("#SBATCH --error=wget_T.err\n")
sbatch.write("#SBATCH --time=20:00:00\n")
sbatch.write("#SBATCH --mem=10GB\n")
sbatch.write("#SBATCH --ntasks-per-node=28\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
sbatch.write("cd /scratch/cm5515/storm_"+str(date)+ "/T\n")
sbatch.write("wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_T\n")
sbatch.close()
sbatch=open("T.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch T.sbatch'
os.system(command)
#now leave this cursed subfolder 
os.chdir(comeback)


############################################
#7) U
############################################
#create a subfolder
os.mkdir('U')
os.chdir('U')

#write a wget list, a text document with the urls of all the files we want to download
wget=open('wget_U', 'w')
folder = 'https://g5nr.nccs.nasa.gov/data/DATA/0.0625_deg/inst/'
data_field = 'inst30mn_3d_U_Nv'
now=start
while now <= end:
    url = folder + data_field # folder where data is kept
    url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
    url = url + 'c1440_NR.'
    url = url + data_field 
    url = url + now.strftime('.%Y%m%d_%H%Mz')
    url = url + ".nc4"
    wget.write(str(url) + "\n")
    now += timedelta(0, 30*60)
wget.close()
wget=open("wget_U", "r")
test=wget.read() 
print(test)
wget.close()
#now we make an sbatch script, so we can download everything at once
sbatch=open("U.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=wget_U \n")
sbatch.write("#SBATCH --output=wget_U.out \n")
sbatch.write("#SBATCH --error=wget_U.err\n")
sbatch.write("#SBATCH --time=20:00:00\n")
sbatch.write("#SBATCH --mem=10GB\n")
sbatch.write("#SBATCH --ntasks-per-node=28\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
sbatch.write("cd /scratch/cm5515/storm_"+str(date)+ "/U\n")
sbatch.write("wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_U\n")
sbatch.close()
sbatch=open("U.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch U.sbatch'
os.system(command)
#now leave this cursed subfolder 
os.chdir(comeback)


############################################
#8) QV
############################################
#create a subfolder
os.mkdir('QV')
os.chdir('QV')

#write a wget list, a text document with the urls of all the files we want to download
wget=open('wget_QV', 'w')
folder = 'https://g5nr.nccs.nasa.gov/data/DATA/0.0625_deg/inst/'
data_field = 'inst30mn_3d_QV_Nv'
now=start
while now <= end:
    url = folder + data_field # folder where data is kept
    url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
    url = url + 'c1440_NR.'
    url = url + data_field 
    url = url + now.strftime('.%Y%m%d_%H%Mz')
    url = url + ".nc4"
    wget.write(str(url) + "\n")
    now += timedelta(0, 30*60)
wget.close()
wget=open("wget_QV", "r")
test=wget.read() 
print(test)
wget.close()
#now we make an sbatch script, so we can download everything at once
sbatch=open("QV.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=wget_QV \n")
sbatch.write("#SBATCH --output=wget_QV.out \n")
sbatch.write("#SBATCH --error=wget_QV.err\n")
sbatch.write("#SBATCH --time=20:00:00\n")
sbatch.write("#SBATCH --mem=28GB\n")
sbatch.write("#SBATCH --ntasks-per-node=28\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
sbatch.write("cd /scratch/cm5515/storm_"+str(date)+ "/QV\n")
sbatch.write("wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_QV\n")
sbatch.close()
sbatch=open("QV.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch QV.sbatch'
os.system(command)
#now leave this cursed subfolder 
os.chdir(comeback)




############################################
#9) V
############################################
#create a subfolder
os.mkdir('V')
os.chdir('V')

#write a wget list, a text document with the urls of all the files we want to download
wget=open('wget_V', 'w')
folder = 'https://g5nr.nccs.nasa.gov/data/DATA/0.0625_deg/inst/'
data_field = 'inst30mn_3d_V_Nv'
now=start
while now <= end:
    url = folder + data_field # folder where data is kept
    url = url + now.strftime('/Y%Y/M%m/D%d/') # specific date
    url = url + 'c1440_NR.'
    url = url + data_field 
    url = url + now.strftime('.%Y%m%d_%H%Mz')
    url = url + ".nc4"
    wget.write(str(url) + "\n")
    now += timedelta(0, 30*60)
wget.close()
wget=open("wget_V", "r")
test=wget.read() 
print(test)
wget.close()
#now we make an sbatch script, so we can download everything at once
sbatch=open("V.sbatch", "w")
sbatch.write("#!/bin/bash \n")
sbatch.write("#SBATCH --nodes=1 \n")
sbatch.write("#SBATCH --job-name=wget_V \n")
sbatch.write("#SBATCH --output=wget_V.out \n")
sbatch.write("#SBATCH --error=wget_V.err\n")
sbatch.write("#SBATCH --time=20:00:00\n")
sbatch.write("#SBATCH --mem=28GB\n")
sbatch.write("#SBATCH --ntasks-per-node=28\n")
sbatch.write("#SBATCH --cpus-per-task=1\n")
sbatch.write("#SBATCH --mail-type=END\n")
sbatch.write("#SBATCH --mail-user=cm5515@nyu.edu\n")
sbatch.write("cd /scratch/cm5515/storm_"+str(date)+ "/V\n")
sbatch.write("wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_V\n")
sbatch.close()
sbatch=open("V.sbatch", "r")
test=sbatch.read()
print(test)
#now download the data from the URLs in the wget list
command='sbatch V.sbatch'
os.system(command)
#now leave this cursed subfolder 
os.chdir(comeback)





