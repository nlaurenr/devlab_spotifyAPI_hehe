import sys
import requests
import base64

def main():

	client_id = 'ef163e2a3dee4c74a91fef81a1f0c453'
	client_secret = 'b7f930f1b29d4916b88cc0dbbc10ef61'
	authorization_param='Basic ' + base64.standard_b64encode(client_id + ':' + client_secret)

	grant_type = 'client_credentials'

	header_params={'Authorization' : authorization_param}
	body_params = {'grant_type' : grant_type}

	url='https://accounts.spotify.com/api/token'

	response=requests.post(url, header_params, body_params) 
	sys.stdout.write(response)


main()
