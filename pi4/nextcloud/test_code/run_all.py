import nextcloud_client

from myconfig import *
nc = nextcloud_client.Client('http://drive.finishyourproduct.com/nextcloud')

nc.login(username, password)


nc.put_file(piDash1 + "testdir/remotefile.txt", 'localfile.txt')

