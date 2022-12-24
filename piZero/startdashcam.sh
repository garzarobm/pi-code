#!/bin/bash

# remove files older than 3 days
find /home/pi/Desktopvideo -type f -iname '*.flv' -mtime +3 -exec rm {} \;

# start dashcam service
sudo systemctl start dashcam