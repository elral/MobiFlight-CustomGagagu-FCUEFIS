#! /bin/bash

custom_device_path='/CustomDevices_own/Gagau'
zip_file_name='gagagu_fcu_efis'

mkdir /CustomDevices_own/Gagau/Community/firmware
cp -r .pio/build/**/*.hex /CustomDevices_own/Gagau/Community/firmware
cp -r .pio/build/**/*.uf2 /CustomDevices_own/Gagau/Community/firmware
cd /CustomDevices_own/Gagau/Community
zip -r -qq gagagu_fcu_efis_$VERSION.zip *
