from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy import SpotifyClientCredentials, SpotifyOAuth

CLIENT_SPOTIFY_ID = "###########################"
CLIENT_SPOTIFY_SECRET = "###########################"
REDIRECT_URL = "http://example.com"






url = "https://player.radiozet.pl/Lista-przebojow"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

songs = soup.select("div.title-track")

top_100 = [song.text.strip() for song in songs]

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_SPOTIFY_ID, client_secret=CLIENT_SPOTIFY_SECRET)
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=REDIRECT_URL,
        client_id=CLIENT_SPOTIFY_ID,
        client_secret=CLIENT_SPOTIFY_SECRET,
        cache_path="token.txt"
    )
)

spotify_song_uris = []

for value in top_100:
    spotify_result = sp.search(q=f"track:{value}", type="track")
    try:
        song_uri = spotify_result['tracks']['items'][0]['uri']
        spotify_song_uris.append(song_uri)
    except IndexError:
        print(f"{value} doesn't exist in Spotify. Skipped.")

user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name="ZET-Listopad2023", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=spotify_song_uris)