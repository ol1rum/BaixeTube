from pydub import AudioSegment
from mutagen.easyid3 import EasyID3
import os
import ctypes


PATH_MUSIC = os.path.join(os.environ["USERPROFILE"], "Music", "Youtube download")
PATH_VIDEO = os.path.join(os.environ["USERPROFILE"], "Videos", "Youtube download")


def baixar_video(video):
    st = video.streams.filter(progressive=True)
    video = st.get_highest_resolution()
    
    video.download(PATH_VIDEO)


def baixar_audio(audio_st):
    audio = audio_st.streams.get_audio_only()

    name = audio.default_filename[:-3]+"mp3"
    audio.download(PATH_MUSIC, filename=name)  #type: ignore
    
    mp3 = AudioSegment.from_file(PATH_MUSIC+'\\'+name, "mp4")
    mp3.export(PATH_MUSIC+name, "mp3")

    tag = EasyID3(PATH_MUSIC+name)
    tag["album"] = audio_st.author
    tag.save()


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
