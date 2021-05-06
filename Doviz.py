# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import locale
import time
from datetime import datetime
from gtts import gTTS
from playsound import playsound
import random
import os

locale.setlocale(locale.LC_ALL,"")

url = "https://www.doviz.com/"

response = requests.get(url)

html_icerigi = response.content

soup = BeautifulSoup(html_icerigi,"html.parser")

names = soup.find_all("span",{"class":"name"})

values = soup.find_all("span",{"class":"value"})

şuan=datetime.now()
print("""
      MERHABA. BORSA BİLGİLERİNİ BURADAN ÖĞRENEBİLİRSİNİZ.
      DEĞERLERİ KAYDETMEK İÇİN 1;
      DEĞERLERİ GÖRMEK İÇİN 2;
      ÇIKMAK İÇİN 3'E BASIN.
      """)

def degerleri_yazdir():
    for name,value in zip(names,values):
        name = name.text
        name = name.strip()
        name = name.replace("\n","")
        value = value.text
        value = value.strip()
        value = value.replace("\n","")
        
        with open("degerler.txt","a",encoding="utf-8") as file:
            file.write(name)
            file.write(" ")
            file.write(":")
            file.write(value)
            file.write("\n")
            
def birlestir():
    for name,value in zip(names,values):
        name = name.text
        name = name.strip()
        name = name.replace("\n","")
        value = value.text
        value = value.strip()
        value = value.replace("\n","")
        print(name,":",value)
        

def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3' 
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Merhaba.Belirtilen tabloya göre, lütfen yapmak istediğiniz işlemin değerini girer misiniz?")

while 1:
    try:
        a = int(input("işlem:"))
        
        if (a==2):
            
            print(datetime.strftime(şuan,"%d %B %Y"),"tarihinden itibaren güncel değerler :")
            
            time.sleep(0.5)
            
            birlestir()
            
            speak("{} tarihinden itibaren güncel değerleri yazdırdım.".format(datetime.strftime(şuan,"%d %B %Y")))
            speak("Yapmamı istediğiniz başka bir işlem var mı?")
        elif(a==1):
            
            degerleri_yazdir()
            speak("Değerleri {} konumuna yazdırdım.".format(os.getcwd()))
            speak("Yapmamı istediğiniz başka bir işlem var mı?")
        elif(a==3):
            
            speak("İyi günler.")
            break
        else:
            
            speak("Lütfen geçerli bir değer girin..")
    except:
        speak("Lütfen geçerli bir değer girin..")
              
                
        