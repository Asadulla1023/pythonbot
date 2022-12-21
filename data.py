import requests

url = f"https://spotifystefan-skliarovv1.p.rapidapi.com/addTracksToPlaylist"

payload = "userId=%3CREQUIRED%3E&accessToken=%3CREQUIRED%3E&playlistId=%3CREQUIRED%3E&uris=%3CREQUIRED%3E"
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "c7d4567b73msh234fbb260b30a57p1c1cfejsn6ec9d4938903",
	"X-RapidAPI-Host": "Spotifystefan-skliarovV1.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)