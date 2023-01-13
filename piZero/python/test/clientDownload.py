import nextcloud_client

public_link = 'http://domain.tld/nextcloud/A1B2C3D4'
folder_password = 'secret'

nc = nextcloud_client.Client.from_public_link(public_link, password=folder_password)
nc.get_file('/sharedfile.zip', 'download/destination/sharedfile.zip')