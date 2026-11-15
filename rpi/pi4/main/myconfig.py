# Credentials come from the environment — never commit them to git.
# Set them in your shell (or a systemd service / ~/.profile on the Pi):
#
#   export NEXTCLOUD_USER="youruser"
#   export NEXTCLOUD_PASSWORD="yourpassword"
#   export NEXTCLOUD_PUBLIC_LINK="https://your-server/nextcloud/index.php/s/XXXXXXXX"
#
import os

username = os.environ.get("NEXTCLOUD_USER", "")
password = os.environ.get("NEXTCLOUD_PASSWORD", "")
publicLink = os.environ.get("NEXTCLOUD_PUBLIC_LINK", "")

piDash1 = "DashCam/piDash1/"
piDash0 = "DashCam/piDash0/"
