#! /bin/bash

mkdir CustomDevices_own/Gagagu/Community/firmware
cp -r .pio/build/gagagu_fcu_efis_mega/*.hex CustomDevices_own/Gagagu/Community/firmware
cp -r .pio/build/gagagu_fcu_efis_raspberrypico/*.uf2 CustomDevices_own/Gagagu/Community/firmware
cd CustomDevices_own/Gagagu/Community
zip -r -qq gagagu_fcu_efis_0.1.0.zip *
