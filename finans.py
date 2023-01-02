from gtts import gTTS
from playsound import playsound
import os
from tkinter import *
import requests
from lxml import html

class Piyasa():
    def __init__(self):
        self.value = StringVar()

    def konus(self,string):
        tts = gTTS(string, lang='tr', slow=FALSE)
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")

    def altin(self):
        r = requests.get("https://www.doviz.com/")
        tree = html.fromstring(r.content)
        altın = tree.xpath('/html/body/header/div[2]/div/div[1]/div[1]/a/span[2]')
        altın=altın[0].text
        altın=altın.split(',',1)
        self.value.set("\n\nAltın: {} TL {} kuruş".format(altın[0],altın[1]))
        self.konus("Altın: {} TL {} kuruş".format(altın[0],altın[1]))
    def dolar(self):
        r = requests.get("https://www.doviz.com/")
        tree = html.fromstring(r.content)
        dolar = tree.xpath('/html/body/header/div[2]/div/div[1]/div[2]/a/span[2]')
        dolar=dolar[0].text
        dolar=dolar.split(',',1)
        self.value.set("\n\nDolar: {} TL {} kuruş".format(dolar[0],dolar[1]))
        self.konus("Dolar: {} TL {} kuruş".format(dolar[0],dolar[1]))
    def euro(self):
        r = requests.get("https://www.doviz.com/")
        tree = html.fromstring(r.content)
        euro = tree.xpath('/html/body/header/div[2]/div/div[1]/div[3]/a/span[2]')
        euro=euro[0].text
        euro=euro.split(',',1)
        self.value.set("\n\nAvro: {} TL {} kuruş".format(euro[0],euro[1]))
        self.konus("Avro: {} TL {} kuruş".format(euro[0],euro[1]))
    def bitcoin(self):
        r = requests.get("https://www.doviz.com/")
        tree = html.fromstring(r.content)
        btc = tree.xpath('/html/body/header/div[2]/div/div[1]/div[6]/a/span[2]')
        btc=btc[0].text
        btc=btc.split(',',1)
        self.value.set("\n\nBitcoin: {} $ {} cent".format(btc[0],btc[1]))
        self.konus("Bitcoin: {} {} cent".format(btc[0],btc[1]))