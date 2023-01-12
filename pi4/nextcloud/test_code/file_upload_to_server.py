<<<<<<< HEAD:pi-code/nextcloud/run.py
import nextcloud_client

nc = nextcloud_client.Client('http://drive.finishyourproduct.com/nextcloud')

nc.login('garzarobm', 'Lordking1!')


nc.put_file('testdir/remotefile.txt', 'localfile.txt')

=======
import nextcloud_client
from myconfig import ^
nc = nextcloud_client.Client('http://drive.finishyourproduct.com/nextcloud')

nc.login(username, password)


nc.put_file('testdir/remotefile.txt', 'localfile.txt')

>>>>>>> 98219ccad8d9d853c512981691447863d39cef67:pi4/nextcloud/test_code/file_upload_to_server.py
