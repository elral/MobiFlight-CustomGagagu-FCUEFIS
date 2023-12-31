Import("env")
import os
#import subprocess
import shutil

dirname = "CustomDevices_own/Gagagu/Community"
# Get the version number from the build environment.
firmware_version = os.environ.get('VERSION', "")

def copy_fw_files (source, target, env):
    fw_file_name=str(target[0])
    print("Endung ist: " + fw_file_name[-3:])

    if os.path.exists(dirname + "/firmware") == False:
        os.mkdir(dirname + "/firmware")
    
    if fw_file_name[-3:] == "bin":
        fw_file_name=fw_file_name[0:-3] + "uf2"

    shutil.copy(fw_file_name, dirname + "/firmware")
    pass

#def create_zip_folder (source, target, env):
#    os.chdir(dirname)
#    subprocess.run(["zip", "-r -qq gagau_fcu_efis_" + firmware_version + ".zip *"])
#    pass


env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", copy_fw_files)
env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", copy_fw_files)
