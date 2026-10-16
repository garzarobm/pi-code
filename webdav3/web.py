[200~import os
import easywebdav
from wallhaven.api import Wallhaven
import tempfile
# Settings Webdav


webdav = easywebdav.connect('192.168.1.40', username='Uri3l', password='mypassword', protocol='http', port=80,
                            verify_ssl=False)

webdav.cd(Wallhaven)
results = wallhaven.search()

with tempfile.TemporaryDirectory() as td:
    for wallpaper in results.data:
        filename = fwallhaven-{wallpaper.id}{wallpaper.extension}  # from the Wallpapers save function
        wallpaper.save(td)
        webdav.upload(os.path.join(td, filename), filename)  # should upload to webdav cwd ?? cant test it~
