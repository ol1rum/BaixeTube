from time import sleep
from pytube import YouTube
from pytube import Playlist
from pytube.exceptions import RegexMatchError
from utils import *
import subprocess, os


tipo = 0
user = 0
sair = 0

if __name__ == '__main__':

    # -----------------------------------------------------------------------------------
    # VERIFYING IF FFMPEG IS PROPERLY INSTALLED
    # -----------------------------------------------------------------------------------
    
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE)

    except FileNotFoundError:
        print(
            "\033[31;1m \
            FFmpeg was not installed or was not found.\n \
            If you have the program, enter the path below to add it to the system variable.\
            \033[m"
        )
        print(
            "\033[33;1m\
            Don't include the executable, only the folder where it is located.\
            \033[m"
        )
        print(
            "\033[1m\
            Link to Download for windows 64-bit\033[m: \
            https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/FFmpeg-master-latest-win64-gpl-shared.zip"
        )

        path = input("Path: ")
        
        subprocess.run(['python', os.path.abspath('config_ffmpeg.py'), path])
        print('\033[33mAfter the process, restart the terminal to update the new environment variable\033[m')
        sleep(2)
        exit()

    # -----------------------------------------------------------------------------------
    # STARTING
    # -----------------------------------------------------------------------------------

    print('=-'*10, "Baixe\033[31mTube\033[m", '=-'*10)
    while True:
        try:
            link = str(input("Link Para Baixar: "))
            if "list" in link or "playlist" in link:
                Playlist(link)
            else:
                YouTube(link)
            break
        except RegexMatchError:
            print("\033[31;1mLINK INVÁLIDO\033[m")

    # -----------------------------------------------------------------------------------
    # VERIFYING IF THERE IS A PLAYLIST
    # -----------------------------------------------------------------------------------

    if "playlist" in link:
        tipo = 1
        print("\n\033[1mUsando Playlist\033[m")

    elif "list" in link:
        print(
"""
Playlist detectada, Baixar playlist completa?
1 - Sim
2 - Não
"""
        )
        while tipo not in [1, 2]:
            tipo = int(input("\033[31m>>>\033[m "))

    if tipo == 1:
        yt = Playlist(link)
    else:
        yt = YouTube(link)

    # -----------------------------------------------------------------------------------
    # DOWNLOAD AUDIO OR VIDEO
    # -----------------------------------------------------------------------------------

    print(
"""
1 - Baixar vídeo
2 - Baixar audio
"""
    )
    while user not in [1, 2]:
        user = int(input("\033[31m>>>\033[m "))

    # -----------------------------------------------------------------------------------
    # INICIATE DOWNLOAD
    # -----------------------------------------------------------------------------------

    if tipo == 1:

        if user  == 1:
            print(f"Baixando {len(yt)} vídeos...")  #type: ignore
            for n, v in enumerate(yt.videos):  #type: ignore
                baixar_video(v)
                print(f"{n+1}/{len(yt)}")  #type: ignore

        else:
            print(f"Baixando audio de {len(yt)} vídeos...")  #type: ignore
            for n, a in enumerate(yt.videos):  #type: ignore
                baixar_audio(a)
                print(f"{n+1}/{len(yt)}")  #type: ignore


    elif user == 1:
        baixar_video(yt)

    elif user == 2:
        baixar_audio(yt)


    print("\033[32;1mDONWLOAD CONCLUíDO\033[m")
