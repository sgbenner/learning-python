import os

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth
import uuid

guid = str(uuid.uuid4())

# date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD: ")
date = "1975-04-01"

SPOTIFY_USERNAME = os.environ.get("SPOTIFY_USERNAME")

PLAYLIST_NAME = f"Music Flashback {date[0:4]} - {guid[0:6]}"


def get_top_100_songs(date):
    top_100_url = f"https://billboard.com/charts/hot-100/{date}"

    response = requests.get(top_100_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')

    results_list = soup.find_all(class_="o-chart-results-list-row-container")

    top_100 = []

    # print(results_list[0].select("li")[3])

    for result in results_list:
        list_items = result.select("li")
        song_artist_li = list_items[3]
        song_name = str(song_artist_li.find("h3").text).strip()
        artist = str(song_artist_li.find("span").text).strip()

        top_100.append([song_name, artist])

    return top_100


def get_spotify_song(date, artist, track):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    q = f"{artist} {track}"

    result = spotify.search(q=q, limit=1, type="track")

    track_url = result["tracks"]["items"][0]["external_urls"]["spotify"]

    return track_url


def spotify_playlist_auth():
    scope = "playlist-modify-private"

    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))


def create_user_playlist(sp):
    # user_playlist_create(user, name, public=True, description='')
    # Creates a playlist for a user
    #
    # Parameters:
    # user - the id of the user
    # name - the name of the playlist
    # public - is the created playlist public
    # description - the description of the playlist
    results = sp.user_playlist_create(SPOTIFY_USERNAME, PLAYLIST_NAME, public=False,
                                      description="You're personal flashback playlist")
    print(results)
    playlist_id = results["id"]

    return playlist_id


def add_song_to_playlist(sp: spotipy.Spotify, user, playlist_id, tracks):
    # user_playlist_add_tracks(user, playlist_id, tracks, position=None)
    # Adds tracks to a playlist
    #
    # Parameters:
    # user - the id of the user
    # playlist_id - the id of the playlist
    # tracks - a list of track URIs, URLs or IDs
    # position - the position to add the tracks
    results = sp.playlist_add_items(playlist_id, tracks)


########################
# get top songs
########################
print(f"Get top songs for {date}")
top_songs = get_top_100_songs(date)

# lookup each song in spotify's list and return spotify url
print("Lookup each song in spotify and return spotify url")
spotify_songs_url = []

for song in top_songs[0:25]:
    track = song[0]
    artist = song[1]

    spotify_songs_url.append(get_spotify_song(date, artist=artist, track=track))

# authenticate to spotify w/ modify playlist scope
print("Auth to spotify w/ scopes")
sp = spotify_playlist_auth()

# create the playlist
print(f"Create playlist {PLAYLIST_NAME}")
playlist_id = create_user_playlist(sp)

# add songs to the playlist
print(f"Add songs to playlist {playlist_id}")
add_song_to_playlist(sp, SPOTIFY_USERNAME, playlist_id, tracks=spotify_songs_url)
