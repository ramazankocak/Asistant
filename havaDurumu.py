from tkinter import *
from playsound import playsound
from lxml import html 
import requests
import os
import time
import speech_recognition as sr
from gtts import gTTS
import emirler



class HavaDurumu():
    def __init__(self):
        self.sehir = StringVar()
        self.value = StringVar()
        self.value1 = StringVar()

    def konus(self,string):
        tts = gTTS(string, lang='tr',slow=FALSE)
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")

    def record(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.3)
            audio = r.listen(source, phrase_time_limit=4)
            data = ""
            try:
                data = r.recognize_google(audio, language='tr-TR')
                self.value1.set('Sen : ' + data.capitalize())
                return data.lower()
            except:
                pass

    def havaDurumu(self):
        city=self.sehir.get().lower()
        try:
            r = requests.get(url="https://www.ntvhava.com/{}-hava-durumu".format(city))
            tree = html.fromstring(r.content)
            derece = tree.xpath("//*[@id='{}']/ul/li[1]/div[2]/div[1]/div[2]/div[1]/text()".format(city))
            durum = tree.xpath("//*[@id='{}']/ul/li[1]/div[2]/div[2]/text()".format(city))
            derece1 = tree.xpath("//*[@id='{}']/ul/li[2]/div[2]/div[1]/div[2]/div[1]/text()".format(city))
            durum1 = tree.xpath("//*[@id='{}']/ul/li[2]/div[2]/div[2]/text()".format(city))
            bugün = "Bugün hava {} derece ve {} gözüküyor.".format(derece[0].lstrip( ),durum[0])
            yarın = "Yarın hava {} derece ve {} gözüküyor.".format(derece1[0].lstrip( ),durum1[0])
            self.value.set(bugün.split())
            self.konus(bugün)
            self.value.set('\n\nYarını da söylememi ister misin?')
            self.konus("Yarını da söylememi ister misin?")
            time.sleep(0.2)
            say=0
            while True:
                say+=1
                asd=self.record()
                if asd in emirler.evet:
                    self.value.set(yarın.split())
                    self.konus(yarın)
                elif asd in emirler.hayır:
                    self.value.set('\n\n\n\n\nPekala...')
                    self.konus("pekala")
                    break
                elif say == 2:
                    say=0
                    break
        except:
            self.value.set("\n\n\n\n\nBir hata oluştu!..")
            self.konus("Bir hata oluştu")