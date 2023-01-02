# -*- coding:utf-8 -*-
import pyperclip
import speech_recognition as sr
from tkinter import *
from tkinter.ttk import Notebook
from gtts import gTTS
from playsound import playsound
import os
import sys
import webbrowser
import locale
import pyautogui
import time
from random import choice
import threading
import emirler
import help
import komutlar
from win32api import GetSystemMetrics
from SanalMouse import *
import cv2
import saat
import tarih
import havaDurumu
import sohbet
import ceviri
import haber
import finans
import eklentiler
import noty

pyautogui.FAILSAFE = False
locale.setlocale(locale.LC_ALL, 'tr_TR')

class Asistan(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master=master
        menu=Menu(self.master)
        self.master.configure(menu=menu)
        fileMenu=Menu(menu, tearoff=0)
        fileMenu.add_command(label="Ayarlar", command=self.ayarlar)
        fileMenu.add_command(label="Yardım", command=self.yardim)
        fileMenu.add_command(label="Müzik", command=self.music)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.kapat)
        menu.add_cascade(label="MENU", menu=fileMenu)
        nameMenu=Menu(menu, tearoff=0)
        nameMenu.add_command(label='Profilin' ,command = self.profil)
        menu.add_cascade(label='PROFİL', menu=nameMenu)
        kmtlrlMenu=Menu(menu, tearoff=0)
        kmtlrlMenu.add_command(label='Mouse', command=self.mouse_komutlar)
        kmtlrlMenu.add_command(label='Klavye', command=self.klavye_komutlar)
        menu.add_cascade(label='KOMUTLAR', menu=kmtlrlMenu)

        self.dizin = os.getcwd()
        self.key0=0
        self.key1=0
        self.key2=0
        self.key3=0
        self.key4=0
        self.key5=0
        self.sekme=0
        self.duration=0.3
        self.time_limit=4
        self.mouse_on = 0

        self.yatay=GetSystemMetrics(0)
        self.dikey=GetSystemMetrics(1)

        self.checkvar1=IntVar()

        self.img1 = PhotoImage(file="{}/mic.png".format(self.dizin))
        self.buton=Button(command=self.asist, image=self.img1)
        self.buton.place(relx=0.45, rely=0.909)
        self.buton1=Button(text='AYARLAR',bd=2, command=self.ayarlar)
        self.buton1.place(relx=0.09, rely=0.909, height=46, width=100)
        self.buton2=Button(text='YARDIM',bd=2, command=self.yardim)
        self.buton2.place(relx=0.66, rely=0.909, height=46, width=100)
        self.cnvs=Canvas(bg='#E0E0E0', width=370, height=30).place(x=0, y=0)
        self.value1 = StringVar()
        self.lbl1=Label(textvariable=self.value1, bg='#E0E0E0', fg='#404040', font=('Calibri',11,'bold')).place(x=0, y=5)
        self.cnvs1=Canvas(bg='#E0E0E0', width=350, height=395).place(x=0, y=50)
        self.value=StringVar()
        self.msg = Message(textvariable=self.value, bg='#E0E0E0', fg='#000000')
        self.msg.configure(font=('Arial',11))
        self.msg.configure(width=350)
        self.msg.place(x=0, y=50)

        self.scroll_up = IntVar(value=500)
        self.scroll_down = IntVar(value=500)
        self.trns = IntVar(value=10)
        self.name = StringVar()
        self.sehir = StringVar()
        self.namefile=open('{}/names.txt'.format(self.dizin),'a+',encoding="utf-8")
        self.namefile.close()
        self.namefile=open('{}/names.txt'.format(self.dizin),encoding="utf-8")
        self.list_name=list(self.namefile.readlines())
        if len(self.list_name) != 0:
            self.name.set(self.list_name[0].lower())
        else:
            self.name.set("bilgisayar")
        self.sehirfile=open('{}/sehir.txt'.format(self.dizin),'a+',encoding="utf-8")
        self.sehirfile.close()
        self.sehirfile=open('{}/sehir.txt'.format(self.dizin),encoding="utf-8")
        self.list_sehir=list(self.sehirfile.readlines())
        if len(self.list_sehir) != 0:
            self.sehir.set(self.list_sehir[0])
        else:
            self.sehir.set("Karabük")

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

    def profil(self):
        win_profil = Toplevel()
        win_profil.geometry('400x300')
        win_profil.title('Profil')
        win_profil.iconbitmap("{}/icon.ico".format(self.dizin))
        win_profil.resizable(0, 0)
        win_profil.configure(bg='#CCE5FF')
        lbl=Label(win_profil, text="ASİSTAN PROFİLİNİZ", font=('Calibri',12,'bold'), bg='#CCE5FF', relief=GROOVE).pack(fill=X)
        lbl1=Label(win_profil, text='PC adı :', bg='#CCE5FF').place(x=5, y=50)
        self.en=Entry(win_profil, textvariable=self.name, width=35).place(x=70, y=50)
        lbl2=Label(win_profil, text='Şehir   :', bg='#CCE5FF').place(x=5, y=90)
        self.en1=Entry(win_profil, textvariable=self.sehir, width=35).place(x=70, y=90)
        def degis():
            isim=self.name.get().lower()
            self.name.set(isim)
            self.namefile=open('{}/names.txt'.format(self.dizin),'w',encoding="utf-8")
            self.namefile.write(isim)
            self.namefile.close()
        def city():
            shr=self.sehir.get()
            self.sehir.set(shr)
            self.sehirfile=open('{}/sehir.txt'.format(self.dizin),'w',encoding="utf-8")
            self.sehirfile.write(shr)
            self.sehirfile.close()
        self.btn=Button(win_profil, text='UYGULA', command=lambda:[degis(), city()], bg='#CCE5FF', width=8).place(x=180, y=200)
    
    def mouse_komutlar(self):
        win_mouse=Toplevel()
        win_mouse.geometry('350x500')
        win_mouse.title('Mouse Komutları')
        win_mouse.resizable(0, 1)
        win_mouse.iconbitmap("{}/icon.ico".format(self.dizin))
        lbl=Label(win_mouse, text='Mouse Komutları', bg='#CCE5FF').pack(fill=X)
        txt=Text(win_mouse, font=('Calibri',12,'bold'), bg='#CCE5FF')
        txt.insert(END, komutlar.mouse_kntrl[0])
        txt.pack(fill=BOTH, expand=True)
        txt.config(state=DISABLED)

    def klavye_komutlar(self):
        win_klavye=Toplevel()
        win_klavye.geometry('350x500')
        win_klavye.title('Klavye Komutları')
        win_klavye.resizable(0, 1)
        win_klavye.iconbitmap("{}/icon.ico".format(self.dizin))
        lbl=Label(win_klavye, text='Klavye Komutları', bg='#CCE5FF').pack(fill=X)
        txt=Text(win_klavye, font=('Calibri',12,'bold'), bg='#CCE5FF')
        txt.insert(END, komutlar.klavye_kntrl[0])
        txt.pack(fill=BOTH, expand=True)
        txt.config(state=DISABLED)

#youtube ve google modülü oluşturuldu fakat eklenmedi.
    def youtube(self):
        self.key1=1
        self.sekme+=1
        url = "https://www.youtube.com"
        webbrowser.get().open(url)
        a=("\n\nYoutube modundasın.\n"
            "Gezinmek için;\n"
            "Kontrol modu otomatik açıldı.\n\n"
            "Ekstra komutları öğrenmek için 'YARDIM' a tıkla.")
        self.value.set(a)
        self.konus("Youtube açıldı.")
        self.kontrol()
        self.key1=0
        self.value.set('\n\nYoutube modu kapatıldı.')
    
    def googledan(self):
        self.sekme+=1
        webbrowser.get().open("https://google.com")
        self.value.set('\n\nAramak istediğini söyle!...')
        self.konus("Ne aramak istiyorsun?")
        self.yazici()
        self.kontrol()
        self.value.set('\n\nGoogle modu kapatıldı.')

    def mUSİc(self):
        self.key3=1
        say=0
        cnt_msc=0
        self.value.set(emirler.mzk_mtn)
        self.konus(' Müzik modu açıldı.')
        file=open('{}/Muzik_Listesi.txt'.format(self.dizin),'a',encoding="utf-8")
        file.close()
        file=open('{}/Muzik_Listesi.txt'.format(self.dizin),encoding="utf-8")
        list_data=list(file.readlines())
        kanallar=[]
        linkler=[]
        for i in list_data:
            asd=i.split(':',1)
            kanallar.append(asd[0].strip(' ').lower())
            linkler.append(asd[1].strip(' ').replace('\n',''))
        if len(kanallar) != 0:
            soz=['Hangi müziği açayım?','Ne dinlemek istersin?','Dinlemek istediğin müziği söyle ya da istersen karışık açayım']
            secim=choice(soz)
            self.konus(secim)
        while True:
            say+=1
            if len(kanallar) == 0:
                self.value.set("\n\n'Menu' e tıkla\n'Müzik' i aç ve listene müzikler ekle.")
                self.konus('Müzik listeniz boş. Müzik eklemelisiniz.')
                time.sleep(5)
                self.value.set('Müzik modu kapatıldı.')
                break
            ses = self.record()
            if ses in emirler.müzikler:
                if len(kanallar) > 10:
                    self.konus("Müzik listesinde {} adet müzik var.".format(len(kanallar)))
                    self.konus('Bunları saymam uzun sürebilir.')
                else:
                    for i in kanallar:
                        self.konus(i)
                say=0
            elif ses in kanallar:
                if cnt_msc == 0:
                    indeks=kanallar.index(ses)
                    url=linkler[indeks]
                    webbrowser.get().open(url)
                    cnt_msc=1
                elif cnt_msc == 1:
                    pyautogui.hotkey('ctrl','w')
                    indeks=kanallar.index(ses)
                    url=linkler[indeks]
                    webbrowser.get().open(url)
                say=0
            elif ses in emirler.mix:
                cnt_msc=1
                pyautogui.hotkey('ctrl','w')
                url=choice(linkler)
                webbrowser.get().open(url)
                say=0
            elif ses in emirler.change:
                cnt_msc=1
                pyautogui.hotkey('ctrl','w')
                url=choice(linkler)
                webbrowser.get().open(url)
                say=0
            elif ses == 'sesi kapat' or ses == 'sesi aç':
                pyautogui.press('volumemute')
                say=0
            elif ses == 'sesi azalt':
                pyautogui.press('volumedown')
                pyautogui.press('volumedown')
                say=0
            elif ses == 'sesi yükselt':
                pyautogui.press('volumeup')
                pyautogui.press('volumeup')
                say=0
            elif ses in emirler.muSic_off:
                pyautogui.hotkey('ctrl','w')
                self.value.set('Müzik modu kapatıldı.')
                self.konus('Müzik modu kapatıldı')
                break
            elif ses == self.name.get():
                self.konus('Seni dinliyorum')
                say=0
            elif ses in emirler.pause:
                self.value.set('Bekleme modu aktif.')
                self.konus('Bekleme modu açıldı')
                self.beklemeModu()
                self.konus('Bekleme modu kapatıldı.')
                self.value.set(emirler.mzk_mtn)
                say=0
            elif ses == 'programı kapat':
                pyautogui.hotkey('ctrl','w')
                self.kapat()
            elif say == 1500:
                pyautogui.press('k')
                self.value.set('Müzik durduruldu.')
                self.konus('Müzik dinlemeye devam ediyor musun?')
                cnt=0
                while True:
                    cnt+=1
                    ses = self.record()
                    if ses == 'evet':
                        pyautogui.press('k')
                        break
                    elif ses == 'hayır':
                        pyautogui.hotkey('ctrl','w')
                        self.value.set('Müzik modu kapatıldı.')
                        self.konus('Müzik kapatıldı.')
                        break
                    elif type(ses) != str or cnt ==15:
                        pyautogui.hotkey('ctrl','w')
                        self.value.set('Müzik modu kapatıldı.')
                        self.konus('Müzik kapatıldı.')
                        break

    def music(self):
        win_mUSİc=Toplevel()
        win_mUSİc.title('Müzik Kutusu')
        win_mUSİc.geometry('400x530')
        win_mUSİc.iconbitmap('{}/icon.ico'.format(self.dizin))
        win_mUSİc['bg']='#606060'
        win_mUSİc.resizable(0,0)
        win_mUSİc.lbl0=Label(win_mUSİc, text="Eklemek İstediğiniz Müzikleri Giriniz",font=('Calibri',10,'bold'), bg='#606060', relief=GROOVE).pack(padx=0, pady=0, fill=X)
        win_mUSİc.lbl1=Label(win_mUSİc, text='Müzik Adı   :',font=('Calibri',10,'bold'), bg='#606060').place(relx=0.0225,rely=0.056)
        win_mUSİc.ent1=StringVar()
        win_mUSİc.entry1=Entry(win_mUSİc, textvariable=win_mUSİc.ent1, bd=2, width=35, bg='#E0E0E0').place(relx=0.25, rely=0.056)
        win_mUSİc.lbl2=Label(win_mUSİc, text='Müzik Linki :',font=('Calibri',10,'bold'), bg='#606060').place(relx=0.0225,rely=0.113)
        win_mUSİc.ent2=StringVar()
        win_mUSİc.entry2=Entry(win_mUSİc, textvariable=win_mUSİc.ent2, bd=2, width=35, bg='#E0E0E0').place(relx=0.25,rely=0.113)
        win_mUSİc.lstbox=Listbox(win_mUSİc, relief= RIDGE, bd=2, bg='#E0E0E0')
        file=open('{}/Muzik_Listesi.txt'.format(self.dizin),'a',encoding="utf-8")
        file.close()
        file=open('{}/Muzik_Listesi.txt'.format(self.dizin),encoding="utf-8")
        list_data=list(file.readlines())
        if len(list_data) != 0:
            for i in list_data:
                m=i.split(':',1)
                win_mUSİc.lstbox.insert(END,m[0])
        def kaydet():
            global list_data
            global file
            win_mUSİc.ent1.set(win_mUSİc.ent1.get())
            win_mUSİc.ent2.set(win_mUSİc.ent2.get())
            if win_mUSİc.ent1.get() !="" and win_mUSİc.ent2.get() !="":
                win_mUSİc.lstbox.insert(END, "{}\n".format(win_mUSİc.ent1.get()))
                file=open('{}/Muzik_Listesi.txt'.format(self.dizin),'a+',encoding="utf-8")
                file.write("{} : {}\n".format(win_mUSİc.ent1.get(),win_mUSİc.ent2.get()))
                file.close()
                file=open('{}/Muzik_Listesi.txt'.format(self.dizin))
                list_data=list(file.readlines())
        win_mUSİc.btn1=Button(win_mUSİc,text='KAYDET', bg='#CCE5FF', command=kaydet, width=8).place(relx=0.79, rely=0.17)
        win_mUSİc.lbl3=Label(win_mUSİc,text='Müzik Listesi:',font=('Calibri',10,'bold'), bg='#606060').place(relx=0.0225, rely=0.226)
        def sil():
            global list_data
            global file
            select=win_mUSİc.lstbox.get(win_mUSİc.lstbox.curselection())
            win_mUSİc.lstbox.delete(win_mUSİc.lstbox.curselection())
            file=open('{}/Muzik_Listesi.txt'.format(self.dizin),encoding="utf-8")
            list_data=list(file.readlines())
            for indx in list_data:
                m=indx.split(':',1)
                if m[0] == select:
                    break
            list_data.pop(list_data.index(indx))
            file=open('{}/Muzik_Listesi.txt'.format(self.dizin),'w+',encoding="utf-8")
            for i in list_data:
                file.write(i)
            file.close()                
        win_mUSİc.lstbox.pack(padx=9, pady=120, expand=True, fill=BOTH)
        win_mUSİc.btn2=Button(win_mUSİc,text='SİL', bg='#CCE5FF', command=sil, width=8).place(relx=0.5875, rely=0.85)
        win_mUSİc.btn3=Button(win_mUSİc,text='TAMAM', bg='#CCE5FF', command=win_mUSİc.destroy, width=8).place(relx=0.79, rely=0.85)

    def mouseStart(self):
        self.mouse_on = 1
        handmajor = HandRecog(HLabel.MAJOR)
        handminor = HandRecog(HLabel.MINOR)
        if self.checkvar1.get() == 1:
            cap = cv2.VideoCapture(0)
        elif self.checkvar1.get() == 2:
            cap = cv2.VideoCapture(1)
        else:
            cap = cv2.VideoCapture(0)
        with mp_hands.Hands(max_num_hands = 2,min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
            while cap.isOpened() and self.mouse_on ==1:
                success, image = cap.read()
                if not success:
                    self.value.set('\n\n\n\n\nKameran yok galiba!...')
                    continue
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                image.flags.writeable = False
                results = hands.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                if results.multi_hand_landmarks:                   
                    GestureController.classify_hands(results)
                    handmajor.update_hand_result(GestureController.hr_major)
                    handminor.update_hand_result(GestureController.hr_minor)
                    handmajor.set_finger_state()
                    handminor.set_finger_state()
                    gest_name = handminor.get_gesture()
                    if gest_name == Gest.PINCH_MINOR:
                        Controller.handle_controls(gest_name, handminor.hand_result)
                    else:
                        gest_name = handmajor.get_gesture()
                        Controller.handle_controls(gest_name, handmajor.hand_result)
                    for hand_landmarks in results.multi_hand_landmarks:
                        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                else:
                    Controller.prev_hand = None
                cv2.imshow('Mouse Kontrol', image)
                if cv2.waitKey(5) == 27:
                    break
            cap.release()
            cv2.destroyAllWindows()
    def mouseOff(self):
        self.mouse_on = 0

    def screen_maps(self):
        w=GetSystemMetrics(0)
        h=GetSystemMetrics(1)
        en=int(w/4)
        boy=int(h/4)
        self.win_maps=Toplevel()
        self.win_maps.geometry('%dx%d+0+0'%(w,h))
        self.win_maps.wm_attributes('-alpha', 0.3)
        self.win_maps.overrideredirect(True)
        cnvas=Canvas(self.win_maps, bg="#CCE5FF" , height=boy , width=en).place(x=0,y=0)
        cnvas1=Canvas(self.win_maps, bg="#FFCCFF" , height=boy , width=en).place(x=w/4,y=0)
        cnvas2=Canvas(self.win_maps, bg="#CCE5FF" , height=boy , width=en).place(x=w/2,y=0)
        cnvas3=Canvas(self.win_maps, bg="#FFCCFF" , height=boy , width=en).place(x=(w/4)*3,y=0)
        cnvas4=Canvas(self.win_maps, bg="#FFCCFF" , height=boy , width=en).place(x=0,y=h/4)
        cnvas5=Canvas(self.win_maps, bg="#CCE5FF" , height=boy , width=en).place(x=w/4,y=h/4)
        cnvas6=Canvas(self.win_maps, bg="#FFCCFF" , height=boy , width=en).place(x=w/2,y=h/4)
        cnvas7=Canvas(self.win_maps, bg="#CCE5FF" , height=boy , width=en).place(x=(w/4)*3,y=h/4)
        cnvas8=Canvas(self.win_maps, bg="#CCE5FF" , height=boy , width=en).place(x=0,y=h/2)
        cnvas9=Canvas(self.win_maps, bg="#FFCCFF" , height=boy , width=en).place(x=w/4,y=h/2)
        cnvas10=Canvas(self.win_maps, bg="#CCE5FF" , height=boy , width=en).place(x=w/2,y=h/2)
        cnvas11=Canvas(self.win_maps, bg="#FFCCFF" , height=boy , width=en).place(x=(w/4)*3,y=h/2)
        cnvas12=Canvas(self.win_maps, bg="#FFCCFF" , height=boy , width=en).place(x=0,y=(h/4)*3)
        cnvas13=Canvas(self.win_maps, bg="#CCE5FF" , height=boy , width=en).place(x=w/4,y=(h/4)*3)
        cnvas14=Canvas(self.win_maps, bg="#FFCCFF" , height=boy , width=en).place(x=w/2,y=(h/4)*3)
        cnvas15=Canvas(self.win_maps, bg="#CCE5FF" , height=boy , width=en).place(x=(w/4)*3,y=(h/4)*3)
        lbl=Label(self.win_maps, text='1', font=('Calibri',20,'bold'), bg="#CCE5FF").place(x=w/8, y=h/8)
        lbl1=Label(self.win_maps, text='2',font=('Calibri',20,'bold'), bg="#FFCCFF").place(x=(w/8)*3, y=h/8)
        lbl2=Label(self.win_maps, text='3',font=('Calibri',20,'bold'), bg="#CCE5FF").place(x=(w/8)*5, y=h/8)
        lbl3=Label(self.win_maps, text='4',font=('Calibri',20,'bold'), bg="#FFCCFF").place(x=(w/8)*7, y=h/8)
        lbl4=Label(self.win_maps, text='5',font=('Calibri',20,'bold'), bg="#FFCCFF").place(x=w/8, y=(h/8)*3)
        lbl5=Label(self.win_maps, text='6',font=('Calibri',20,'bold'), bg="#CCE5FF").place(x=(w/8)*3, y=(h/8)*3)
        lbl6=Label(self.win_maps, text='7',font=('Calibri',20,'bold'), bg="#FFCCFF").place(x=(w/8)*5, y=(h/8)*3)
        lbl7=Label(self.win_maps, text='8',font=('Calibri',20,'bold'), bg="#CCE5FF").place(x=(w/8)*7, y=(h/8)*3)
        lbl8=Label(self.win_maps, text='9',font=('Calibri',20,'bold'), bg="#CCE5FF").place(x=w/8, y=(h/8)*5)
        lbl9=Label(self.win_maps, text='10',font=('Calibri',20,'bold'), bg="#FFCCFF").place(x=(w/8)*3, y=(h/8)*5)
        lbl10=Label(self.win_maps, text='11',font=('Calibri',20,'bold'), bg="#CCE5FF").place(x=(w/8)*5, y=(h/8)*5)
        lbl11=Label(self.win_maps, text='12',font=('Calibri',20,'bold'), bg="#FFCCFF").place(x=(w/8)*7, y=(h/8)*5)
        lbl12=Label(self.win_maps, text='13',font=('Calibri',20,'bold'), bg="#FFCCFF").place(x=w/8, y=(h/8)*7)
        lbl13=Label(self.win_maps, text='14',font=('Calibri',20,'bold'), bg="#CCE5FF").place(x=(w/8)*3, y=(h/8)*7)
        lbl14=Label(self.win_maps, text='15',font=('Calibri',20,'bold'), bg="#FFCCFF").place(x=(w/8)*5, y=(h/8)*7)
        lbl15=Label(self.win_maps, text='16',font=('Calibri',20,'bold'), bg="#CCE5FF").place(x=(w/8)*7, y=(h/8)*7)
        while True:
            ses=self.record()
            if ses == '1' or ses == 'bir':
                self.yatay/=8
                self.dikey/=8
                pyautogui.moveTo(w/8,h/8, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '2' or ses == 'iki':
                self.yatay=(self.yatay/8)*3
                self.dikey/=8
                pyautogui.moveTo((w/8*3),h/8, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '3' or ses == 'üç':
                self.yatay=(self.yatay/8)*5
                self.dikey/=8
                pyautogui.moveTo((w/8)*5,h/8, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '4' or ses == 'dört':
                self.yatay=(self.yatay/8)*7
                self.dikey/=8
                pyautogui.moveTo((w/8)*7,h/8, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '5' or ses == 'beş':
                self.yatay/=8
                self.dikey=(self.dikey/8)*3
                pyautogui.moveTo(w/8,(h/8)*3, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '6' or ses == 'altı':
                self.yatay=(self.yatay/8)*3
                self.dikey=(self.dikey/8)*3
                pyautogui.moveTo((w/8)*3,(h/8)*3, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '7' or ses == 'yedi':
                self.yatay=(self.yatay/8)*5
                self.dikey=(self.dikey/8)*3
                pyautogui.moveTo((w/8)*5,(h/8)*3, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '8' or ses == 'sekiz':
                self.yatay=(self.yatay/8)*7
                self.dikey=(self.dikey/8)*3
                pyautogui.moveTo((w/8)*7,(h/8)*3, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '9' or ses == 'dokuz':
                self.yatay/=8
                self.dikey=(self.dikey/8)*5
                pyautogui.moveTo(w/8,(h/8)*5, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '10' or ses == 'on':
                self.yatay=(self.yatay/8)*3
                self.dikey=(self.dikey/8)*5
                pyautogui.moveTo((w/8)*3,(h/8)*5, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '11' or ses == 'on bir':
                self.yatay=(self.yatay/8)*5
                self.dikey=(self.dikey/8)*5
                pyautogui.moveTo((w/8)*5,(h/8)*5, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '12' or ses == 'on iki':
                self.yatay=(self.yatay/8)*7
                self.dikey=(self.dikey/8)*5
                pyautogui.moveTo((w/8)*7,(h/8)*5, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '13' or ses == 'on üç':
                self.yatay/=8
                self.dikey=(self.dikey/8)*7
                pyautogui.moveTo(w/8,(h/8)*7, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '14' or ses == 'on dört':
                self.yatay=(self.yatay/8)*3
                self.dikey=(self.dikey/8)*7
                pyautogui.moveTo((w/8)*3,(h/8)*7, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '15' or ses == 'on beş':
                self.yatay=(self.yatay/8)*5
                self.dikey=(self.dikey/8)*7
                pyautogui.moveTo((w/8)*5,(h/8)*7, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break
            elif ses == '16' or ses == 'on altı':
                self.yatay=(self.yatay/8)*7
                self.dikey=(self.dikey/8)*7
                pyautogui.moveTo((w/8)*7,(h/8)*7, 1, pyautogui.easeOutQuad)
                self.win_maps.destroy()
                break

    def kontrol(self):
        self.key2=1
        self.value.set('Kontrol açıldı.')
        self.konus('Kontrol açıldı')
        self.yatay = GetSystemMetrics(0)/2
        self.dikey = GetSystemMetrics(1)/2
        w = self.yatay/2
        h = self.dikey/2
        pyautogui.moveTo(self.yatay,self.dikey,duration=0.5)
        self.value.set("Kontrol modundasın.\n"
                        "{}".format(emirler.kntrl_metin))
        say=0
        while True:
            say+=1
            ses = self.record()
            if ses == 'mouse aç':
                window.wm_attributes('-alpha', 0)
                self.mouse_off = Toplevel()
                self.mouse_off.title('Mouse Kapat')
                self.mouse_off.attributes('-topmost',1)
                self.mouse_off.wm_attributes('-alpha', 7)
                self.mouse_off.overrideredirect(True)
                self.mouse_off.btn=Button(self.mouse_off, text='MOUSE KAPAT', command=self.mouseOff, bd=3).pack(fill=BOTH, expand=True, anchor=CENTER)
                self.mouse_off.geometry('150x100+%d+%d'%(GetSystemMetrics(0)/2,0))
                self.mouseStart()
                self.mouse_off.destroy()
                self.konus('Sanal mouse kapatıldı.')
                if self.key4 == 1:
                    self.reaction()
                    window.wm_attributes('-alpha', 0)
                elif self.key4 == 0:
                    window.wm_attributes('-alpha', self.trns.get()/10)
                say=0
            if ses == 'ekranı göster':
                self.yatay=GetSystemMetrics(0)
                self.dikey=GetSystemMetrics(1)
                w = self.yatay/16
                h = self.dikey/16
                window.attributes('-topmost',0)
                window.wm_attributes('-alpha', 0)
                self.screen_maps()
                if self.key4 == 1:
                    window.attributes('-topmost',1)
                    window.wm_attributes('-alpha', 0)
                elif self.key4 == 0:
                    window.attributes('-topmost',1)
                    window.wm_attributes('-alpha', self.trns.get())
                say=0
            if ses in emirler.sag:
                self.yatay+=w
                pyautogui.moveTo(self.yatay,self.dikey,duration=0.5)
                w/=2
                say=0
            elif ses in emirler.sol:
                self.yatay-=w
                pyautogui.moveTo(self.yatay,self.dikey,duration=0.5)
                w/=2
                say=0
            elif ses in emirler.yukarı:
                self.dikey-=h
                pyautogui.moveTo(self.yatay,self.dikey,duration=0.5)
                h/=2
                say=0
            elif ses in emirler.asagi:
                self.dikey+=h
                pyautogui.moveTo(self.yatay,self.dikey,duration=0.5)
                h/=2
                say=0
            elif ses in emirler.orta:
                self.yatay = GetSystemMetrics(0)/2
                self.dikey = GetSystemMetrics(1)/2
                pyautogui.moveTo(self.yatay,self.dikey,duration=0.5)
                w = self.yatay/2
                h = self.dikey/2
                say=0
            elif ses in emirler.scrll_down:
                asd=int(self.scroll_down.get())*(-1)
                pyautogui.scroll(asd)
                say=0
            elif ses in emirler.scrll_up:
                pyautogui.scroll(int(self.scroll_up.get()))
                say=0
            elif ses in emirler.back:
                pyautogui.hotkey('alt','left')
                say=0
            elif ses in emirler.next:
                pyautogui.hotkey('alt','right')
                say=0
            elif ses in emirler.sesArti:
                pyautogui.hotkey('volumeup')
                pyautogui.hotkey('volumeup')
                say=0
            elif ses in emirler.sesEksi:
                pyautogui.hotkey('volumedown')
                pyautogui.hotkey('volumedown')
                say=0
            elif ses in emirler.ses_ac_kapat:
                pyautogui.press('volumemute')
                say=0
            elif ses in emirler.ileriSar:
                pyautogui.press('right')
                say=0
            elif ses in emirler.geriSar:
                pyautogui.press('left')
                say=0
            elif ses == "sekme aç" or ses == "yeni sekme aç":
                self.sekme+=1
                pyautogui.hotkey('ctrl','t')
                say=0
            elif ses == "sekmeyi kapat" or ses == "sekme kapat":
                self.sekme-=1
                pyautogui.hotkey('ctrl','w')
                say=0
            elif ses == "sekmeyi değiştir" or ses == "sekme değiştir":
                pyautogui.hotkey('ctrl','tab') 
                say=0            
            elif ses == "dediğimi yaz" or ses == "yaz":
                if self.key4 == 1:
                    self.reaction()
                    self.yazici()
                    window.wm_attributes('-alpha', 0)
                    self.value.set("Kontrol modundasın.\n"
                            "{}".format(emirler.kntrl_metin))
                elif self.key4 == 0:
                    self.reaction()
                    self.yazici()
                    window.wm_attributes('-alpha', self.trns.get()/10)
                    self.value.set("Kontrol modundasın.\n"
                            "{}".format(emirler.kntrl_metin))
                say=0
            elif ses == "enter":
                pyautogui.press('enter')
                say=0
            elif ses == "sil":
                pyautogui.press('backspace')
                say=0
            elif ses in emirler.bekle:
                self.value.set("'Kontrol modunda beklemedesin.'\n"
                                "Kontrolü tekrar açmak için \n{}\ndemelisin.".format(self.name.get()))
                pyautogui.moveTo(GetSystemMetrics(0)/2, GetSystemMetrics(1), duration=1)
                self.beklemeModu()
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                self.konus("Seni dinliyorum")
                say=0
            elif ses in emirler.ara:
                if self.key4 == 1:
                    self.reaction()
                    self.local_ara()
                    window.wm_attributes('-alpha', 0)
                elif self. key4 == 0:
                    self.reaction()
                    self.local_ara()
                    window.wm_attributes('-alpha', self.trns.get()/10)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses == 'sayfayı yenile':
                pyautogui.press('f5')
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses == 'çık':
                pyautogui.press('esc')
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses == 'window' or ses == 'windows':
                pyautogui.press('win')
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses == 'topla' or ses == 'toplama işlemi':
                pyautogui.press('+')
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses == 'çıkar' or ses == 'çıkarma işlemi':
                pyautogui.press('-')
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses == 'çarp' or ses == 'çarpma işlemi':
                pyautogui.press('*')
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses == 'böl' or ses == 'bölme işlemi':
                pyautogui.press('/')
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.youtube:
                self.youtube()
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.translate:
                if self.key4 == 1:
                    window.wm_attributes('-alpha', 1)
                ceviri.CeviriYap.ceviriYap(self)
                if self.key4 == 1:
                    window.wm_attributes('-alpha', 0)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.nOt:
                if self.key4 == 1:
                    window.wm_attributes('-alpha', 1)
                noty.Not.notYaz(self)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                if self.key4 == 1:
                    window.wm_attributes('-alpha', 0)
                say=0
            elif ses in emirler.haber:
                haber.HaberOku.haberler(self)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.altın:
                finans.Piyasa.altin(self)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.dolar:
                finans.Piyasa.dolar(self)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.euro:
                finans.Piyasa.euro(self)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.btc:
                finans.Piyasa.bitcoin(self)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.saat:
                saat.Saat.saat()
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.tarih:
                tarih.Tarih.tarih(self)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.hava:
                havaDurumu.HavaDurumu.havaDurumu(self)
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                say=0
            elif ses in emirler.giz_on:
                self.gizMod_on()
                say=0
            elif ses in emirler.giz_of:
                self.gizMod_off()
                say=0
            elif ses == self.name.get():
                if self.key4 == 1:
                    self.konus("Seni dinliyorum")
                    self.reaction()
                    window.wm_attributes('-alpha', 0)
                    self.konus("Kontrol modu açık.")
                elif self.key4 == 0:
                    self.konus("Seni dinliyorum")
                    self.reaction()
                    window.wm_attributes('-alpha', self.trns.get()/10)
                    self.konus("Kontrol modu açık.")
            elif ses == "çift tıkla":
                pyautogui.click(clicks=2)
                say=0
            elif ses in emirler.tikla:
                self.value.set("Kontrol modundasın.\n"
                                "{}".format(emirler.kntrl_metin))
                pyautogui.click(button='left')
                self.yatay = GetSystemMetrics(0)/2
                self.dikey = GetSystemMetrics(1)/2
                w = self.yatay/2
                h = self.dikey/2
                say=0
            elif ses in emirler.ss:
                if self.key4 == 1:
                    window.wm_attributes('-alpha',self.trns.get())
                    eklentiler.Ekler.screens(self)
                    time.sleep(1)
                    window.wm_attributes('-alpha',0)
                elif self.key4 == 0:
                    eklentiler.Ekler.screens(self)
            elif ses in emirler.kontrol_off:
                self.value.set('Kontrol kapatıldı.')
                self.konus('Kontrol kapatıldı')
                self.key2=0
                break
            elif ses in emirler.help:
                say=0
                self.yardim()
            elif ses in emirler.settings:
                say=0
                self.ayarlar()
            elif ses == "programı kapat":
                self.kapat()
            elif say == 533:
                self.value.set('Kontrol kapatıldı.')
                self.konus('Kontrol kapatıldı')
                break

    def local_ara(self):
        self.key5 = 1
        self.duration = 0.2
        self.time_limit = 2
        lokal_say=1
        self.value.set("CTRL+F aktif.\n"
                        "{}".format(emirler.lkl_ara_mtn))
        pyautogui.hotkey('ctrl','f')
        self.konus('Ne arayım')
        while True:
            ses = self.record()
            if ses in emirler.iptal or ses in emirler.kapat or lokal_say == 0:
                pyautogui.press('esc')
                self.value.set('CTRL+F kapatıldı.')
                self.key5=0
                break
            elif type(ses) == str:
                pyperclip.copy(ses)
                pyautogui.hotkey('ctrl','v')
                while True:
                    ses=self.record()
                    if ses == 'sonraki' or ses == 'başka':
                        pyautogui.press('enter')
                    elif ses in emirler.tikla:
                        pyautogui.press('esc')
                        pyautogui.press('enter')
                        lokal_say=0
                        break
                    elif ses == 'geri al':
                        pyautogui.hotkey('ctrl','z')
                        break
                    elif ses in emirler.iptal or ses in emirler.kapat:
                        pyautogui.press('esc')
                        lokal_say=0
                        break

    def yazici(self):
        self.duration = 0.2
        self.time_limit = 2
        self.value.set(emirler.yzc_mtn)
        while True:
            ses = self.record()
            old = pyperclip.paste()
            if ses == "enter":
                pyautogui.press('enter')
                self.value.set("Yazma modundan çıkılıdı.")
                break
            elif ses == "kapat" or ses == 'iptal':
                self.value.set('Yazma modundan çıkıldı.')
                break
            elif ses == 'geri al':
                pyautogui.hotkey('ctrl','z')
                pyautogui.hotkey('ctrl','z')
            elif type(ses) == str:
                pyperclip.copy(ses)
                pyautogui.hotkey('ctrl','v')
                pyautogui.press('space')
                pyperclip.copy(old)

    def reaction(self):
        window.wm_attributes('-alpha', 1)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 0.8)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 0.6)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 0.4)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 0.2)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 1)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 0.8)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 0.6)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 0.4)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 0.2)
        time.sleep(0.05)
        window.wm_attributes('-alpha', 1)

    def beklemeModu(self):
        say=0
        if self.key4 == 1:
            self.konus('Bekleme modu açıldı.')
        elif self.key4 == 0:
            self.reaction()
        while True:
            say+=1
            ses=self.record()
            if ses == self.name.get() and self.key4 == 1:
                self.reaction()
                window.wm_attributes('-alpha', 0)
                break
            elif ses == self.name.get() and self.key4 == 0:
                self.reaction()
                break
            elif say >= 7 and self.key1 == 1 and self.key2 == 1:
                self.value.set("Bekleme modundasın.\n"
                                "Bu moddan çıkmak içim {} demen yeterli.\n"
                                "Açık modlar:\n"
                                "-Youtube modu,\n"
                                "-Kontrol modu.".format(self.name.get()))
            elif say >= 7 and self.key1 == 0 and self.key2 == 1:
                self.value.set("Bekleme modundasın.\n"
                                "Bu moddan çıkmak içim {} demen yeterli.\n"
                                "Açık modlar:\n"
                                "-Kontrol modu.".format(self.name.get()))
            elif say >= 7 and self.key2 == 1 and self.sekme >= 1:
                self.value.set("Bekleme modundasın.\n"
                                "Bu moddan çıkmak içim {} demen yeterli.\n"
                                "Açık modlar:\n"
                                "-Kontrol modu,\n"
                                "-İnternet tarayıcısı.".format(self.name.get()))
            elif say >= 7 and self.key3 == 1:
                self.value.set("Bekleme modundasın.\n"
                                "Bu moddan çıkmak içim {} demen yeterli.\n"
                                "Açık modlar:\n"
                                "-Müzik Modu.".format(self.name.get()))

    def yardim(self):
        win_yardim = Toplevel()
        win_yardim.geometry('835x700')
        win_yardim.attributes('-topmost', True)
        win_yardim.iconbitmap('{}/icon.ico'.format(self.dizin))
        win_yardim.title('YARDIM')
        win_yardim.resizable(0, 0)
        note = Notebook(win_yardim)
        frame0 = Frame(win_yardim)
        lbl0=Label(frame0, text='ASİSTAN İÇİN TEMEL BİLGİLER',  bg='#99CCFF', font=('Calibri',12,'bold'), height=2).pack(fill=BOTH)
        txt0=Text(frame0, font=('Calibri',12),  bg='#CCE5FF')
        txt0.insert(END, help.asis[0])
        txt0.pack(fill=BOTH, expand=True)
        txt0.config(state=DISABLED)
        frame0.pack(fill='both', expand=True)
        frame1 = Frame(win_yardim)
        lbl1=Label(frame1, text='KONTROL MODU HAKKINDA BİLGİLER', bg='#99CCFF', font=('Calibri',12,'bold'), height=2).pack(fill=BOTH)
        txt1=Text(frame1, font=('Calibri',12), bg='#CCE5FF')
        txt1.insert(END, help.kntrl[0])
        txt1.pack(fill=BOTH, expand=True)
        txt1.config(state=DISABLED)
        frame1.pack(fill='both', expand=True)
        frame2 = Frame(win_yardim)
        lbl2=Label(frame2, text='YOUTUBE MODU HAKKINDA BİLGİLER', bg='#99CCFF', font=('Calibri',12,'bold'), height=2).pack(fill=BOTH)
        txt2=Text(frame2, font=('Calibri',12),  bg='#CCE5FF')
        txt2.insert(END, help.ytbe[0])
        txt2.pack(fill=BOTH, expand=True)
        txt2.config(state=DISABLED)
        frame2.pack(fill='both', expand=True)
        frame3 = Frame(win_yardim)
        lbl3=Label(frame3, text='GOOGLE MODU HAKKINDA BİLGİLER', bg='#99CCFF', font=('Calibri',12,'bold'), height=2).pack(fill=BOTH)
        txt3=Text(frame3, font=('Calibri',12),  bg='#CCE5FF')
        txt3.insert(END, help.ggle[0])
        txt3.pack(fill=BOTH, expand=True)
        txt3.config(state=DISABLED)
        frame3.pack(fill='both', expand=True)
        frame4 = Frame(win_yardim)
        lbl4=Label(frame4, text='MÜZİK MODU HAKKINDA BİLGİLER', bg='#99CCFF', font=('Calibri',12,'bold'), height=2).pack(fill=BOTH)
        txt4=Text(frame4, font=('Calibri',12), bg='#CCE5FF')
        txt4.insert(END, help.mzk[0])
        txt4.pack(fill=BOTH, expand=True)
        txt4.config(state=DISABLED)
        frame4.pack(fill='both', expand=True)
        frame5 = Frame(win_yardim)
        lbl5=Label(frame5, text='BEKLEME MODU HAKKINDA BİLGİLER', bg='#99CCFF', font=('Calibri',12,'bold'), height=2).pack(fill=BOTH)
        txt5=Text(frame5, font=('Calibri',12), bg='#CCE5FF')
        txt5.insert(END, help.bkle[0])
        txt5.pack(fill=BOTH, expand=True)
        txt5.config(state=DISABLED)
        frame5.pack(fill='both', expand=True)
        frame6 = Frame(win_yardim)
        lbl6=Label(frame6, text='AYARLAR HAKKINDA BİLGİLER', bg='#99CCFF', font=('Calibri',12,'bold'), height=2).pack(fill=BOTH)
        txt6=Text(frame6, font=('Calibri',12), bg='#CCE5FF')
        txt6.insert(END, help.ayrlar[0])
        txt6.pack(fill=BOTH, expand=True)
        txt6.config(state=DISABLED)
        frame6.pack(fill='both', expand=True)
        frame7 = Frame(win_yardim)
        lbl7=Label(frame7, text='PROFİL HAKKINDA BİLGİLER', bg='#99CCFF', font=('Calibri',12,'bold'), height=2).pack(fill=BOTH)
        txt7=Text(frame7, font=('Calibri',12), bg='#CCE5FF')
        txt7.insert(END, help.prfl[0])
        txt7.pack(fill=BOTH, expand=True)
        txt7.config(state=DISABLED)
        frame7.pack(fill='both', expand=True)
        frame8 = Frame(win_yardim)
        lbl8=Label(frame8, text='PROFİL HAKKINDA BİLGİLER', bg='#99CCFF', font=('Calibri',12,'bold'), height=2).pack(fill=BOTH)
        txt8=Text(frame8, font=('Calibri',12), bg='#CCE5FF')
        txt8.insert(END, help.gzlmod[0])
        txt8.pack(fill=BOTH, expand=True)
        txt8.config(state=DISABLED)
        frame8.pack(fill='both', expand=True)
        note.add(frame0, text=' ASİSTAN ')
        note.add(frame1, text=' Kontrol ')
        note.add(frame2, text=' YoutTube ')
        note.add(frame3, text=' Google' )
        note.add(frame4, text=' Müzik ')
        note.add(frame5, text=' Bekle ')
        note.add(frame6, text=' Ayarlar ')
        note.add(frame7, text=' Profil ')
        note.add(frame8, text=' Gizli Mod ')
        note.pack(fill=BOTH, expand=True)

    def ayarlar(self):
        win_ayar = Toplevel()
        win_ayar.geometry('400x300')
        win_ayar.title(' AYARLAR')
        win_ayar.attributes('-topmost', True)
        win_ayar.iconbitmap('{}/icon.ico'.format(self.dizin))
        win_ayar.resizable(0, 0)
        note_ayar = Notebook(win_ayar)
        frme0 = Frame(win_ayar, bg='#CCE5FF')
        lbl=Label(frme0, text="Değerleri girdikten sonra enter'a basın.", bg='#CCE5FF', font=('Calibri',12,'bold'), relief=GROOVE).pack(fill=X)
        lbl1=Label(frme0,text='Scroll Up     :', bg='#CCE5FF', font=('Calibri',12)).place(x=5,y=60)
        scrollUp = Spinbox(frme0, from_=240, to=960, textvariable=self.scroll_up, font=('Calibri',12)).place(x = 150, y=60)
        lbl2=Label(frme0,text='Scroll Down:', bg='#CCE5FF', font=('Calibri',12)).place(x=5,y=100)
        scrollDown = Spinbox(frme0, from_=240, to=960, textvariable=self.scroll_down, font=('Calibri',12)).place(x = 150, y=100)
        def scrollup():
            scrllu=self.scroll_up.get()
            self.scroll_up.set(scrllu)
        def scrolldown():
            scrlld=self.scroll_down.get()
            self.scroll_down.set(scrlld)
        btn0=Button(frme0, text='UYGULA', bg='#CCE5FF', command=lambda:[scrollup(),scrolldown()], width=8).place(x=160, y=200)
        frme0.pack(fill=BOTH, expand=True)
        frme1 = Frame(win_ayar, bg='#CCE5FF')
        lbl11=Label(frme1, text='1 - 10 aralığında değer giriniz.', font=('Calibri',12,'bold'), bg='#CCE5FF', relief=GROOVE).pack(fill=X)
        seffaf=Spinbox(frme1, from_ = 1, to = 10, textvariable=self.trns, font=('Calibri',12)).place(x = 100, y=100, height=30)
        def trans():
            scale=self.trns.get()/10
            window.wm_attributes('-alpha',scale)
        btn=Button(frme1, text='UYGULA', command= trans, bg='#CCE5FF', width=8).place(x=160, y=200)
        frme1.pack(fill=BOTH, expand=True)
        frme2 = Frame(win_ayar, bg='#CCE5FF')
        lbl21=Label(frme2, text='Kameranızı Seçin.', bg='#CCE5FF', font=('Calibri',12,'bold'), relief=GROOVE).pack(fill=X)
        self.check1=Radiobutton(frme2, text='Dahili Kamera', variable=self.checkvar1, bg='#CCE5FF', font=('Calibri',12), relief=GROOVE, value=1).pack(fill=BOTH, expand=True)
        self.Check2=Radiobutton(frme2, text='Harici Kamera', variable=self.checkvar1, bg='#CCE5FF', font=('Calibri',12), relief=GROOVE, value=2).pack(fill=BOTH, expand=True)
        frme2.pack(fill=BOTH, expand=True)
        note_ayar.add(frme2, text='KamreSeçimi')
        note_ayar.add(frme0, text=' MouseScroll ')
        note_ayar.add(frme1,text=' PencereŞeffaflığı ')
        note_ayar.pack(fill=BOTH, expand=True)

    def gizMod_on(self):
        self.key4=1
        window.wm_attributes('-alpha', 0)
    def gizMod_off(self):
        self.key4=0
        window.wm_attributes('-alpha', self.trns.get()/10)

    def kapat(self):
        self.value.set('\n\nGörüşmek üzere.'
                        '\n\n\n\n\nBye... ;)')
        self.konus('Görüşmek üzere')
        window.destroy()
        sys.exit()
        
    def komut(self,ses):
        if ses in emirler.hava:
            havaDurumu.HavaDurumu.havaDurumu(self)
        elif ses in emirler.saat:
            saat.Saat.saat(self)
        elif ses in emirler.tarih:
            tarih.Tarih.tarih(self)
        elif ses in emirler.how_r_u:
            sohbet.Sohbet.sohbet(self)
        elif ses in emirler.thank:
            self.value.set('Rica ederim,\nSenin için ne yapabilirim?')
            self.konus("Rica ederim")
            self.konus('Senin için ne yapabilirim?')
        elif ses in emirler.hi:
            asd = ["Merhaba", "Selam"]
            secim = choice(asd)
            self.value.set(secim)
            self.konus(secim)
        elif ses in emirler.what_r_u_doing:
            self.value.set('Senin emirlerini bekliyorum')
            self.konus("Senin emirlerini bekliyorum")
        elif ses in emirler.ad:
            self.value.set('Benim adım {}'.format(self.name.get()))
            self.konus("Benim adım {}".format(self.name.get()))
        elif ses in emirler.u_about:
            self.value.set('Ben bir bilgisayarım,\nSenin için ne yapabilirim?')
            self.konus("Ben bir bilgisayarım.")
            self.konus('Senin için ne yapabilirim?')
        elif ses in emirler.search:
            self.googledan()
        elif ses in emirler.ss:
            eklentiler.Ekler.screens(self)
        elif ses in emirler.nOt:
            if self.key4 == 1:
                window.wm_attributes('-alpha', 1)
            noty.Not.notYaz(self)
            if self.key4 == 1:
                window.wm_attributes('-alpha', 0)
        elif ses in emirler.youtube:
            self.youtube()
        elif ses in emirler.haber:
            haber.HaberOku.haberler(self)
        elif ses in emirler.altın:
            finans.Piyasa.altin(self)
        elif ses in emirler.dolar:
            finans.Piyasa.dolar(self)
        elif ses in emirler.euro:
            finans.Piyasa.euro(self)
        elif ses in emirler.btc:
            finans.Piyasa.bitcoin(self)
        elif ses in emirler.translate:
            if self.key4 == 1:
                window.wm_attributes('-alpha', 1)
            ceviri.CeviriYap.ceviriYap(self)
            if self.key4 == 1:
                window.wm_attributes('-alpha', 0)
        elif ses in emirler.muSic:
            self.mUSİc()
        elif ses in emirler.help:
            self.yardim()
        elif ses in emirler.settings:
            self.ayarlar()
        elif ses in emirler.kontrol_on:
            self.kontrol()
        elif ses in emirler.sesEksi:
            eklentiler.Ekler.ses_eksi(self)
        elif ses in emirler.sesArti:
            eklentiler.Ekler.ses_artı(self)
        elif ses in emirler.giz_on:
            self.gizMod_on()
        elif ses in emirler.giz_of:
            self.gizMod_off()
        else:
            self.value.set('\n\n\n\n\nGeçersiz emir.')
            self.konus("geçersiz emir")

    def asistan(self):
        self.key0=1
        if self.key0 == 1:
            self.buton['state']=DISABLED
        say=0
        self.value.set('\n\n\n\n\nEmirlerini Bekliyorum!....')
        while True:
            say+=1
            ses = self.record()
            if ses in emirler.start or ses == self.name.get():
                self.value.set('\n\n\n\n\nSeni dinliyorum ,komutlar aktif.')
                self.reaction()
                window.wm_attributes('-alpha', self.trns.get()/10)
                self.konus('seni dinliyorum')
                say=0
            elif ses in emirler.off:
                self.kapat()
            elif ses in emirler.pause:
                self.value.set("\n\nBekleme Modu açıldı."
                                "\n\n\n\n\nBekleme modundan çıkmak için '{}' demen yererli".format(self.name.get()))
                self.beklemeModu()
                self.value.set('\n\n\n\n\nSeni dinliyorum ,komutlar aktif.')
                self.konus('Seni dinliyorum.')
                say=0
            elif ses != None:
                self.value.set('\n\n\n\n\nSeni dinliyorum ,komutlar aktif.')
                self.komut(ses)
                say=0
            else:
                if say >= 1000:
                    self.value.set('Program Sonlanıyor!...\n\n\n\n\nHoşça Kal!...')
                    self.konus('Hoşça Kal')
                    window.destroy()
                    sys.exit()
                else:
                    self.value1.set('Sen : ...')
                    self.value.set('\n\nBirşey demedin.'
                                    '\n\n\n\n\nEmirlerini bekliyorum.')

    def asist(self):
        threading.Thread(target=self.asistan).start()

window=Tk()
app=Asistan(window)
w=window.winfo_screenwidth()
h=window.winfo_screenheight()
ws=w-360
hs=h-600
window.geometry('350x500+%d+%d'%(ws,hs))
window.attributes('-topmost', True)
window.resizable(0, 0)
dzn=os.getcwd()
window.iconbitmap("{}/icon.ico".format(dzn))
window.title('  ASISTAN 1.0')
window.configure(background='#D5D8DC')
window.mainloop()