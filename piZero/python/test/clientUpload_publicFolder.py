import nextcloud_client

public_link = 'http://domain.tld/nextcloud/A1B2C3D4'

nc = nextcloud_client.Client.from_public_link(public_link)
nc.drop_file('myfile.zip')