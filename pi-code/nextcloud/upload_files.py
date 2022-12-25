#!/usr/bin/env python
from myconfig import *
import nextcloud_client

import os
import shutil

ROOT_PATH = os.getenv("ROOT_PATH", "/home/pi")
RECORDINGS_PATH = os.getenv("RECORDINGS_PATH", "recordings")
UPLOADED_RECORDINGS_PATH = os.getenv("UPLOADED_RECORDINGS_PATH", "uploaded")
PERCENTAGE_THRESHOLD = 25.0

statvfs = os.statvfs(ROOT_PATH)

free_bytes = statvfs.f_frsize * statvfs.f_bfree
total_bytes = statvfs.f_frsize * statvfs.f_blocks

free_bytes_percentage = ((1.0 * free_bytes) / total_bytes) * 100

#if free_bytes_percentage < PERCENTAGE_THRESHOLD:
recordings_path = os.path.join(ROOT_PATH, RECORDINGS_PATH)

recordings = []
for dir_name in os.listdir(recordings_path):
    recording_path = os.path.join(recordings_path, dir_name)
    recordings.append((recording_path, os.stat(recording_path).st_mtime))
#sorting according to name
recordings.sort(key=lambda tup: tup[1])



nc = nextcloud_client.Client('http://drive.finishyourproduct.com/nextcloud')
nc.login(username, password)
for recordingFolder in recordings:
    print(recordingFolder)
    for file_name in os.listdir(recordingFolder[0]):
        cloud_path = os.path.join(piDash1,recordingFolder[0],file_name)
        pi_path=os.path.join(ROOT_PATH,RECORDINGS_PATH,recordingFolder[0],file_name)
        print("pi path =" +  pi_path)
        finished_pi_path=os.path.join(ROOT_PATH,RECORDINGS_PATH,UPLOADED_RECORDINGS_PATH)
        nc.put_file(cloud_path,pi_path)
        print("placed" + file_name + "in cloud") 
        subprocess.call(["mv", pi_path, finished_pi_path])

