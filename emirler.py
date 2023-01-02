#Bilgisayara verilebilecek emir kelimeleri veya cümleleri
start=['bilgisayar','beni dinle','orada mısın','beni duyuyor musun']
pause=['bekle','bekle biraz','biraz bekle','bilgisayar bekle','bekle bilgisayar']
off=['görevini bitir','görevin bitti',"asistan'ı kapat",'işin bitti','programı kapat','programdan çık','program kapat']
saat=['saat kaç','saati söyle','zamanı söyle','şuan saat kaç']
hava=['hava durumunu söyle','bugün hava nasıl','hava durumu']
tarih=['tarihi söyle','bugün ayın kaçı','bugünün tarihini söyle']
how_r_u=['nasılsın','ne haber','nasıl gidiyor','ne var ne yok']
thank=['teşekkürler','sağ ol']
hi=['merhaba','selam']
what_r_u_doing=['ne yapıyorsun']
ad=['adın ne','ismin ne']
u_about=['kendinden bahset']
search=["internet'te arama yap","google'da arama yap",'google arama yap',"arama yap google'da",'google aç',"google'u aç"]
ss=['ekran görüntüsü al','ekran resmi al']
nOt=['not al','not yaz','dediklerimi not al']
youtube=['youtube aç','youtube']
haber=['haber oku','haberler']
translate=['çeviri yap','tercüme et']
altın=['altın kaç lira','altın kaç TL','altın kaç']
dolar=['dolar kaç lira','dolar kaç TL','dolar kaç']
euro=['avro kaç lira','euro kaç lira','avro kaç TL','euro kaç TL','euro kaç','avro kaç']
btc=['bitcoin kaç dolar','bitcoin kaç']

help=['yardım aç','yardımı aç','yardım','yardım et', 'yardımcı ol', 'bana nasıl yardımcı olabilirsin']
settings=['ayarları aç','ayarlar','ayarlar aç']

#anlamadığında yapacakları
y_n_o=['evet','olur','tamam ara','ara','tamam','evet ara','olur ara']
hayır=['hayır','hayır arama','arama','hayır gerek yok']
evet=['evet söyle','evet','söyle']

down=['aşağı','aşağı in','aşağıyı göster','sayfanın aşağısını göster','alttakileri göster','in']
up=['yukarıyı göster','yukarı','sayfanın yukarısını göster','sayfanın yukarısına çık','yukarı çık']
iptal=['iptal','iptal et','aramayı iptal et']
ses_ac_kapat=['sesi kapat','sesi aç','kapat sesi','aç sesi']
kapat=['kapat','youtube kapat','hesap makinesini kapat','hesaplamayı bitir','çık','hesap makinesinden çık']
back=['geri dön','önceki sayfaya dön','dön geri','dön geriye']
next=['sonraki sayfaya dön','sonraki sayfa','ileri sayfa']

#Kontrol için emir listesi
kontrol_on=['kontrol aç','kontrolü aç','kontrol',]
kontrol_off=['kontrol kapat','kontrolü kapat','kapat kontrolü','kapat kontrol']
sag=['sağ','doğu','sağ yan','sağ tarafa','sağa','sağ taraf']
sol=['sol','batı','sol yan','sol tarafa','sola','sol taraf']
yukarı=['yukarı','kuzey']
asagi=['aşağı','güney']
orta=['ortala','ortaya','merkez','herkes','orta']
tikla=['tıkla','bunu aç','aç','aç bunu','aç şunu']
scrll_down=['indir','aşağı indir','sayfayı aşağı indir','aşağıyı göster']
scrll_up=['yukarıyı göster','yukarı çık','sayfayı yukarı kaydır','yukarı göster','yukarıya çık']

#ctrl +f
ara = ['ara','dediğimi ara','arama yap']

#Bekleme/Devam etme 
bekle=['bekle','youtube bekle','bekle biraz','biraz bekle','bekleme modu','bekleme modunu aç']

sesEksi=['sesi azalt','sesi kıs','azalt sesi']
sesArti=['sesi arttır','sesi yükselt','daha fazla ses','arttır']
ileriSar=['ileri sar','videoyu ilerlet','video ileri','videoyu ileri sar']
geriSar=['geri sar','videoyu geri sar','video geri']

sohbet=["İyiyim teşekkürler sen nasılsın?", "İyiyim sağol seni sormalı", "Herşey yolunda, sende durumlar nasıl"]

mix=['karışık', 'rastgele', 'sen tercih et']
change=['değiştir', 'başka müzik aç','başka kanal aç','müziği değiştir','kanalı değiştir']
muSic=['müzik aç','müzik','aç müzik']
muSic_off=['müziği kapat','kapat müziği','kapat']
müzikler=['müzikleri söyle','hangi müzikler var','müzik listesini söyle','müzikleri söyle','kanalları söyle']

giz_on=['gizli mod aç','gizli modu aç','gizli mod']
giz_of=['gizli mod kapat','gizli modu kapat','kapat gizli modu']

#bilgilendirme metinleri
kntrl_metin=("-Sanal mouse açmak istersen 'mouse aç' diyebilirsin.\n"
            "-Sanal mouse kullanırken sesli komutlar kapatılır!...\n"
            "-Mouse'u sağ tarafa kaydırmak için \n'sağ taraf'\n"
            "-Mouse'u sol tarafa kaydırmak için \n'sol taraf'\n"
            "-Mouse'u yukarı tarafa kaydırmak için 'yukarı'\n"
            "-Mouse'u ağaşı tarafa kaydırmak için\n'aşağı'\n"
            "-Mouse'u ortalamak için 'ortala'\n"
            "-Kontrol'u kapatmak için 'kapat'\n"
            "-Sayfayı aşağı indirmek için 'indir'\n"
            "-Sayfayı yukarı çıkarmak için 'yukarı çık'\n"
            "-Ekstra komutlar için KOMUTLAR sayfası!...")

lkl_ara_mtn=("-Sayfadaki aramak istediğinizi kısaca söyleyin;\n"
            "-'sonraki' ya da 'başka' dedikçe sayfada bulduklarında gezinirsiniz.\n"
            "-Aradığınıza geldiğinizde 'tıkla' ya da 'bunu aç' deyin.\n"
            "-Yanlış yazılırsa 'geri al' komutunu ver ve tekrar söyle.\n"
            "-CTRL+F kapatmak için 'iptal' ya da 'kapat' demen yeterli.")

mzk_mtn=("Müzik modu açıldı.\n"
            "-Kanalları/müzikleri öğrenmek için 'kanalları söyle', 'müzikleri söyle'\n"
            "-Bekletmek için 'bekle',\n"
            "-Kapatmak için 'kapat' veya 'müziği kapat',\n"
            "-Sesi komple açmak/kapatmak için 'sesi aç' veya 'sesi kapat',\n"
            "-Sesi kısmak/yükseltmek için 'sesi azalt' veya 'sesi yükselt',\n"
            "-Listenizdeki herhangi bir müziği açmak için 'rastgele' ya da 'karışık'"
            "Diyebilirsin.\n\n"
            "Müzik eklemek için Menu'den Müzik penceresinde ekleme yapabilirsin.\n"
            "-Müzik ya da dinlemek istediğiniz müziğin linkini 'Müzik Linki' kısmına yazın,\n"
            "-Müzik ya da dinlemek istediğiniz müziğe isim verin 'Müzik Adı' kısmında.")

yzc_mtn=("Yazma modu açık.\n"
        "Bitirmek ve onaylamak için 'enter' demen yeterli.\n"
        "İptal için 'iptal' ya da 'kapat' diyebilirsin.\n"
        "Yazılan hatalıysa 'geri al' diyebilirsin.\n"
        "'enter' kelimiseini yazıldığı gibi söyleyin.")