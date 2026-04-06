#!/bin/bash


usage(){
	echo "Usage: script.sh <log file path>"
}

if [[ $# -ne 1 ]]; then
	echo "Please pass the log file with the script."
	usage
	exit 1
fi

LOG_FILE="$1"

if [[ ! -f $LOG_FILE ]]; then
	echo "Log file not found."
	exit 1
fi

ERROR_COUNT=$(grep -c "ERROR" $LOG_FILE)

if [[ $ERROR_COUNT -gt 0  ]]; then
	echo "$ERROR_COUNT erros found the the log file provided."
	echo -e "Moving that erro log lines to temp file debugging\n"

	grep "ERROR" $LOG_FILE >> /root/app-error.log

	if [[ $? -eq 0 ]]; then
		echo "ERROR logs has been copied to error log file successfully."
	else
		echo "Error in coping the logs."
	fi

else
	echo "No erros in the $LOG_FILE."
fi
