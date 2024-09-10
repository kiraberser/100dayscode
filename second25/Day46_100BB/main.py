import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os 
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
CLIENT_ID = os.environ['CLIENT_ID']
API_SECRET = os.environ['CLIENT_SECRET']

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=API_SECRET,
        redirect_uri="http://example.com",
        scope='playlist-modify-private',
        show_dialog=True,
        cache_path="token.txt",
        username="edwinvega1"
    )
)

user_id = sp.current_user()["id"]
question = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
ENDPOINT = "https://www.billboard.com/charts/hot-100"

response = requests.get(f"{ENDPOINT}/{question}")

bilboard_100 = response.text
soup = BeautifulSoup(bilboard_100, "html.parser")

#soup.select(div ul li h3)
top_music = soup.find_all(name="ul", class_="lrv-a-unstyle-list lrv-u-flex lrv-u-height-100p lrv-u-flex-direction-column@mobile-max")
list_music = [music.find('h3').getText().strip() for music in top_music]

song_uris = []
year = question.split('-')[0]
index = 1
for music in list_music:
    result = sp.search(q=f"track:{music} year:{year}")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{index}.-{music} doesn't exist in Sporify")
        index += 1

#Playlist

playlist = sp.user_playlist_create(user=user_id, name=f"{question} Billboard 100", public=False)
sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist['id'], tracks=song_uris)
