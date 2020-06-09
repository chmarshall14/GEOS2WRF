#!/bin/bash

#SBATCH --nodes=1
#SBATCH --job-name=wget_MET1
#SBATCH --output=wget_MET1.out
#SBATCH --error=wget_MET1.err
#SBATCH --time=20:00:00
#SBATCH --mem=10GB
#SBATCH --ntasks-per-node=10
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END
#SBATCH --mail-user=cm5515@nyu.edu

cd /scratch/cm5515/storm_20050813/MET1

wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_MET1
