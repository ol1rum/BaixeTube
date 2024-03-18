from time import sleep
from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import RegexMatchError
from utils import *
import subprocess, os


tipo = 0
user = 0


if __name__ == '__main__':

    # -----------------------------------------------------------------------------------
    # VERIFYING IF FFMPEG IS PROPERLY INSTALLED
    # -----------------------------------------------------------------------------------
    
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE)

    except FileNotFoundError:
        print(
            "\033[31;1m"
            "FFmpeg was not installed or was not found.\n"
            "If you have the program, enter the path below to add it to the system variable."
            "\033[m"
        )
        print(
            "\033[33;1m"
            "Don't include the executable, only the folder where it is located."
            "\033[m"
        )
        print(
            "\033[1m"
            "Link to Download for windows 64-bit\033[m:"
            "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/"
            "FFmpeg-master-latest-win64-gpl-shared.zip"
        )

        path = input("Path: ")
        
        subprocess.run(['python', os.path.abspath('config_ffmpeg.py'), path])
        print('\033[33mAfter the process, restart the terminal to update the new environment variable\033[m')
        sleep(2)
        exit()

    # -----------------------------------------------------------------------------------
    # STARTING
    # -----------------------------------------------------------------------------------

    title()
    while True:
        try:
            link = str(input("Link to downlaod: "))
            if "list" in link or "playlist" in link:
                Playlist(link)
            else:
                YouTube(link)
            break
        except RegexMatchError:
            print("\033[31;1mINVALID LINK\033[m")

    # -----------------------------------------------------------------------------------
    # VERIFYING IF THERE IS A PLAYLIST
    # -----------------------------------------------------------------------------------

    if "playlist" in link:
        tipo = 1

    elif "list" in link:
        while tipo not in [1, 2]:
            print('\n'*50)
            title()

            print(
"""
Playlist detected, Downlaod the entire playlist?
1 - Sim
2 - Não
"""
        )
            tipo = only_numeric_input("\033[31m>>>\033[m ")

    if tipo == 1:
        yt = Playlist(link)
    else:
        yt = YouTube(link)

    # -----------------------------------------------------------------------------------
    # DOWNLOAD AUDIO OR VIDEO
    # -----------------------------------------------------------------------------------

    while user not in [1, 2]:
        print('\n'*50)
        title()
        if "playlist" in link:
            print("\033[1mUsing playlist\033[m")  
            
        print(
"""
1 - Downlaod video
2 - download audio
"""
    )
        user = only_numeric_input("\033[31m>>>\033[m ")

    # -----------------------------------------------------------------------------------
    # INICIATE DOWNLOAD
    # -----------------------------------------------------------------------------------

    if tipo == 1:

        if user  == 1:
            print(f"Downloading {len(yt)} videos...")  #type: ignore
            for n, v in enumerate(yt.videos):  #type: ignore
                download_video(v)
                print(f"{n+1}/{len(yt)}")  #type: ignore

        else:
            print(f"Downloading {len(yt)} audios from videos...")  #type: ignore
            for n, a in enumerate(yt.videos):  #type: ignore
                download_audio(a)
                print(f"{n+1}/{len(yt)}")  #type: ignore


    elif user == 1:
        download_video(yt)

    elif user == 2:
        download_audio(yt)


    print("\033[32;1mDONWLOAD COMPLETE\033[m")
