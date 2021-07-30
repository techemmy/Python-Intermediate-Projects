import os
import shutil
from tkinter import filedialog
from gtts import gTTS
from playsound import playsound

def main():
    text = input("Enter text > ")
    language = input("Enter language to speak in > ")
    tld = input("Enter accent > ")

    speech = gTTS(text, lang=language, tld=tld)
    speech.save('sound.mp3')

    action = input('Do you want to save or play (save/play) > ')
    if action == "save":
        save_location = filedialog.askdirectory(
            title='Choose directory to save speech in.')
        shutil.move('sound.mp3', save_location)
    elif action == "play":
        playsound('sound.mp3')
        os.remove('sound.mp3')


if __name__ == '__main__':
    run = ""
    while run == "":
        try:
            main()
        except Exception as e:
            print("ERROR:", e)
            continue
        run = input("Press enter/return to continue:")
    
