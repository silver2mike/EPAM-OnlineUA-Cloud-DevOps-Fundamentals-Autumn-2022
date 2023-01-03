#!/bin/bash
### count max number of request from IP ###
#
#  Usage ./log-checker.sh [file name]
#
#

if [ $1 eq "" ] || [ ! -f $1 ];
then
	echo "Error! File doesn't exit or not specified"
fi

NUM1=`cat $1 | awk '{ print $1 }' | sort | uniq -c | sort -n | tail -1 | awk '{ print $1 }'`
IP=`cat $1 | awk '{ print $1 }' | sort | uniq -c | sort -n | tail -1 | awk '{ print $2 }'`

echo "There are $NUM1 requests from IP: $IP"

echo -e  "\n\nThe most 10 visited pages are:"
cat $1 | awk '{ print $7 }' | sort | uniq -c | sort -n | tail -10 | awk '{ print $2 }'

echo "------------------"
echo "Requests |   IP address"
cat $1 | awk '{ print $1 }' | sort | uniq -c | sort -n | awk '{printf("%4s%20s\n", $1, $2)}'

echo "------------------"
echo "Non existen pages"
cat $1 | awk '{ print $7 " " $9 }' | grep ' 404' | uniq |column -t


echo "------------------"
echo "The most visited time"
cat $1 | awk '{ print $4 }' | uniq -c | cut -c 22-26 | uniq -c | sort -n | tail -1

echo "------------------"
echo "Search bots"
cat $1 | awk '{ print $1 " - " $12 $13 $14 $15 $16 $17 }' | grep bot | sort | uniq -c | sort -n
