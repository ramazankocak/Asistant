from tkinter import *
import emirler
from random import choice
from gtts import gTTS
from playsound import playsound
import os

class Sohbet():
    def __init__(self):
        self.value = StringVar()

    def konus(self,string):
        tts = gTTS(string, lang='tr',slow=FALSE)
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")
    
    def sohbet(self):
        try:
            secim = choice(emirler.sohbet)
            self.value.set(secim)
            self.konus(secim)
        except:
            self.value.set('\n\n\n\n\nBir hata oluştu!...')
            self.konus("Bir hata oluştu")