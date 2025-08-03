import yt_dlp
import ffmpeg

import os
import re

def yt_download(yt_url:str):
    yt_opts = {
        'extract_audio': True,
        'format': 'bestaudio',
        'outtmpl': 'mp3_files/temp-track.webm',
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    with yt_dlp.YoutubeDL(yt_opts) as audio:
        audio_info = audio.extract_info(yt_url,download=True)
        raw_title = audio_info['title']
        audio_title = re.sub(r'[\\/*?:"<>|]', '-', raw_title)

        input_path = f'mp3_files/temp-track.webm'
        output_path = f'mp3_files/{audio_title}.mp3'

        ffmpeg.input(input_path).output(output_path, acodec='libmp3lame', ab='192k', ar='44100').run(overwrite_output=True)
        os.remove(input_path)

        return (audio_title,output_path) # return mp3 file location
