import os
from pytube import YouTube
from pydub import AudioSegment

def download_youtube_video(url):
    print("Starting download...")
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=".")
    print(f"Downloaded: {out_file}")
    return out_file

def convert_to_mp3(video_file):
    print("Starting conversion to MP3...")
    base, ext = os.path.splitext(video_file)
    mp3_file = base + '.mp3'
    
    audio = AudioSegment.from_file(video_file)
    audio.export(mp3_file, format="mp3")
    
    print(f"Converted to MP3: {mp3_file}")
    return mp3_file

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube video URL: ")
    video_file = download_youtube_video(youtube_url)
    mp3_file = convert_to_mp3(video_file)
    print(f"MP3 file saved as: {mp3_file}")
