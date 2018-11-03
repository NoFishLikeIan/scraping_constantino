from scraper import get_song_list
import spotipy
import spotipy.util as util
import os
import re

from dotenv import load_dotenv
load_dotenv()


def generate_sp():
    username = os.getenv('USERNAME')
    token = os.getenv('TOKEN')
    playlist_id = os.getenv('PLAYLIST_ID')
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

    return sp, playlist_id, username


def add_tracks_playlist(track_ids, sp, username, playlist_id):

    try:
        sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    except Exception as e:
        print(e)


def get_add_tracks():
    tracks = get_song_list()
    sp, playlist_id, username = generate_sp()
    track_ids = []
    for trk in tracks:
        results = sp.search(q=f'{trk}')
        track_result = results['tracks']['items']
        if len(track_result) > 0:
            for found_track in track_result:
                if 'available_markets' in found_track.keys() and 'IT' in found_track['available_markets']:
                    if found_track['type'] == 'track':
                        track_ids.append(found_track['id'])

    add_tracks_playlist(track_ids, sp, username, playlist_id)


if __name__ == '__main__':
    get_add_tracks()
