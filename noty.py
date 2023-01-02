from gtts import gTTS
from playsound import playsound
from datetime import datetime
import os
from tkinter import *
import subprocess
import pyperclip
import pyautogui
import speech_recognition as sr

class Not():
    def __init__(self):
        self.value = StringVar()

    def konus(self,string):
        tts = gTTS(string, lang='tr', slow=FALSE)
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")

    def record(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=self.duration)
            audio = r.listen(source, phrase_time_limit=self.time_limit)
            data = ""
            try:
                data = r.recognize_google(audio, language='tr-TR')
                self.value1.set('Sen : ' + data.capitalize())
                return data.lower()
            except:
                pass
    
    def notYaz(self):
        self.duration = 0.2
        self.time_limit = 2
        total=0
        an=datetime.now()
        subprocess.Popen("C:\\Windows\\System32\\{}.exe".format("notepad"))
        self.value.set("\n\nNot defteri açıldı.\n\n"
                        "-Yazılacakları en fazla her 4 saniyede söyle.\n\n"
                        "-Kaydetip kapatmak için 'kaydet' demelisin.\n\n"
                        "-Kapatmak veya iptal için:\n'kapat' ya da 'iptal'  demelisin.\n\n"
                        "Uyarı: Kaydedilen notunuzu Masaüstünde\n'not_günün tariri_saat'şeklinde görebilirsiniz.")
        self.konus("Yazılacakları söyle")
        while True:
            ses = self.record()
            old = pyperclip.paste()
            if ses == 'kaydet':
                pyautogui.hotkey('ctrl', 'shift','s')
                pyautogui.typewrite("not_{}_{}_{}_{}_{}_{}".format(an.day,an.month,an.year,an.hour,an.minute,an.second))
                pyautogui.press('enter')
                pyautogui.hotkey('alt','f4')
                self.value.set('\n\nİşlem tamamlandı ve kapatıldı.')
                self.konus("İşlem tamamlandı ve kapatıldı.")
                break
            elif ses == 'iptal' or ses == 'kapat':
                pyautogui.hotkey('alt','f4')
                pyautogui.press('tab')
                pyautogui.press('enter')
                self.value.set('\n\nİşleminiz iptal edildi ve kapatıldı.')
                self.konus("İşlem iptal edildi ve kapatıldı.")
                break
            elif type(ses) == str:
                total+=len(ses)
                pyperclip.copy(ses)
                pyautogui.hotkey('ctrl','v')
                pyautogui.press('space')
                pyperclip.copy(old)
                if total > 85:
                    pyautogui.press('enter')