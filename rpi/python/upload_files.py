#!/usr/bin/env python
import sys
sys.path.insert(0, '/mnt/c/Users/Mike/Documents/esp/dashCam/pi-code/piZero/python/test')
#user config
from myconfig import *
#print(piDash0_USBPath)

import nextcloud_client

import subprocess
import os
import shutil

ROOT_PATH = os.getenv("ROOT_PATH", "/home/pi")
RECORDINGS_PATH = os.getenv("RECORDINGS_PATH", "Desktop/Videos/recordings")
UPLOADED_RECORDINGS_PATH = os.getenv("UPLOADED_RECORDINGS_PATH", "uploaded")
PERCENTAGE_THRESHOLD = 25.0

'''
statvfs = os.statvfs(ROOT_PATH)

free_bytes = statvfs.f_frsize * statvfs.f_bfree
total_bytes = statvfs.f_frsize * statvfs.f_blocks

free_bytes_percentage = ((1.0 * free_bytes) / total_bytes) * 100

#if free_bytes_percentage < PERCENTAGE_THRESHOLD:
'''
#getting local recordings path
recordings_path = os.path.join(ROOT_PATH, RECORDINGS_PATH)

recordings = []
for dir_name in os.listdir(recordings_path):
    recording_path = os.path.join(recordings_path, dir_name)
    recordings.append((recording_path, os.stat(recording_path).st_mtime))
#sorting according to name
recordings.sort(key=lambda tup: tup[1])

print(recordings)

#nextcloud login
#nc = nextcloud_client.Client('http://drive.finishyourproduct.com/nextcloud')
#nc = nextcloud_client.Client('https://192.168.1.213/nextcloud')
#nc.login(username, password)
nc = nextcloud_client.Client(driveUrl)
print("logging in")
nc.login(piDash0_username, piDash0_pass)
print("logged in\n")

for file_info in recordings:
    local_file_path=file_info[0]
    file_name= str(file_info[0]).split("/",-1)[-1]
    file_ending=file_name.split('.', -1)[-1]

    print("looking into " + file_name + " with file_ending " + file_ending + " at "+ local_file_path)
    if file_ending == ".flv":
        print("file_name: " + file_name)
        cloud_file_path = piDash0_USBPath + "/" + str(file_name)
        print("cloud fp: " + cloud_file_path)
        local_finished_dir_path=os.path.join(ROOT_PATH,RECORDINGS_PATH,UPLOADED_RECORDINGS_PATH)

        #uploading file to cloud
        nc.put_file(cloud_file_path, local_file_path)
        print("placed " + local_file_path + " in cloud")
        #place uploaded file in created directory
        #os.mkdir(local_finished_dir_path)
        #print("created dir " + local_finished_dir_path)

        #moving local file to uploaded folder once processed
        subprocess.call(["mv", local_file_path, local_finished_dir_path])
        print("moved " + local_file_path + " to " + local_finished_dir_path)
    else:
        print("skipping file/folder " + file_name +   " with file_ending: " + local_file_path  + "\n\n\n")

   
    '''
    for file_name in os.listdir(recordingFolder[0]):
        #cloud_path = os.path.join(piDash0_USBPath,recordingFolder[0],file_name)
        
        local_dir_path=os.path.join(ROOT_PATH,RECORDINGS_PATH,recordingFolder[0])
        file_path=os.path.join(dir_path,file_name)
        print("dir_path" + local_dir_path)

        #placing file in
        nc.put_file(piDash0_USBPath+"/" + file_path, local_dir_path)



        #zipping up files
        #command = "zip -r " + dir_path + ".zip " + dir_path 
        #subprocess.call(["zip", "-r", dir_path + ".zip",dir_path]) 
        #next cloud


        #through public link
        #nc = nextcloud_client.Client.from_public_link(publicLink)
        #nc.drop_file(dir_path+".zip")

        ###placing through login
        #nc = nextcloud_client.Client('http://drive.finishyourproduct.com/nextcloud')

        
        #link_info = nc.share_file_with_link(cloud_path+".zip")
        #print("Here is your link:"  + link_info.get_link())

        finished_dir_path=os.path.join(ROOT_PATH,RECORDINGS_PATH,UPLOADED_RECORDINGS_PATH, recordingFolder[0])
        os.mkdir(finished_dir_path)
        print("created dir " + finished_dir_path)
        subprocess.call(["mv", pi_path, finished_pi_path])
        print("placed" + file_name + "in cloud") 
    '''