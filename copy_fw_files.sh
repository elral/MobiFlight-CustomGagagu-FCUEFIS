#! /bin/bash

custom_device_path='CustomDevices_own/Gagau'
zip_file_name='gagagu_fcu_efis'

mkdir $custom_device_path/Community/firmware
cp -r .pio/build/**/*.hex $custom_device_path/Community/firmware
cp -r .pio/build/**/*.uf2 $custom_device_path/Community/firmware
cd /CustomDevices_own/Gagau/Community
zip -r -qq $zip_file_name_$VERSION.zip *
