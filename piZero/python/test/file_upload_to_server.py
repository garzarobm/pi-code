import nextcloud_client
from myconfig import *

#local variables
file_name="test.txt"
nc = nextcloud_client.Client(driveUrl)

#logging in 
print("logging in...\n")
nc.login(piDash0_username, piDash0_pass)


print("sending test file " + file_name + " now to: " + piDash0_USBPath)
nc.put_file(piDash0_USBPath + '/' + file_name, file_name)

#link_info = nc.share_file_with_link(piDash0_localPath + '/test.txt')

#print("Here is your link: " + link_info.get_link())