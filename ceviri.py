from tkinter import *
import os
from gtts import gTTS
from playsound import playsound
import time
from googletrans import Translator

class CeviriYap():
    def __init__(self):
        self.value = StringVar()

    def konus(self,string):
        tts = gTTS(string, lang='tr',slow=FALSE)
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")

    def ceviriYap(self):
        say=0
        self.value.set("\nTercüman modu açıldı.\n\n\n"
                        "-Kelime veya kısa cümleler söyleyin,\n\n"
                        "-Her çeviri den sonra tekrar 'çeviri yap' diyerek yeni çeviri yapabilirsin.\n\n"
                        "-Çeviriyi kapatmak için 'çeviriyi kapat' demelisiniz!...")
        self.konus("Çevirilicek metni söyleyiniz")
        while True:
            say+=1
            metin = self.record()
            if metin == 'çeviriyi kapat' or say == 10:
                    self.value.set('\n\n\n\n\nÇeviri kapatıldı...')
                    self.konus('Çeviri kapatıldı')
                    break
            try:
                trans = Translator()      
                source = trans.detect(metin)
                if source.lang == 'tr':
                    example = trans.translate(metin, src='tr', dest='en')
                    self.value.set('{} :\n{}'.format(source.lang, example.text.capitalize()))
                    self.konus(example.text)
                    say=0
                    time.sleep(1)
                else:
                    example = trans.translate(metin, src=source.lang ,dest='tr')
                    self.value.set('{} :\n{}'.format(source.lang, example.text.capitalize()))
                    self.konus(example.text)
                    say=0
                    time.sleep(1)
            except:
                self.value.set("\nSeni dinliyorum..."
                                "\n\n\nBirşey demedin ya da dediğin çevrilemiyor.")
                if say == 10:
                    self.value.set("\n\n\n\n\nÇeviri kapatıldı...")
                    self.konus('Çeviri kapatıldı')
                    break