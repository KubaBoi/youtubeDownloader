from downloader import Downloader

downloader = Downloader()

while True:
    print('Youtube Downloader'.center(40, '_'))
    URL = input('Enter youtube url :  ')
    downloader.download(URL)