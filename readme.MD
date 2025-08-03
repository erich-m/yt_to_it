# Youtube to iTunes MP3 Downloader Script

Command Line Script to automatically Download mp3 from YouTube and add mp3 to iTunes using com interface

Command Line: py main.py
Enter track information as requested in the command line
There are a few things to streamline information entry:

- Blank URL or Track Name to exit
- Blank Album Artist to reuse Track Artist
- Reuse the Previous Track Artist with blank entry
- Loops until exit to handle multiple tracks to add

Bugs:
Does not work with URLs from YT playlists

If the yt-dlp stops working, try updating: pip install --upgrade yt-dlp
