#!/bin/bash

#start upload file
/bin/bash /home/pi/Desktop/pi-code/piZero/dashcam.sh

# remove files older than 3 days
#find /home/pi/Desktop/DashVideos -type f -iname '*.flv' -mtime +3 -exec rm {} \;

# start dashcam service 
#sudo systemctl start dashcam



