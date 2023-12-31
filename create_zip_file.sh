#! /bin/bash

custom_device_path='CustomDevices_own/Gagagu'
zip_file_name='gagagu_fcu_efis'

cd "$custom_device_path"/Community
zip -r -qq "$zip_file_name"_"$VERSION".zip *
