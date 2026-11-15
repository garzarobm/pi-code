from webdav3.client import Client
import os

# Credentials come from the environment — see "Credentials" in README.md:
#   export WEBDAV_HOSTNAME="https://your-server/nextcloud/remote.php/dav/files/youruser/"
#   export WEBDAV_LOGIN="youruser"
#   export WEBDAV_PASSWORD="yourpassword"
options = {
 'webdav_hostname': os.environ["WEBDAV_HOSTNAME"],
 'webdav_login':    os.environ["WEBDAV_LOGIN"],
 'webdav_password': os.environ["WEBDAV_PASSWORD"],
}
client = Client(options)
