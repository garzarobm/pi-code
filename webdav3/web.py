import os
import easywebdav
from wallhaven.api import Wallhaven
import tempfile
# Settings Webdav


webdav = easywebdav.connect('webdav.robjects.me', username='homeconnections', password='7DhL#*/$', protocol='https', port=443,
                            verify_ssl=True)

#webdav.cd(Wallhaven)
#results = wallhaven.search()
#
#with tempfile.TemporaryDirectory() as td:
#    for wallpaper in results.data:
#        filename = fwallhaven-{wallpaper.id}{wallpaper.extension}  # from the Wallpapers save function
#        wallpaper.save(td)
#        webdav.upload(os.path.join(td, filename), filename)  # should upload to webdav cwd ?? cant test it~
