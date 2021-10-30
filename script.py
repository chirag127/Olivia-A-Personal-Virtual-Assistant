from bs4 import BeautifulSoup
from googletrans import Translator
import ctypes
import datetime
import json
import operator
import os
import pyttsx3  # pip install pyttsx3
import random
import requests
import shutil
import smtplib
import speech_recognition as sr  # pip install speechRecognition
import subprocess
import sys
import time
import tkinter
import webbrowser
import wikipedia  # pip install wikipedia
import win32com.client as wincl
import winshell
import pyautogui  # pip install pyautogui

# I was getting error so i install pyaudio
# error in that too so i googled it on the stackover flow.

"""
# Text to Speech Engine
# Define Text to Speech Engine

"""


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am olivia Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def takescreenshot():
    subprocess.call(["screencapture", "-x", "image.png"])
    speak("Sir, I have taken a screenshot of your screen")


myScreenshot = pyautogui.screenshot()
myScreenshot.save(r'C:\Users\Ron\Desktop\Test\screenshot_1.png')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chriagsinghal@gmail.com', 'my password')
    server.sendmail('chiragsinghal@gmail.com', to, content)
    server.close()


def exitcode():
    sys.exit()


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def sp(text):
    print(text)
    speak(text)


def givejoke():
    response_API = requests.get(
        'https://icanhazdadjoke.com/slack')
    data = response_API.text
    parse_json = json.loads(data)
    key = parse_json['attachments']
    joketext = key[0]['text']
    print("The random joke is ", joketext)
    speak(joketext)


def translatelanguage(languageptext):
    query = takeCommand().lower()
    if languageptext in query:
        query = query.replace(languageptext, "")
        k = Translator().translate(query, dest=languageptext)
        translated = str(k.text)
        sp(translated)


def clear():
    return os.system('cls')


def open_chrome():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open('https://www.google.com')


def ctime():
    now = datetime.datetime.now()
    speak("The current time is")
    speak(now.strftime("%I:%M:%S"))


def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("Welcome Mister")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you, Sir")


alllanguage = ['afrikaans',
               'albanian',
               'amharic',
               'arabic',
               'armenian',
               'azerbaijani',
               'basque',
               'belarusian',
               'bengali',
               'bosnian',
               'bulgarian',
               'catalan',
               'cebuano',
               'chichewa',
               'corsican',
               'croatian',
               'czech',
               'danish',
               'dutch',
               'english',
               'esperanto',
               'estonian',
               'filipino',
               'finnish',
               'french',
               'frisian',
               'galician',
               'georgian',
               'german',
               'greek',
               'gujarati',
               'haitian creole',
               'hausa',
               'hawaiian',
               'hebrew',
               'hindi',
               'hmong',
               'hungarian',
               'icelandic',
               'igbo',
               'indonesian',
               'irish',
               'italian',
               'japanese',
               'javanese',
               'kannada',
               'kazakh',
               'khmer',
               'korean',
               'kurdish (kurmanji)',
               'kyrgyz',
               'lao',
               'latin',
               'latvian',
               'lithuanian',
               'luxembourgish',
               'macedonian',
               'malagasy',
               'malay',
               'malayalam',
               'maltese',
               'maori',
               'marathi',
               'mongolian',
               'myanmar (burmese)',
               'nepali',
               'norwegian',
               'odia',
               'pashto',
               'persian',
               'polish',
               'portuguese',
               'punjabi',
               'romanian',
               'russian',
               'samoan',
               'scots gaelic',
               'serbian',
               'sesotho',
               'shona',
               'sindhi',
               'sinhala',
               'slovak',
               'slovenian',
               'somali',
               'spanish',
               'sundanese',
               'swahili',
               'swedish',
               'tajik',
               'tamil',
               'telugu',
               'thai',
               'turkish',
               'ukrainian',
               'urdu',
               'uyghur',
               'uzbek',
               'vietnamese',
               'welsh',
               'xhosa',
               'yiddish',
               'yoruba',
               'zulu'
               ]


if __name__ == "__main__":
    # wishMe()

    clear()

    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        #  if 'olivia' in query:
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            sp(results)

        elif 'open' in query:
            print("opening.....")
            query = query.replace("open ", "")

            if 'edge' in query:
                if 'youtube' in query:
                    webbrowser.register('edge',
                                        None,
                                        webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
                    webbrowser.get('edge').open(
                        "https://www.youtube.com/feed/subscriptions")

            elif 'youtube' in query:

                webbrowser.open("https://www.youtube.com/")

            elif 'google' in query:
                webbrowser.open("https://www.google.com/")

            elif 'stack overflow' in query:
                webbrowser.open("https://www.stackoverflow.com/")

            elif 'flipkart' in query:
                webbrowser.open("https://www.flipkart.com/")

            else:
                webbrowser.open(
                    f"https://duckduckgo.com/?q=%21+{query}&ia=olivia")

        elif 'Call Me' in query:
            speak('What is your name?')
            query = query.replace("call me", "")
            uname = query
            speak('Hello ' + uname + ' How may I help you?')

        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            uname = query

        elif 'hello' in query:
            speak("hello")
            wishMe()

        elif 'what you' in query:
            sp("I am olivia. I Wish you According to the time of the day. I can Open websites like Google ,Youtube ,flipkart ,Stackoverflow. Give you a joke. Search websites like Google ,YouTube. Give the Introduction of someone or something according to wikipedia. Play music. Stop listening. Tell the current time. send email to someone.")

        elif 'wish me' in query:
            wishMe()

        elif 'play video' in query:
            music_dir = 'D:\\non critical\\video'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play music' in query or "play song" in query:
            sp("Here you go with music")
            music_dir = "C:\\Users\\hp\\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif 'email to chirag' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "chriagsinghal@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend chirag sir. I am not able to send this email")

        elif 'stop music' in query:
            os.close("C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe")

        elif 'search' in query:
            speak('Searching ...')
            query = query.replace("search ", "")
            query = query.replace(" on ", "")

            if 'youtube' in query:
                query = query.replace("youtube", "")
                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={query}")

            elif 'flipkart' in query:
                query = query.replace("flipkart", "")
                webbrowser.open(
                    f"https://www.flipkart.com/search?q={query}&otracker1=olivia")
            else:
                query = query.replace("google", "")

                webbrowser.open(
                    f"https://www.google.com/search?q={query}&sourceid=olivia")
        elif 'clear' in query:
            clearConsole()

        elif 'joke' in query:
            givejoke()

        elif 'kill me' in query:
            sp("I won't")

        elif 'your god' in query:
            sp("chriag singhal is my god")

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:
            speak("I was built by Chirag singhal")

        elif 'exit' in query:
            sp("exiting........")
            exitcode()

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            sp("User asked to Locate")
            sp(location)
            webbrowser.open(
                "https://www.google.com / maps / place/" + location + "")

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif 'translate' in query:
            query = query.replace("translate", "")
            query = query.replace("to", "")

            if 'spanish' in query:
                query = query.replace("spanish", "")
                k = Translator().translate(query, dest='spanish')
                translated = str(k.text)
                sp(translated)

            elif 'hindi' in query:
                query = query.replace("hindi", "")
                k = Translator().translate(query, dest='hindi')
                translated = str(k.text)
                sp(translated)
            elif 'french' in query:
                query = query.replace("french", "")
                k = Translator().translate(query, dest='french')
                translated = str(k.text)
                sp(translated)
            elif 'german' in query:
                query = query.replace("german", "")
                k = Translator().translate(query, dest='german')
                translated = str(k.text)
                sp(translated)
            elif 'dutch' in query:
                query = query.replace("dutch", "")
                k = Translator().translate(query, dest='dutch')
                translated = str(k.text)
                sp(translated)

            elif 'italian' in query:
                query = query.replace("italian", "")
                k = Translator().translate(query, dest='italian')
                translated = str(k.text)
                sp(translated)

            elif 'portuguese' in query:
                query = query.replace("portuguese", "")
                k = Translator().translate(query, dest='portuguese')
                translated = str(k.text)
                sp(translated)

            elif 'russian' in query:
                query = query.replace("russian", "")
                k = Translator().translate(query, dest='russian')
                translated = str(k.text)
                sp(translated)

            elif 'turkish' in query:
                query = query.replace("turkish", "")
                k = Translator().translate(query, dest='turkish')
                translated = str(k.text)
                sp(translated)

            elif 'chinese' in query:
                query = query.replace("chinese", "")
                k = Translator().translate(query, dest='chinese')
                translated = str(k.text)
                sp(translated)

            elif 'japanese' in query:
                query = query.replace("japanese", "")
                k = Translator().translate(query, dest='japanese')
                translated = str(k.text)
                sp(translated)

            elif 'korean' in query:
                query = query.replace("korean", "")
                k = Translator().translate(query, dest='korean')
                translated = str(k.text)
                sp(translated)

            elif 'arabic' in query:
                query = query.replace("arabic", "")
                k = Translator().translate(query, dest='arabic')
                translated = str(k.text)
                sp(translated)

            elif 'bengali' in query:
                query = query.replace("bengali", "")
                k = Translator().translate(query, dest='bengali')
                translated = str(k.text)
                sp(translated)

            elif 'telugu' in query:
                query = query.replace("telugu", "")
                k = Translator().translate(query, dest='telugu')
                translated = str(k.text)
                sp(translated)

            elif 'thai' in query:
                query = query.replace("thai", "")
                k = Translator().translate(query, dest='thai')
                translated = str(k.text)
                sp(translated)

            elif 'vietnamese' in query:
                query = query.replace("vietnamese", "")
                k = Translator().translate(query, dest='vietnamese')
                translated = str(k.text)
                sp(translated)

            elif 'urdu' in query:
                query = query.replace("urdu", "")
                k = Translator().translate(query, dest='urdu')
                translated = str(k.text)
                sp(translated)

            elif 'malayalam' in query:
                query = query.replace("malayalam", "")
                k = Translator().translate(query, dest='malayalam')
                translated = str(k.text)
                sp(translated)

            elif 'gujarati' in query:
                query = query.replace("gujarati", "")
                k = Translator().translate(query, dest='gujarati')
                translated = str(k.text)
                sp(translated)

            elif 'punjabi' in query:
                query = query.replace("punjabi", "")
                k = Translator().translate(query, dest='punjabi')
                translated = str(k.text)
                sp(translated)

            elif 'malay' in query:
                query = query.replace("malay", "")
                k = Translator().translate(query, dest='malay')
                translated = str(k.text)
                sp(translated)

            elif 'tamil' in query:
                query = query.replace("tamil", "")
                k = Translator().translate(query, dest='tamil')
                translated = str(k.text)
                sp(translated)

            elif 'sinhala' in query:
                query = query.replace("sinhala", "")
                k = Translator().translate(query, dest='sinhala')
                translated = str(k.text)
                sp(translated)

            elif 'burmese' in query:
                query = query.replace("burmese", "")
                k = Translator().translate(query, dest='burmese')
                translated = str(k.text)
                sp(translated)

            elif 'khmer' in query:
                query = query.replace("khmer", "")
                k = Translator().translate(query, dest='khmer')
                translated = str(k.text)
                sp(translated)

            elif 'czech' in query:
                query = query.replace("czech", "")
                k = Translator().translate(query, dest='czech')
                translated = str(k.text)
                sp(translated)

            elif 'danish' in query:
                query = query.replace("danish", "")
                k = Translator().translate(query, dest='danish')
                translated = str(k.text)
                sp(translated)

            elif 'polish' in query:
                query = query.replace("polish", "")
                k = Translator().translate(query, dest='polish')
                translated = str(k.text)
                sp(translated)

            elif 'icelandic' in query:
                query = query.replace("icelandic", "")
                k = Translator().translate(query, dest='icelandic')
                translated = str(k.text)
                sp(translated)

            elif 'ukrainian' in query:
                query = query.replace("ukrainian", "")
                k = Translator().translate(query, dest='ukrainian')
                translated = str(k.text)
                sp(translated)

            elif 'french' in query:
                query = query.replace("french", "")
                k = Translator().translate(query, dest='french')
                translated = str(k.text)
                sp(translated)

            elif 'italian' in query:
                query = query.replace("italian", "")
                k = Translator().translate(query, dest='italian')
                translated = str(k.text)
                sp(translated)

            elif 'portuguese' in query:
                query = query.replace("portuguese", "")
                k = Translator().translate(query, dest='portuguese')
                translated = str(k.text)
                sp(translated)

            elif 'spanish' in query:

                query = query.replace("spanish", "")
                k = Translator().translate(query, dest='spanish')
                translated = str(k.text)
                sp(translated)

            elif 'german' in query:

                query = query.replace("german", "")
                k = Translator().translate(query, dest='german')
                translated = str(k.text)
                sp(translated)

            elif 'estonian' in query:

                query = query.replace("estonian", "")
                k = Translator().translate(query, dest='estonian')
                translated = str(k.text)
                sp(translated)

            elif 'norwegian' in query:

                query = query.replace("norwegian", "")
                k = Translator().translate(query, dest='norwegian')
                translated = str(k.text)
                sp(translated)

            elif 'chinese' in query:
                query = query.replace("chinese", "")

                if 'traditional' in query:
                    query = query.replace("traditional", "")
                    query = query.replace("simplified", "")

            elif 'azerbaijani' in query:

                query = query.replace("azerbaijani", "")
                k = Translator().translate(query, dest='azerbaijani')
                translated = str(k.text)
                sp(translated)

            elif 'farsi' in query:

                query = query.replace("farsi", "")
                k = Translator().translate(query, dest='farsi')
                translated = str(k.text)
                sp(translated)

            elif 'hindi' in query:

                query = query.replace("hindi", "")
                k = Translator().translate(query, dest='hindi')
                translated = str(k.text)
                sp(translated)

        elif 'how are you' in query:
            speak("i am fine")
        elif 'what time is it' in query:
            speak(ctime())
        elif 'who are you' in query:
            speak("i am olivia")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Ron\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open chrome' in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif 'open notepad' in query:
            notepadPath = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(notepadPath)

        elif 'open visual studio' in query:
            visualStudioPath = "C:\\Program Files\\Microsoft Visual Studio\\2019\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(visualStudioPath)

        elif 'open visual studio code' in query:
            visualStudioCodePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(visualStudioCodePath)

        elif 'open sublime text' in query:
            sublimeTextPath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
            os.startfile(sublimeTextPath)

        elif 'open pycharm' in query:
            pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
            os.startfile(pycharmPath)

        elif 'open notepad++' in query:
            notepadPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(notepadPath)

""""        




"""
