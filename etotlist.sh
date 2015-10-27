#!/bin/bash
a=`ls -l |grep ^d|awk '{print($8)}'`
for i in $a
do
	cd $i
	if [ -e Log.txt ]; then
		cd OUT.*
		etot=`sed -n '/!FINAL_ETOT_IS/p' running* |awk '{print($2)}'`
		cd ..
	fi
	cd ..
	echo "$i $etot" >> etotlist.dat
done
