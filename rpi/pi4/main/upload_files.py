#!/usr/bin/env python
from myconfig import *
import nextcloud_client

import subprocess
import os
import shutil
import os
import easywebdav
from wallhaven.api import Wallhaven
import tempfile
# Settings Webdav





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





####PING SERVERS
#webdav
#webdav = easywebdav.connect('webdav.robjects.me', username='homeconnections', password='7DhL#*/$', protocol='https', port=443,
                            verify_ssl=True)

#nextcloud login
#nc = nextcloud_client.Client('http://drive.finishyourproduct.com/nextcloud')
#nc = nextcloud_client.Client('https://192.168.1.213/nextcloud')
#nc.login(username, password)
for recordingFolder in recordings:
   # print("--> "recordingFolder[0])
    for file_name in os.listdir(recordingFolder[0]):
        cloud_path = os.path.join(pi,recordingFolder[0],file_name)
    
        dir_path=os.path.join(ROOT_PATH,RECORDINGS_PATH,recordingFolder[0])
        file_path=os.path.join(dir_path,file_name)
        print("dir_path" + dir_path)

        #zipping up files
        command = "zip -r " + dir_path + ".zip " + dir_path 
        subprocess.call(["zip", "-r", dir_path + ".zip",dir_path]) 
        #next cloud
        ####################BOOKMARK######
        #after login, webdave needs to 1 check exists & is folder and log if exists (add printing 2. place the file securely and transfer (check not corrupted possibly) 3. place files to webdav location

        import easywebdav
        # Start off by creating a client object. Username and
        # password may be omitted if no authentication is needed.

        #TODO: Step 0 - initializing and connecting
        # DO BASIC ENCRYPTION OF FILES VIA SUBPROCESS





        #`111111111111111111111111
        #webdav = easywebdav.connect('webdav.your-domain.com', username='myuser', password='mypass')


        webdav_path =  webdav.cd('/home/pi')
        #if does not exist, then create folder 1. otherwise continue
        # check last folder created and create next to add to stack.
        # upload file through public
        webdav.mkdir('')
        webdav.rmdir('another_dir')
        webdav.download('remote/path/to/file', 'local/target/file')
        webdav.upload('local/path/to/file', 'remote/target/file')


        #####nextcloud only
        #through public link
        #nc = nextcloud_client.Client.from_public_link(publicLink)
        #nc.drop_file(dir_path+".zip")
        #nc = nextcloud_client.Client('http://drive.finishyourproduct.com/nextcloud')
        #nc.login(username, password)
        #nc.put_file(cloud_path+".zip",dir_path+".zip")
        #link_info = nc.share_file_with_link(cloud_path+".zip")



        #grab link_info and print 2 and print 2
        #print("Here is your link:"  + link_info.get_link())

        #3 - upload file and log uploaded to txt
        finished_dir_path=os.path.join(ROOT_PATH,RECORDINGS_PATH,UPLOADED_RECORDINGS_PATH, recordingFolder[0])
        os.mkdir(finished_dir_path)
        print("created dir " + finished_dir_path)
        subprocess.call(["mv", pi_path, finished_pi_path])
        print("placed" + file_name + "in cloud") 


       ############END OF BOOKMARK 
