Import("env")
import os
import shutil

custom_device_path = "CustomDevices_own/Gagagu/Community"


# Get the version number from the build environment.
firmware_version = os.environ.get('VERSION', "")

def copy_fw_files (source, target, env):
    fw_file_name=str(target[0])

    if os.path.exists(custom_device_path + "/firmware") == False:
        os.mkdir(custom_device_path + "/firmware")
    
    if fw_file_name[-3:] == "bin":
        fw_file_name=fw_file_name[0:-3] + "uf2"

    shutil.copy(fw_file_name, custom_device_path + "/firmware")
    pass



env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", copy_fw_files)
env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", copy_fw_files)
