#!/bin/sh
while true
do
    sleep 15
    wget -q http://192.168.100.19:8001/ -O /dev/null
done
