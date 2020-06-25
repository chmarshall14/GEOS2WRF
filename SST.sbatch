#!/bin/bash 
#SBATCH --nodes=1 
#SBATCH --job-name=GEOS_SST 
#SBATCH --output=GEOS_SST.out 
#SBATCH --error=GEOS_SST.err
#SBATCH --time=1:00:00
#SBATCH --mem=80GB
#SBATCH --ntasks-per-node=10
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END
#SBATCH --mail-user=cm5515@nyu.edu
cd /scratch/cm5515/storm_20050813/MET2
srun ./geos2wps