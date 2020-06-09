#!/bin/bash

#SBATCH --nodes=1
#SBATCH --job-name=wget_PL
#SBATCH --output=wget_PL.out
#SBATCH --error=wget_PL.err
#SBATCH --time=20:00:00
#SBATCH --mem=10GB
#SBATCH --ntasks-per-node=10
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END
#SBATCH --mail-user=cm5515@nyu.edu

cd /scratch/cm5515/storm_20050813/PL

wget --retry-connrefused --waitretry=1 --read-timeout=20 --timeout=15 -t 0 -i wget_PL
