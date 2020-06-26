# GEOS2WRF

You will have to change the directory paths in these scripts to use them. It also assumes you have GEOS2WRF and WRF-4.0 compiled on your system. 

Below is a log of how each of the scripts work. To run this (after you have changed the directory paths in the scripts), the only thing you should regularly have to edit is the namelist.geos_scripts, which allows you to change the start and end times of your storms. From there, 

These are python scripts that take a start date and end date and time as inputs, then download the necessary data files from NASA and process them using GEOS2WPS and the utilities createLANDSEA, createRH, and createSOILHGT. 

The scripts are broadly organized into four sections: a series of download scripts, a series of scripts that run geos2wps, scripts that run utilities, and a script that concatenates all the required fields to prepare files that are ready to be used by Metgrid. There are high level scripts to run all four of these sub-sections.

The download scripts: There is a single download script called ‘download_wrapper” that should download every file you need given an start and end time. It also organizes the files into a storm_startdate with subfolders for each field. 

The processing scripts: The scripts named GEOS_<filename> run geos2wps on each file you have downloaded, and the scripts named create<utility> run createRH, createLANDSEA and createSOILHGT. These scripts are broken up by GEOS file to be processed, there is one for each downloaded file. They link in the executable geos2wps, create a namelist and run geos2wps for each time step.   The wrapper script GEOS_wrapper runs all of these.
  

Once you have processed all of the fields in geos2wps, you can run the utility scripts that concatenate the files you need into a geos:timestamp file and run the utility executable. The util_wrapper automates this process. 

The concatenation script: once everything is done, you can move all of the files you have processed into the same folder (the wraparound script I am writing will do this for you), and catGEOS.py will get everything you need into the files GEOS:TIMESTAMP to be ready to be used by metgrid. The cat_wrapper automates this, as well as creates a single SST file you can input as a constant into WPS. 
