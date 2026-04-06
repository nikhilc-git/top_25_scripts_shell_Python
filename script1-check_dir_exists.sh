#!/bin/bash

#Check of dir is exists
#If dir is exists then check files and folders inside it 
#Else create the dir

################################################################

set -eou pipefail

usage(){
	echo "Usage:: script.sh <dir path>"
}

if [[ $# -eq 0 ]]; then
	echo "Please pass the dir name to check."
	usage
	exit 1
fi

DIR_PATH="$1"

if [[ -d "$DIR_PATH" ]]; then
	echo "Dir $DIR_PATH is exists."
	num_content=$(find "$DIR_PATH" -maxdepth 1 -type f | tail -n +2 | wc -l)
	echo "Number of files in the given dir:$num_content"

else
	echo "Creating the dir..."
	mkdir $DIR_PATH
	echo "Dir $DIR_PATH has been created."
fi

