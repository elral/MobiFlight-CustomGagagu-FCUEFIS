Import("env")
import os, zipfile, shutil


custom_device_path = "CustomDevices_own/Gagagu"
zip_file_name = "gagagu_fcu_efis"

# Get the version number from the build environment.
firmware_version = os.environ.get('VERSION', "")
if firmware_version == "":
  firmware_version = "0.0.1"
firmware_version = firmware_version.lstrip("v")
firmware_version = firmware_version.strip(".")


def copy_fw_files (source, target, env):
#    if firmware_version == "0.0.1":
#        return

    fw_file_name=str(target[0])

    if os.path.exists(custom_device_path + "/Community/firmware") == False:
        os.mkdir(custom_device_path + "/Community/firmware")
    
    if fw_file_name[-3:] == "bin":
        fw_file_name=fw_file_name[0:-3] + "uf2"

    shutil.copy(fw_file_name, custom_device_path + "/Community/firmware")
    createZIP()


def createZIP():
    complete_ZIP_Filename = custom_device_path + '/' + zip_file_name + '_' + firmware_version + '.zip'
    with zipfile.ZipFile(complete_ZIP_Filename, 'w', zipfile.ZIP_DEFLATED) as target:
        for root, dirs, files in os.walk(custom_device_path + "/Community"):
            for file in files:
                add = os.path.join(root, file)
                target.write(add)


env.AddPostAction("$BUILD_DIR/${PROGNAME}.hex", copy_fw_files)
env.AddPostAction("$BUILD_DIR/${PROGNAME}.bin", copy_fw_files)
