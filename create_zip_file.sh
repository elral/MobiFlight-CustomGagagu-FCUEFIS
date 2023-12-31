#! /bin/bash

custom_device_path='CustomDevices_own/Gagagu/Community'
zip_file_name='gagagu_fcu_efis'



cd "$custom_device_path"
zip -r -qq "$zip_file_name"_"$VERSION".zip *
