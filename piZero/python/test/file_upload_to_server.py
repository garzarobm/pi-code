import nextcloud_client
from myconfig import *
nc = nextcloud_client.Client('https://drive.finishyourproduct.com/nextcloud')

nc.login(piDash0_username, piDash0_pass)



nc.put_file(piDash0_localPath + '/remotefile.txt', 'test.txt')

