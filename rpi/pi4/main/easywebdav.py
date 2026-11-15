import os
import easywebdav
import tempfile
# Settings Webdav — credentials come from the environment, see README
# (export WEBDAV_HOST, WEBDAV_USER, WEBDAV_PASSWORD)


webdav = easywebdav.connect(os.environ.get('WEBDAV_HOST', 'webdav.example.com'),
                            username=os.environ['WEBDAV_USER'],
                            password=os.environ['WEBDAV_PASSWORD'],
                            protocol='https', port=443,
                            verify_ssl=True)

#webdav.cd(Wallhaven)
#results = wallhaven.search()
#
#with tempfile.TemporaryDirectory() as td:
#    for wallpaper in results.data:
#        filename = fwallhaven-{wallpaper.id}{wallpaper.extension}  # from the Wallpapers save function
#        wallpaper.save(td)
#        webdav.upload(os.path.join(td, filename), filename)  # should upload to webdav cwd ?? cant test it~
