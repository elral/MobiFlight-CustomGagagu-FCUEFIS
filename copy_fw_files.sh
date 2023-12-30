#! /bin/bash

my_custom_path=CustomDevices_own/Gagau
my_custom_name=gagagu_fcu_efis

mkdir $my_custom_path/Community/firmware
cp -r .pio/build/**/*.hex $my_custom_path/Community/firmware
cp -r .pio/build/**/*.uf2 $my_custom_path/Community/firmware
cd $my_custom_path/Community
zip -r -qq $my_custom_name_$VERSION.zip *
