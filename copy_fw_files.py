Import("env")
import os
import subprocess
import shutil

dirname = "CustomDevices_own/Gagagu/Community"
# Get the version number from the build environment.
firmware_version = os.environ.get('VERSION', "")

def copy_fw_files (source, target, env):
    print(f'Creating folder')
    os.mkdir("CustomDevices_own/Gagagu/Community" + "/firmware")
    print(f'Copy files')
    shutil.copy(str(target[0]), "CustomDevices_own/Gagagu/Community" + "/firmware")
    pass

def create_zip_folder (source, target, env):
    os.chdir(dirname)
    #subprocess.run(["zip", "-r -qq gagau_fcu_efis_" + firmware_version + ".zip *"])
    print(f'Creating ZIP file')
    pass

env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", [copy_fw_files, create_zip_folder])
