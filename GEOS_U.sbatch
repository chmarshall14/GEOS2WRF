#!/bin/bash

#SBATCH --nodes=1
#SBATCH --job-name=GU
#SBATCH --output=GU.out
#SBATCH --error=GU.err
#SBATCH --time=5:00:00
#SBATCH --mem=100GB
#SBATCH --ntasks-per-node=10
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END
#SBATCH --mail-user=cm5515@nyu.edu

cd /scratch/cm5515/scripts
module load openmpi/intel/3.1.3
module load intel/17.0.1
module load openmpi/intel/3.1.3
module load netcdf/intel/4.4.1.1
module load libpng/intel/1.6.29
module load jasper/intel/2.0.14
module load openjpeg/intel/2.1.2
module load zlib/intel/1.2.8
module load hdf5/intel/1.8.21
module load szip/intel/2.1.1
module load hdf/intel/4.2.12
module load hdf/intel/4.2.6
module load netcdf/intel/4.1.1
module load zlib/intel/1.2.8
module load jpeg/intel/9b
module load python3/intel/3.7.3

python GEOS_U.py &> log.GU

