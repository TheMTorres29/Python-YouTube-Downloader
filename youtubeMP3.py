# Youtube MP4
import subprocess
from pytube import YouTube

url = "https://www.youtube.com/watch?v=2ZIpFytCSVc"
ytVid = YouTube(url)
fileName = ytVid.title
loopin = True

def convert_mp4_to_mp3():
    mp4 = "%s.mp4" % fileName
    mp3 = "%s.mp3" % fileName
    ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
    subprocess.call(ffmpeg, shell=True)

while loopin == True:
    print("~ YouTube to MP3 Downloader Project ~")
    url = input("Enter url of YouTube video: ")

    userChoice = input("Do you want to download {}? (Y/N)  ".format(YouTube(url).title))
    if userChoice == "0":
        print("Exiting...")
        break
    if userChoice.upper() == "Y":
        choice = input("Do you want to use the video name or rename file yourself? (1. Video Name, 2. Rename):  ")
        if choice == '2':
            fileName = input("FileName: ")
        else:
            print("FileName set to YouTube video name")
            fileName = ytVid.title
        print("Downloading as mp4...")
        ytVid = YouTube(url).streams.first().download(filename=fileName)
        print(ytVid)
        print("Converting to mp3..")
        convert_mp4_to_mp3()
    else:
        userChoice = input("Do you want to download a different video? (Y/N)  ")
        if userChoice == "Y":
            pass
        else:
            loopin = False
print("Thank you. Goodbye!")
