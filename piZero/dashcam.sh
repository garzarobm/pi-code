#!/bin/bash

# set variable form the date 
when=$(date)

# make sure dashcam.log is present touch dashcam.log
if [ -e dashcam.log ]
then
    echo "found previous dashcam.log"
else
    echo "no dashcam log file \n creating one now"
    touch  dashcam.log
fi
# mv the current video to the same name but with the date added  
if [ -e dashcam.flv ]
then
    echo "found previous recording"
    mv dashcam.flv $(date+%F-%H:%M).dashcam.flv

else
    echo "no previous video found \n starting dashcam"
fi
mv dashcam.flv $(date+%F-%H:%M).dashcam.flv

# log to dashcam.log every time the service is started 
echo "Started at: $when" >> dashcam.log

# record at 1024x760 with a Desktop preview window of 640x480, pipe to ffmpeg and output dashcam.flv 
raspivid -t 0 -w 1024 -h 760 -fps 25 -b 5000000 -p 0,0.640,480 -vf -o - | ffmpeg -i - -vcodec copy -an -f flv -r 25 -pix_fmt yuv420p dashcam.flv -y