import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.util as util
import settings
import os
scope = "user-library-read"

print("Getting this")

#sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

print("About to print results")
results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])

