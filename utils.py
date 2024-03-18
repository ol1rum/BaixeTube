from pydub import AudioSegment
from mutagen.easyid3 import EasyID3
import os


PATH_MUSIC = os.path.join(os.environ["USERPROFILE"], "Music", "Youtube download")
PATH_VIDEO = os.path.join(os.environ["USERPROFILE"], "Videos", "Youtube download")

def title() -> None:
    print('=-'*10, "Baixe\033[31mTube\033[m", '=-'*10, "\n")


def download_video(video) -> None:
    st = video.streams.filter(progressive=True)
    video = st.get_highest_resolution()
    
    video.download(PATH_VIDEO)


def download_audio(audio_st) -> None:
    audio = audio_st.streams.get_audio_only()

    name = audio.default_filename[:-3]+"mp3"
    audio.download(PATH_MUSIC, filename=name)  #type: ignore
    
    mp3 = AudioSegment.from_file(PATH_MUSIC+'\\'+name, "mp4")
    mp3.export(PATH_MUSIC+name, "mp3")

    tag = EasyID3(PATH_MUSIC+name)
    tag["album"] = audio_st.author
    tag.save()


def only_numeric_input(text: str) -> int:
    while True:
        t: str = input(text)
        if t.isnumeric():
            return int(t)
        
        print(
            "\033[33;1m"
            "Plese enter only numeric value"
            "\033[m"
        )
        
