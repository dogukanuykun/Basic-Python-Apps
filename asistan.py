import speech_recognition as sr
import time
from datetime import datetime
import webbrowser
from gtts import gTTS
from playsound import playsound
import random
import os

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            speak("ne dediğini anlamadım")
        except sr.RequestError:
            speak("Sistemi çalıştıramadım efendim")
        return voice

def response(voice):
    if 'nasılsın' in voice:
        speak("iyiyim reis sen")
    if 'saat kaç' in voice:
        speak("Saat {} efendim.".format(datetime.now().strftime('%H:%M:%S')))
    if 'arama' in voice:
        search = record('ne aramamı istersiniz')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        speak(search+'için bunları buldum efendim.')
    if 'tamamdır' in voice:
        speak('İyi günler efendim.')
        exit()

def speak(string):
    tts = gTTS(string,lang='tr')
    rand = random.randint(1,10000)
    file = 'audio-'+str(rand)+'.mp3' 
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("merhaba efendim")
time.sleep(0.1)
while 1:
    voice = record()
    print(voice)
    response(voice)
