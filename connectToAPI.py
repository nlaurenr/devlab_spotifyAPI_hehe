import sys
import requests
import base64

def main():

	client_id = ('ef163e2a3dee4c74a91fef81a1f0c453').encode("utf8")
	client_secret = ('b7f930f1b29d4916b88cc0dbbc10ef61').encode("utf8")
	auth_param_id=base64.standard_b64encode(client_id).decode("utf8")
	auth_param_sec=base64.standard_b64encode(client_secret).decode("utf8")
	auth = 'Basic' + auth_param_id + ':' + auth_param_sec

	grant_type = 'client_credentials'

	header_params={'Authorization' : auth}
	body_params = {'grant_type' : grant_type}

	url='https://accounts.spotify.com/api/token'

	response=str(requests.post(url, header_params, body_params))
	sys.stdout.write(response)


main()
