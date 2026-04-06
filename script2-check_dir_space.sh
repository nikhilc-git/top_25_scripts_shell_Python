#!/bin/bash

usage(){
	echo "Usage: script.sh </> <80>"
}

if [[ $# -ne 2 ]]; then
	echo "Please provide the mount point and threshold."
	usage
	exit 1
fi

mnp="$1"
th="$2"

#echo $mnp
#echo $th

DISK=$(df -h | awk '$NF=="/" {gsub("%","",$5);print $5}')

if [[ $DISK -ge $th ]]; then
	echo -e "WARNING: / disk usage exceeds the threshold.\nActual Disk:$DISK%\nThreshold:$th%"

else
	echo -e "INFO:/ disk usage is within the thrshold.\nActual Disk:$DISK%\nThreshold:$th%"
fi	
