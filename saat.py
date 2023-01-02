from datetime import datetime
#from typing_extensions import Self
from gtts import gTTS                       
from playsound import playsound
import os
from tkinter import *


class Saat():
    def __init__(self):
        self.value = StringVar()

    def konus(self,string):
        tts = gTTS(string, lang='tr',slow=FALSE)
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")

    def saat(self):
        try:
            yazi = datetime.now().strftime('%H:%M:%S')
            self.value.set('\n\n\n\n\n      '+yazi)
            self.konus(yazi)
        except:
            self.value.set('\n\n\n\n\nBir hata oluştu!...')
            self.konus("Bir hata oluştu")