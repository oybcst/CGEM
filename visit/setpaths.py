#setpaths.py
##--Set path to scripts----
##On my Mac:
#SCRIPT_PATH = "/Users/lllowe/visit-scripts"
#On Hazel:
SCRIPT_PATH = "/expanse/lustre/scratch/llowe/temp_project/CGEM/visit"

#Put the full path, followed by '/'
#SCHISM outputs here: 
##On my Mac:
OUTPUTS = "/expanse/lustre/scratch/llowe/temp_project/cgem-SA/outputs_nosink_noflux/" 

FILENAME = "TPtot.nc"
#FILENAME = "leem_0001.nc"
#OUTPUTS = "/Users/lllowe/SASJ/outputs/"
#On Hazel:
#OUTPUTS = "/rsstu/users/l/lllowe/cgem/schism_sa_CGEM_test/outputs/"
#OUTPUTS = "/rsstu/users/l/lllowe/cgem/cgem-real/outputs/"

#Or use databases (*.visit files)
USE_DB = True 
#True 
#DBFILES are *.visit files containint names of outputfiles
#ignore if USE_DB = False
DBFILES = "/expanse/lustre/scratch/llowe/temp_project/CGEM/visit/databases/"

#Main path to images
##On Expanse 
IMAGES = "/expanse/lustre/scratch/llowe/temp_project/imgs-cgem-nosink-noflux/"
#IMAGES = "/Users/lllowe/SASJ/images/"
#On Hazel:
#IMAGES = "/rsstu/users/l/lllowe/tops/images_sasj_mocsy/"
#IMAGES = "/rsstu/users/l/lllowe/tops/images_cgem-sa/"
