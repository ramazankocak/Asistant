from gtts import gTTS
from playsound import playsound
import os
from tkinter import *
import pyautogui
from datetime import datetime

class Ekler():
    def __init__(self):
        self.value = StringVar()

    def konus(self,string):
        tts = gTTS(string, lang='tr', slow=FALSE)
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")

    def ses_artı(self):
        pyautogui.press('volumeup')
        pyautogui.press('volumeup')
        
    def ses_eksi(self):
        pyautogui.press('volumedown')
        pyautogui.press('volumedown')

    def screens(self):
        an=datetime.now()
        pyautogui.screenshot("SS_{}_{}_{}_{}_{}_{}.jpg".format(an.day,an.month,an.year,an.hour,an.minute,an.second))
        self.value.set('\n\nEkran görüntüsü alındı.')
        self.konus("Ekran görüntüsü alındı")
        self.value.set('\n\nAlınan ekran görüntüsü programın bulunduğu dosyada.')