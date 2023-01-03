#!/bin/bash

if [ ! -d "$1" ] || [ ! -d "$2" ]; then
 echo "****************************************************"
 echo "* Use ./script.sh [Source path] [Destination path] *"
 echo "*                                                  *"
 echo "* Log is stored /var/log/syncro.log                *"
 echo "****************************************************"

 exit -1
fi

src=$1

dat=$(date +"%D")
tim=$(date +"%T")

echo "---------------------------------------------------------" | tee -a /var/log/syncro.log
echo "Sync process from $1 to $2" | tee -a /var/log/syncro.log
echo "Script run $dat at $tim" | tee -a /var/log/syncro.log

if [ ${src: -1} != "/" ]; then
 src=$src/
fi

rsync -avu --delete $src $2 | tee -a /var/log/syncro.log

diff -qr $1 $2
