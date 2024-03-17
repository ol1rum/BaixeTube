import ctypes
import sys
import subprocess
import os

# Função para verificar se o script está sendo executado como administrador
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

# Se não estiver rodando como administrador, solicita elevação de privilégios
if not is_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

# Seu código para modificar o PATH aqui
path_ffmpeg = sys.argv[1]
paths = os.environ["Path"]

subprocess.run(["setx", "/m", "PATH", f'{path_ffmpeg};{paths}'])
