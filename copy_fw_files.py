Import("env")
import os
import subprocess
import shutil


# Get the version number from the build environment.
firmware_version = os.environ.get('VERSION', "")

#dirname = os.environ['HOME'] + "CustomDevices_own/Gagagu/Community/firmware"
dirname = "CustomDevices_own/Gagagu/Community/firmware"
os.mkdir(dirname)

#source = os.environ['HOME'] + ".pio/build/**/*.hex"
source = ".pio/build/gagagu_fcu_efis_mega/*.hex"
#target = os.environ['HOME'] + "CustomDevices_own/Gagagu/Community/firmware"
target = "CustomDevices_own/Gagagu/Community/firmware"
shutil.copy(source, target)

#source = os.environ['HOME'] + ".pio/build/**/*.uf2"
source = ".pio/build/gagagu_fcu_efis_raspberrypico/*.uf2"
shutil.copy(source, target)

os.chdir("CustomDevices_own/Gagagu/Community")

subprocess.run(["zip", "-r -qq gagau_fcu_efis_" + "firmware_version" + ".zip *"])





# mkdir $custom_device_path/Community/firmware
# cp -r .pio/build/**/*.hex $custom_device_path/Community/firmware
# cp -r .pio/build/**/*.uf2 $custom_device_path/Community/firmware
# cd "$custom_device_path"/Community
# zip -r -qq "$zip_file_name"_"$VERSION".zip *
