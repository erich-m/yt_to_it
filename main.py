import win32com.client
import os
import time

from utils import *
tracks_added = 0
prev_artist = ''
it = win32com.client.Dispatch("iTunes.Application")
# print(dir(it))

playlist = it.LibraryPlaylist
# print(dir(playlist))
while(True):
    print('Enter Track Info:')
    track_url = input("Track URL = ")
    if track_url == '':
        break;

    track_name = input("Track Name = ")
    if track_url == '':
        break;
    track_artist = input(f"Track Artist (Previous = {prev_artist}) = ") or prev_artist
    if track_url == '':
        break;
    prev_artist = track_artist

    track_album_artist = input("Album Artist = ")
    if track_album_artist == '':
        track_album_artist = track_artist

    audio_name,mp3_file_rel = yt_download(track_url)
    mp3_file_full = os.path.abspath(mp3_file_rel)

    print(audio_name)

    it.LibraryPlaylist.AddFile(mp3_file_full)
    time.sleep(1)

    results = playlist.Search(audio_name, 0)
    track = results.Item(1)

    track.Name = track_name
    track.Artist = track_artist
    track.AlbumArtist = track_album_artist

    track.Comment = 'Updated Info' # always add this to every song
    tracks_added += 1

print(f'Successfully added {tracks_added} tracks')