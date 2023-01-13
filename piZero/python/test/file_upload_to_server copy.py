import nextcloud_client
from myconfig import *
nc = nextcloud_client.Client(driveUrl)

nc.login(piDash0_username, piDash0_pass)



nc.put_file(piDash0_localPath + '/test.txt', 'test.txt')

#link_info = nc.share_file_with_link(piDash0_localPath + '/test.txt')

#print("Here is your link: " + link_info.get_link())