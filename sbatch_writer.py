# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 16:56:39 2020

@author: chmar
"""
# Import modules
import os

#set up how many control folders there are and where they're located
net_id='cm5515'
directory='/scratch/cm5515' #this should also be where this script lives
num=100

for i in range(num):
    folder='control' + str(i)
    os.chdir(folder)
    sbatch=open("control" + str(i) + ".sbatch", "w")
    sbatch.write("#!/bin/bash \n")
    sbatch.write("#SBATCH --nodes=1 \n")
    sbatch.write("#SBATCH --job-name=control" +str(i) + " \n")
    sbatch.write("#SBATCH --output=control" + str(i) + ".out \n")
    sbatch.write("#SBATCH --error=control" + str(i) + ".err\n")
    sbatch.write("#SBATCH --time=20:00:00\n")
    sbatch.write("#SBATCH --mem=100GB\n")
    sbatch.write("#SBATCH --ntasks-per-node=25\n")
    sbatch.write("#SBATCH --cpus-per-task=1\n")
    sbatch.write("#SBATCH --mail-type=END\n")
    sbatch.write("#SBATCH --mail-user="+ str(net_id) + "@nyu.edu\n")
    sbatch.write("\n")
    sbatch.write("cd control" + str(i) + "\n")
    sbatch.write("\n")
    sbatch.write("module load openmpi/intel/3.1.3\n")
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
    sbatch.write("module load hdf/intel/4.2.6\n")
    sbatch.write("module load netcdf/intel/4.1.1\n")
    sbatch.write("module load zlib/intel/1.2.8\n")
    sbatch.write("module load jpeg/intel/9b\n")
    sbatch.write("\n")
    sbatch.write("ulimit -s unlimited \n")
    sbatch.write ("srun wrf.exe")
    sbatch.close()
    # sbatch=open("control" + str(i) + ".sbatch", "r")
    # test=sbatch.read()
    # print(test)
    #now submit this job
    command="sbatch control" + str(i) + ".sbatch"
    
    os.system(command)
    #now leave this subfolder 
    os.chdir(directory)