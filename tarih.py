from gtts import gTTS                      
import os
from playsound import playsound
from tkinter import *
from datetime import datetime

class Tarih():
    def __init__(self):
        self.value = StringVar()

    def konus(self,string):
        tts = gTTS(string, lang='tr',slow=FALSE)
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")

    def tarih(self):
        try:
            an = datetime.now()
            trh = "\n\n\n\n\nBugün {} {} {} \nGünlerden {}".format(an.day, an.strftime('%B'), an.year, an.strftime('%A'))
            self.value.set(trh)
            self.konus(trh)
        except:
            self.value.set('\n\n\n\n\nBir hata oluştu!...')
            self.konus("Bir hata oluştu")