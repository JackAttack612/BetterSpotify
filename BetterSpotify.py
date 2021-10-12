from playsound import playsound
import os
import time
from os import listdir
from os.path import isfile, join

def main():
    print()
    print(song_list)
    song = input("\nWhat song do you want to play: ")
    playsound(location + r'\songs\\' + song + r'.mp3')
    main()


location = os.path.dirname(__file__)
song_list = os.listdir(location + r'\songs\\')

print("INSTRUCTIONS")
print("The list of files below are the songs that are available")
print("Type the file name without the .mp3 or .wav")
print("If you want to add songs add mp3 or wav files to the songs directory")
print("Note: Do not put any other file types besides .mp3 or .wav in the songs folder")

main()