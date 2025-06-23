import spotipy
from spotipy.oauth2 import SpotifyOAuth


client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = 'https://localhost:3000/'
scope = 'user-library-read user-read-playback-state user-modify-playback-state user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# Resto del código igual...

# Mostrar datos del perfil
user_profile = sp.current_user()
print("Perfil del usuario:")
print(user_profile)
print()

# Buscar alguna canción
results = sp.search(q='Rebote El malilla', type='track')
track_uri = results['tracks']['items'][0]['uri']
devices = sp.devices()
device_id = devices['devices'][0]['id']

# Reproducir la canción
sp.start_playback(device_id=device_id, uris=[track_uri], position_ms=0)

# Obtener las 5 canciones más escuchadas
top_tracks = sp.current_user_top_tracks(limit=5, time_range='medium_term')

# Mostrar las canciones
print("\nTus 5 canciones más escuchadas:")
for i, track in enumerate(top_tracks['items'], 1):
    print(f"{i}. {track['name']} by {track['artists'][0]['name']}")
