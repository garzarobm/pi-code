from webdav3.client import Client
import os

options = {
 'webdav_hostname': "https://drive.finishyourproduct.com/nextcloud/remote.php/dav/files/garzarobm/",
 'webdav_login':    "garzarobm",
 'webdav_password': "Lordking1!"
 'webdav_password': os.environ["WEBDAV_PASSWORD"],
  }
client = Client(options)
