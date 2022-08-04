import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 

client_id = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
client_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids

ids = getTrackIDs('INSERT USERNAME HERE', 'INSERT PLAYLIST ID HERE')

def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # meta data
  name = meta['name']
  album = meta['album']['name']
  artist = meta['album']['artists'][0]['name']
  release_date = meta['album']['release_date']
  length = meta['duration_ms']
  popularity = meta['popularity']

  # audio features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  loudness = features[0]['loudness']
  speechiness = features[0]['speechiness']
  tempo = features[0]['tempo']
  key = features[0]['key']
  length_ms = features[0]['duration_ms']
  loudness = features[0]['loudness']
  valence = features[0]['valence']
  mode = features[0]['mode']
  uri = features[0]['uri']
  time_signature = features[0]['time_signature']

  track = [name, album, artist, release_date, length_ms, popularity, danceability, acousticness, energy, instrumentalness, liveness, loudness, speechiness, tempo, key, valence, mode, uri, time_signature]
  return track

# loop over track ids 
tracks = []
for i in range(len(ids)):
  time.sleep(.5)
  track = getTrackFeatures(ids[i])
  tracks.append(track)

# create dataset
df = pd.DataFrame(tracks, columns = ['name', 'album', 'artist', 'release_date', 'length_ms', 'popularity', 'danceability', 'acousticness', 'energy', 'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo', 'key','valence', 'mode', 'uri', 'time_signature'])
df.to_csv("Spotipy.csv", sep = ',')

