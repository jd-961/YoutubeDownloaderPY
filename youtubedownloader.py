import time
import os.path
from os import path
from pytube import YouTube
from clint.textui import colored, puts

class YoutubeDownloader:
    def mp4Download(self, url):
        try:
            ytInitialize = YouTube(url)
            ytStreams = ytInitialize.streams.filter(progressive=True)
            downloadPATH = './YoutubeMP4/'

            count = 0
            for countElements in ytStreams:
                count += 1

            if count > 1:            
                ytStreams = ytInitialize.streams[1]
                puts(colored.green(f"Downloading: {ytInitialize.title} (720p)"))
                ytStreams.download(downloadPATH)
                puts(colored.green(f"Done Downloading - {ytInitialize.title} (720p)\n"))

            if count == 1:
                ytStreams = ytInitialize.streams[0]
                puts(colored.green(f"Downloading: {ytInitialize.title} (360p)"))
                ytStreams.download(downloadPATH)
                puts(colored.green(f"Done Downloading - {ytInitialize.title} (360p)\n"))

        except:
            print('Something is wrong with the youtube video.')



    def mp3Download(self, url):

        try:
            downloadPATH = './YoutubeMP3/'
            ytInitialize = YouTube(url)
            puts(colored.green(f'Downloading: {ytInitialize.title} (AUDIO ONLY)'))
            ytStreams = ytInitialize.streams.filter(only_audio=True)[0]
            ytStreams.download(downloadPATH)
            time.sleep(0.5)
            puts(colored.green(f'Done Downlading - {ytInitialize.title} (AUDIO ONLY)\n'))
        except:
            print('Something is wrong with the youtube video.')



if __name__ == "__main__":
    if path.exists('YoutubeMP3'):
        pass
    else:
        os.mkdir('YoutubeMP3')

    if path.exists('YoutubeMP4'):
            pass
    else:
        os.mkdir('YoutubeMP4')

    download = YoutubeDownloader()
    
    while(True):
        puts(colored.magenta("""\
            Download Format: 
                1.MP4
                2.MP3
                3.Exit"""))

        puts(colored.magenta("Enter the number to select format of download."))
        try:
            inp = int(input('> '))


            if inp == 1:
                while(True):
                    keyEnter = 'https://www.youtube.com/watch?v='
                    puts(colored.magenta('Enter the youtube link you would like to download.'))
                    puts(colored.magenta("Enter \"exit\" without \"\" to go back to menu."))
                    inpMP4 = input('> ')
                    if inpMP4.startswith(keyEnter):
                        download.mp4Download(inpMP4)
                    if inpMP4 == 'exit':
                        puts(colored.green('Going back to menu. \n'))
                        break
                    if not inpMP4.startswith(keyEnter):
                        puts(colored.red('Enter a valid youtube url.\n'))

            if inp == 2:
                while(True):
                    puts(colored.magenta('Enter the youtube you would like to download.'))
                    puts(colored.magenta('Enter "exit" without " " to go back to menu.'))
                    inpMP3 = input('> ')
                    if inpMP3.startswith(keyEnter):
                        download.mp3Download(inpMP3)

                    if inpMP3 == "exit":
                        break
                    
                    if not inpMP3.startswith(keyEnter):
                        puts(colored.red('Enter a valid youtube url.\n'))

            if inp == 3:
                break
        except:
            puts(colored.red('Enter integer only'))
