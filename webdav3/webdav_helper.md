webdav.mkdir('some_dir')
webdav.rmdir('another_dir')
webdav.download('remote/path/to/file', 'local/target/file')
webdav.upload('local/path/to/file', 'remote/target/file')



# more commands
cd(path)
ls(path=None)
exists(remote_path)
mkdir(path, safe=False)
mkdirs(path)
rmdir(path, safe=False)
delete(file_path)
upload(local_path_or_fileobj, remote_path)
download(remote_path, local_path_or_fileobj)
