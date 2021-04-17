from youtube_dl import YoutubeDL
from shutil import copyfile, move, rmtree
import os
import os.path
from os import walk

class Downloader:

    def __init__(self):
        self.audio_downloader = YoutubeDL({'format':'bestaudio'})

    def download(self, URL):
        try:
            self.audio_downloader.extract_info(URL)

            if (not os.path.exists("songs")):
                os.mkdir("songs")

            for (dirpath, dirnames, filenames) in walk("."):
                for f in filenames:
                    if (f.split(".")[-1] == "webm"):
                        os.remove(f)
                    if (f.split(".")[-1] == "m4a"):
                        move(f, "songs/" + f)
                break

        except Exception:
            print("Couldn\'t download the audio")