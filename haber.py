#xpath sürekli değişiyor, 'bir hata oluştu' uyarısı aldığında xpath'i kontrol et.
from gtts import gTTS
from playsound import playsound
import os
import html
from lxml import html 
import requests
from tkinter import *
import speech_recognition as sr

class HaberOku():
    def __init__(self):
        self.value = StringVar()
        self.value1 = StringVar()

    def konus(self,string):
        tts = gTTS(string, lang='tr', slow=FALSE)
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

    def haberler(self):
        a=1
        try:
            r = requests.get("https://www.haberler.com/son-dakika/")
            tree = html.fromstring(r.content)
            haber = tree.xpath("/html/body/div[1]/div[3]/div[1]/div/div[{}]/a/span".format(a))
            self.value.set(haber[0].text)
            self.konus(haber[0].text)
            self.value.set("\n\nBaşka haberler için;\n'evet','oku','tabiki' diyebilirsin\n"
                            "Haberleri kapatmak için;\n'hayır','hayır okuma','bu kadar yeter' diyebilirsin")
            self.konus('Başka haber okumamı ister misin')
            say=0
            while True:
                say+=1
                ses=self.record()
                if ses == "evet" or ses == "tabiki" or ses == "oku":
                    a+=1
                    haber = tree.xpath("/html/body/div[1]/div[3]/div[1]/div/div[{}]/a/span".format(a))
                    self.value.set(haber[0].text)
                    self.konus(haber[0].text)
                    self.value.set("\n\nBaşka haberler için 'evet',\n'oku',\n'tabiki' diyebilirsin\n"
                                    "Haberleri kapatmak için 'hayır',\n'hayır okuma',\n'bu kadar yeter' diyebilirsin")
                    self.konus('Başka haber okumamı ister misin')
                    say=0
                elif ses == "hayır" or ses == "hayır okuma" or ses == "bu kadar yeter":
                    self.value.set('\n\nHaberler modundan çıkıldı.')
                    self.konus('Tamam.')
                    say=0
                    break
                elif say == 50:
                    say=0
                    break
        except:
            self.value.set('\n\n\n\n\nBir hata oluştu!...')
            self.konus("Bir hata oluştu")