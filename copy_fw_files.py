Import("env")
import os
#import subprocess
import shutil

dirname = "CustomDevices_own/Gagagu/Community"
# Get the version number from the build environment.
firmware_version = os.environ.get('VERSION', "")

def copy_fw_files (source, target, env):
    if os.path.exists(dirname + "/firmware") == False:
        os.mkdir(dirname + "/firmware")
    
    shutil.copy(str(target[0]), dirname + "/firmware")
    pass

#def create_zip_folder (source, target, env):
#    os.chdir(dirname)
#    subprocess.run(["zip", "-r -qq gagau_fcu_efis_" + firmware_version + ".zip *"])
#    pass

env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", copy_fw_files)
env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", copy_fw_files)
