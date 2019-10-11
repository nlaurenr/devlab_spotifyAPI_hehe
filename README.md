# devlab_spotifyAPI_hehe

1) Put client ID:client Secret in Ruby generator (encode.rb) to get the base 64 text 

2) Use that base 64 printed output in the following terminal command (after 'Basic'):
curl -X "POST" -H "Authorization: Basic MzQ1MjExMzAwNDlmNDMGU0ZTEzZGVhY2Y1NGVkMDkxYWIwMDFiNGNkMGU4ZGE=" -d grant_type=client_credentials https://accounts.spotify.com/api/token

Output will look like this:
{"access_token":"BQAeryI9rw5eKXEUlb55xTKtlw0UvNEt4Ov-4U3iVNPvaBm9c6-Fal_CdweU7JvZQ49EbMp1yoTkWPGepQU","token_type":"Bearer","expires_in":3600,"scope":""}

3) Get authorization bearer token from access_token field of above and use it in another GET request (in terminal):
curl -X GET "https://api.spotify.com/v1/playlists/59ZbFPES4DQwEjBpWHzrtC" -H "Authorization: Bearer {your access token}"

(replace part after /playlists/ with the spotify ID from a specific playlist - get that by right clicking playlist on spotify)

4) Redirect stdout to a file (ex. output.json)
