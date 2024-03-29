# CGEM
Implementing CGEM in SCHISM.

- [CGEM-SCHISM Status Report](CGEM-SCHISM-Report.pdf) (11/11/2023)

## Running CGEM on Expanse

[General Notes](cgem-dev.md)


### Python and R libraries

If you are in the OyBcSt Expanse group, you should have access to my 'cgem' module, containing pylibs, r-netcdf, f90nml, and the nco operators.  To use, do
```
module use --append /home/llowe/modulefiles
module load cgem
```

To avoid complications, I recommend creating your own modulefiles.  Content of my module files are available in this repository.

### VisIt

To use VisIt, you must install the SCHISM plugin locally and set up client-server mode for Expanse.  Instructions are on Expanse:
```
more /cm/shared/examples/sdsc/visit/README
```

The plugin must also be installed on Expanse.  You can install the plugins by following [these instructions](https://github.com/schism-dev/schism_visit_plugin/blob/master/install-expanse.md) or, (for OyBcSt members), by copying my plugins to your home directory:
```
cd ~
cp -r /home/llowe/.visit .
ls -a
```

See [visit-scripts](https://github.com/l3-hpc/visit-scripts/blob/main/README.md) for mini-tutorials and links to videos. 

## Contents
Files in the main repo:
- [cgem.nml](cgem.nml) - namelist for CGEM used in LSC2 runs
- [param.nml](param.nml) - namelist for SCHISM used in LSC2 runs
- [write_initial_conditions.py](write_initial_conditions.py) - writes simple initial condition files for CGEM according to cgem.nml
- [PYTHON](PYTHON.MD) - instructions for installing pyschism and pylibs
- env_schism.yml, pyschism.module, env_pylibs.yml, pylibs.module - conda environments and custom modules for pyschism and pylibs
- [rm.sh](rm.sh) - to remove garbage without accidentally deleting important stuff, `source rm.sh`
- [clean.sh](clean.sh) - to remove garbage **and** everything in the *outputs* directory.
- [listplot.R](listplot.R) - little R function to make plots based on Rdat files created with Reformat_cgem.R
- [Reformat_cgem.R](Reformat_cgem.R) - reformats extracted netCDF timeseries files into R databases (rdat files) for plotting and using with Shiny
- [cosine](cosine.md) - notes for compiling cosine, and how I created the param.nml and chose initial values
- [write_initial_conditions_cosine.py](write_initial_conditions_cosine.py) - writes simple initial condition files for COSINE
- [TryCOSINE](TryCOSINE.md) - Link to the video instructions for trying COSINE, with written description of video and list of commands used
- [write_submit_nco.py](write_submit_nco.py) - writes a SLURM submission script for extracting a timeseries from each node as defined in setvars.py.
- [setvars.py](setvars.py) - sets paths, variables, nodes, layers, year, debug flags for files in this directory
- [shiny_extract_one.py](shiny_extract_one.py) - extract time series, rename, and add attributes, use when there is only 1 GEN file, GEN_X_1.nc, takes command line argument, which_node to extract
- [shiny_extract_all.py](shiny_extract_all.py) - extract time series, rename, and add attributes, used to extract from all GEN files in the directory, GEN_X_*.nc, takes command line argument, which_node to extract
- and there are a bunch of submit scripts for the above.  Read [cgem-dev](cgem-dev.md).

Files in **visit** directory, in approximate order of use:
- [setpaths.py](visit/setpaths.py) - Set your paths.  Follow the instructions.
- [cgem_vars.py](visit/cgem_vars.py) - Defines a list of CGEM parameters with default names and colormap settings.  To run scripts with a smaller subset of variables, redefine cgem_vars.
- [databases.py](visit/databases.py) - Creates .visit files, (VisIt databases), which are text files listing all files to be included as a single 'variable'.  As it simply writes a file, `python databases.py` will work without needing to load a module.
- [parallel_plot_cgem.py](visit/parallel_plot_cgem.py) - Creates types of plots as specified in cgem_vars, but the variables to be plotted are chosen by command line argument, an integer between 0 and 29 (for 30 state variables).  If USE_DB is False, only _1.nc will be plotted.
- [s2p_commands.txt](visit/s2p_commands.txt) - ser2par looks for this file, containing commands to give each processor.  Number of commands should equal number of cores requested.
- [s2p_commands.txt.all](visit/s2p_commands.txt.all) - This lists all possible commands, to have a saved copy in case you modify s2p_commands.txt to plot only a couple variables
- [s2p_run.csh](visit/s2p_run.csh) - submit script for running the plots in serial.  To use, compile ser2par and place executable in this directory.  Instructions are in [cgem-dev](cgem-dev.md).
- [ffmpeg.py](visit/ffmpeg.py) - Script to create a movie for each image that should have been created if you successfully ran the plotting scripts with the current settings of setpaths and cgem_vars
- [submit_ffmpeg.sh](visit/submit_ffmpeg.sh) - submit script for running ffmpeg.py
- [rm.sh](visit/rm.sh) - to remove garbage without accidentally deleting important stuff, `source rm.sh`
- [plot_schism_cgem.py](visit/plot_schism_cgem.py) - Creates all plots as specified in cgem_vars.  I use the parallel one, and have not tested this one in a while.
- [l3v.py](visit/l3v.py) - Python 'library' that defines VisIt macros.  Only used for plot_schism_cgem.py.

## Preprocessing
Python script [write_initial_conditions.py](write_initial_conditions.py) writes initial condition files(GEN...ic) required to run SCHISM.  To use:
```
python write_initial_conditions.py
```
Requires the following libraries: pylib, f90nml, FileInput

The grid file hgrid.gr3 needs to be in the current working directory(CWD), as does cgem.nml.  Output is also written to CWD.

# Thank you!
*This work is funded by the National Oceanic and Atmospheric Administration's RESTORE Science Program under award NA19NOS4510194.*
