from youtube_dl import YoutubeDL
from shutil import copyfile, move, rmtree
import os
import os.path
from os import walk

class Downloader:

    def __init__(self):
        self.audio_downloader = YoutubeDL({'format':'bestaudio'})

    def download(self):
        try:
            print('Youtube Downloader'.center(40, '_'))
            URL = input('Enter youtube url :  ')
            audio_downloader.extract_info(URL)

            if (not os.path.exists("songs")):
                os.mkdir("songs")

            for (dirpath, dirnames, filenames) in walk("."):
                for f in filenames:
                    if (f.split(".")[-1] == "webm"):
                        move(f, "songs/" + f)
                    if (f.split(".")[-1] == "m4a"):
                        os.remove(f)
                break

        except Exception:
            print("Couldn\'t download the audio")