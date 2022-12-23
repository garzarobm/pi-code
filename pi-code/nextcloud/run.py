import nextcloud_client

nc = nextcloud_client.Client('http://drive.finishyourproduct.com/nextcloud')

nc.login('garzarobm', 'Lordking1!')


nc.put_file('testdir/remotefile.txt', 'localfile.txt')

