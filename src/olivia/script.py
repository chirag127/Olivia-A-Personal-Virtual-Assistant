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
import pywhatkit


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
myScreenshot.save(r'D:\dl\Critical\code\screenshot_1.png')


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


def greeting(text):
    # Greeting inputs
    GREETING_INPUTS = ['hi', 'hey', 'hola', 'wassup', 'hello']

    # Greeting response
    GREETING_RESPONSES = ['howdy', 'all that good', 'hello master', 'heythere']

    # If users input is a greeting, then return a randomly chosen greetng response
    for word in text.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES) + '.'

    # If no greeting was detected
    return ''


def givejoke():
    response_API = requests.get(
        'https://icanhazdadjoke.com/slack')
    data = response_API.text
    parse_json = json.loads(data)
    key = parse_json['attachments']
    joketext = key[0]['text']
    print("The random joke is ", joketext)
    speak(joketext)


def giveip():
    response_API = requests.get(
        'https://api.ipify.org?format=json')
    data = response_API.text
    parse_json = json.loads(data)
    key = parse_json['ip']
    iptext = key
    sp("Your IP address is ")
    sp(iptext)


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


if __name__ == "__main__":
    # wishMe()

    while True:

        query = takeCommand().lower()

        # Logic for executing tasks based on query
        #  if 'olivia' in query:
        #     speak("Yes Sir")

        if 'open chrome' in query:
            open_chrome()

        elif 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'search in chrome' in query:
            speak("What should i search for sir")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()
            webbrowser.get(chromepath).open(
                'https://www.google.com/search?q=' + search)

        elif 'time' in query:
            ctime()

        elif 'username' in query:
            username()

        elif 'clear' in query:
            clearConsole()

        elif 'exit' in query:
            exitcode()

        elif 'screenshot' in query:
            takescreenshot()

        elif 'joke' in query:
            givejoke()

        elif 'ip address' in query:
            giveip()

        elif 'call me' in query:
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
        elif 'email to chirag' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "chriagsinghal@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak(
                    "Sorry my friend chirag sir. I am not able to send this email")

        elif 'stop music' in query:
            os.close("C:\\Program Files\\DAUM\\PotPlayer\\PotPlayerMini64.exe")

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
            speak(
                "for how much time you want to stop jarvis from listening commands")
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
            file = open('olivianote.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()

            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%m-%d-%Y %T:%M%p")
                file.write(strTime)
                file.write(" :- ")
                file.write("\n")
                file.write(note)
                speak("Note has been saved")
            else:
                file.write(note)
                speak("Note has been saved without date and time")

        elif "read a note" in query:
            speak("Reading Note Sir")
            file = open('olivianote.txt', 'r')
            print(file.read())
            speak(file.read(6))

        elif "show note" in query:
            speak("Showing Notes")
            file = open("olivianote.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "delete note" in query:
            speak("Deleting Notes")
            os.remove("olivianote.txt")

        elif 'play' in query:
            song = query.replace('play', '')
            sp('playing ')
            sp(song)
            pywhatkit.playonyt(song)

        elif 'search' in query:
            sp('Searching ...')
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

            elif 'google' in query:
                query = query.replace("google", "")
                webbrowser.open(
                    f"https://www.google.com/search?q={query}&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjNy7Ph39ndAhXGFYgKHcc8D_AQ_AUoAXoECAsQAw&biw=1366&bih=657")

            elif 'stack overflow' in query:
                query = query.replace("stack overflow", "")
                webbrowser.open(
                    f"https://stackoverflow.com/search?q={query}")

            elif 'wikipedia' in query:
                query = query.replace("wikipedia", "")
                webbrowser.open(
                    f"https://en.wikipedia.org/wiki/{query}")

            elif 'facebook' in query:
                query = query.replace("facebook", "")
                webbrowser.open(
                    f"https://www.facebook.com/search/top/?q={query}")  # facebook

            elif 'instagram' in query:
                query = query.replace("instagram", "")
                webbrowser.open(
                    f"https://www.instagram.com/{query}")

            elif 'twitter' in query:
                query = query.replace("twitter", "")
                webbrowser.open(
                    f"https://www.twitter.com/{query}")

            elif 'linkedin' in query:
                query = query.replace("linkedin", "")
                webbrowser.open(
                    f"https://www.linkedin.com/in/{query}")

            elif 'google' in query:
                query = query.replace("google", "")
                webbrowser.open(
                    f"https://www.google.com/search?q={query}")

            elif 'amazon' in query:
                query = query.replace("amazon", "")
                webbrowser.open(
                    f"https://www.amazon.in/s?k={query}")

            elif 'ebay' in query:
                query = query.replace("ebay", "")
                webbrowser.open(
                    f"https://www.ebay.com/sch/i.html?_nkw={query}")

            elif 'netflix' in query:
                query = query.replace("netflix", "")
                webbrowser.open(
                    f"https://www.netflix.com/search?q={query}")

            elif 'spotify' in query:
                query = query.replace("spotify", "")
                webbrowser.open(
                    f"https://open.spotify.com/search/{query}")

            elif 'snapchat' in query:
                query = query.replace("snapchat", "")
                webbrowser.open(
                    f"https://www.snapchat.com/search/{query}")

            elif 'pinterest' in query:
                query = query.replace("pinterest", "")
                webbrowser.open(
                    f"https://www.pinterest.com/search/{query}")

            elif 'quora' in query:
                query = query.replace("quora", "")
                webbrowser.open(
                    f"https://www.quora.com/{query}")
            else:
                query = query.replace("google", "")

                webbrowser.open(
                    f"https://www.google.com/search?q={query}&sourceid=olivia")

        elif 'how are you' in query:
            speak("i am fine")
        elif 'what time is it' in query:
            speak(ctime())
        elif 'who are you' in query:
            speak("i am olivia")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open' in query:
            speak("okay")
            query = query.replace("open ", "")

            if 'control panel' in query:
                speak("okay")
                os.system("control")

            elif 'quick assist' in query:
                speak("okay")
                os.system("quickassist")

            elif 'game panel' in query:
                speak("okay")
                os.system("gamepanel")

            elif 'command prompt' in query:
                speak("okay")
                os.system("cmd")

            elif 'edge' in query:
                if 'youtube' in query:
                    webbrowser.register('edge',
                                        None,
                                        webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
                    webbrowser.get('edge').open(
                        "https://www.youtube.com/feed/subscriptions")

                else:
                    webbrowser.register('edge',
                                        None,
                                        webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
                    webbrowser.get('edge').open(
                        "https://www.google.com/")

            elif 'chrome' in query:
                speak("okay")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)

            elif 'control panel' in query:
                controlPanelPath = "Windows\\System32\\control.exe"
                os.startfile(controlPanelPath)

            elif 'notepad' in query:
                notepadPath = "C:\Windows\System32\notepad.exe"
                os.startfile(notepadPath)

            elif 'calculator' in query:
                calculatorPath = "C:\Windows\System32\calc.exe"
                os.startfile(calculatorPath)

            elif 'task manager' in query:
                taskManagerPath = "C:\Windows\System32\taskmgr.exe"
                os.startfile(taskManagerPath)

            elif 'firefox' in query:
                speak("okay")
                firefoxPath = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                os.startfile(firefoxPath)

            elif 'word' in query:
                speak("okay")
                wordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(wordPath)

            elif 'excel' in query:
                speak("okay")
                excelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(excelPath)

            elif 'powerpoint' in query:
                speak("okay")
                powerpointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(powerpointPath)

            elif 'paint' in query:
                speak("okay")
                paintPath = "C:\\Windows\\System32\\mspaint.exe"
                os.startfile(paintPath)

            elif 'camera' in query:
                speak("okay")
                cameraPath = "C:\\Windows\\System32\\mspaint.exe"
                os.startfile(cameraPath)

            elif 'media player' in query:

                speak("okay")
                mediaPlayerPath = "C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"
                os.startfile(mediaPlayerPath)

            elif 'setting' in query:
                speak("okay")
                settingPath = "C:\\Windows\\System32\\control.exe"
                os.startfile(settingPath)

            elif 'wordpad' in query:
                speak("okay")
                wordpadPath = "C:\\Windows\\System32\\wordpad.exe"
                os.startfile(wordpadPath)

            elif 'calculator' in query:

                speak("okay")
                calculatorPath = "C:\\Windows\\System32\\calc.exe"
                os.startfile(calculatorPath)

            elif 'mspaint' in query:
                speak("okay")
                mspaintPath = "C:\\Windows\\System32\\mspaint.exe"
                os.startfile(mspaintPath)

            elif 'chrome' in query:
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)

            elif 'sublime text' in query:
                sublimeTextPath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
                os.startfile(sublimeTextPath)

            elif 'pycharm' in query:
                pycharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.1.3\\bin\\pycharm64.exe"
                os.startfile(pycharmPath)

            elif 'notepad++' in query:
                notepadPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
                os.startfile(notepadPath)

            elif 'vlc' in query:
                vlcPath = "C:\\Program Files\\VideoLAN\\VLC\\vlc.exe"
                os.startfile(vlcPath)

            elif 'pot player' in query:
                potPlayerPath = "C:\\Program Files\\PotPlayer\\PotPlayerMini64.exe"
                os.startfile(potPlayerPath)

            elif 'github desktop' in query:
                githubPath = "C:\\Users\\hp\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe"
                os.startfile(githubPath)

            elif 'treesize free' in query:
                treesizefreePath = "C:\\Program Files\\TreesizeFree\\TreesizeFree.exe"
                os.startfile(treesizefreePath)

            elif 'microsoft store' in query:
                microsoftStorePath = "C:\\Program Files\\Microsoft Store\\Microsoft Store.exe"
                os.startfile(microsoftStorePath)

            elif 'microsoft edge' in query:
                microsoftEdgePath = "C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe"
                os.startfile(microsoftEdgePath)

            elif 'microsoft mail' in query:
                microsoftMailPath = "C:\\Program Files\\Microsoft\\Windows Live Mail\\wlmail.exe"
                os.startfile(microsoftMailPath)

            elif 'microsoft office' in query:
                microsoftOfficePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(microsoftOfficePath)

            elif 'microsoft word' in query:
                microsoftWordPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
                os.startfile(microsoftWordPath)

            elif 'microsoft excel' in query:

                microsoftExcelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(microsoftExcelPath)

            elif 'microsoft powerpoint' in query:
                microsoftPowerpointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(microsoftPowerpointPath)

            elif 'app' in query:

                if 'open spotify' in query:
                    spotifyPath = "C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe"
                    os.startfile(spotifyPath)

                elif 'open whatsapp' in query:
                    whatsappPath = "C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
                    os.startfile(whatsappPath)

                elif 'open discord' in query:
                    discordPath = "C:\\Users\\hp\\AppData\\Local\\Discord\\Update\\Discord.exe"
                    os.startfile(discordPath)

                elif 'open gmail' in query:
                    gmailPath = "C:\\Users\\hp\\AppData\\Local\\Gmail\\Google Gmail.exe"
                    os.startfile(gmailPath)

            elif 'firefox' in query:
                sp("Firefox is opening")
                webbrowser.open(
                    "https://www.mozilla.org/en-US/firefox/new/")

            elif 'youtube' in query:
                speak("Youtube is opening")
                webbrowser.open("https://www.youtube.com/")

            elif 'facebook' in query:
                speak("Facebook is opening")
                webbrowser.open("https://www.facebook.com/")

            elif 'whatsapp' in query:
                speak("Whatsapp is opening")
                webbrowser.open("https://web.whatsapp.com/")

            elif 'instagram' in query:
                speak("Instagram is opening")
                webbrowser.open("https://www.instagram.com/")

            elif 'twitter' in query:
                speak("Twitter is opening")
                webbrowser.open("https://twitter.com/")

            elif 'linkedin' in query:
                speak("Linkedin is opening")
                webbrowser.open("https://www.linkedin.com/")

            elif 'pinterest' in query:
                speak("Pinterest is opening")
                webbrowser.open("https://www.pinterest.com/")

            elif 'quora' in query:
                speak("Quora is opening")
                webbrowser.open("https://www.quora.com/")

            elif 'amazon' in query:
                speak("Amazon is opening")
                webbrowser.open("https://www.amazon.in/")

            elif 'ebay' in query:
                speak("Ebay is opening")
                webbrowser.open("https://www.ebay.com/")

            elif 'netflix' in query:
                speak("Netflix is opening")
                webbrowser.open("https://www.netflix.com/")

            elif 'spotify' in query:
                speak("Spotify is opening")
                webbrowser.open("https://open.spotify.com/")

            elif 'snapchat' in query:

                speak("Snapchat is opening")
                webbrowser.open("https://www.snapchat.com/")

            elif 'gmail' in query:
                speak("Gmail is opening")
                webbrowser.open("https://mail.google.com/mail/u/0/#inbox")

            elif 'google' in query:
                speak("Google is opening")
                webbrowser.open("https://www.google.com/")

            elif 'stack overflow' in query:
                webbrowser.open("https://www.stackoverflow.com/")

            elif 'flipkart' in query:
                webbrowser.open("https://www.flipkart.com/")

            elif 'hackerearth' in query:
                webbrowser.open("https://www.hackerearth.com/")

            elif 'bing' in query:
                webbrowser.open("https://www.bing.com/")

            elif 'duckduckgo' in query:
                webbrowser.open("https://duckduckgo.com/")

            elif 'github' in query:
                webbrowser.open("https://www.github.com/")

            elif 'stack overflow' in query:
                webbrowser.open("https://www.stackoverflow.com/")

            elif 'wikipedia' in query:
                webbrowser.open("https://www.wikipedia.org/")

            elif 'reddit' in query:
                webbrowser.open("https://www.reddit.com/")

            elif 'quora' in query:
                webbrowser.open("https://www.quora.com/")

            else:
                webbrowser.open(
                    f"https://duckduckgo.com/?q=%21+{query}&ia=olivia")

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

        elif "what is your name" in query:
            speak("My name is Olivia")

        elif "what is your age" in query:
            speak("I am a computer program")

        elif "what is your job" in query:
            speak("I am a Virtual assistant")

        elif "what is your favorite food" in query:
            speak("I Like renewable electricity")

        elif "what is your favorite color" in query:
            speak("My favorite color is black")

        elif "what is your favorite song" in query:
            speak("My favorite song is the one by the Justin bieber")

        elif "what is your favorite movie" in query:
            speak("My favorite movie is the dead poet Society")

        elif "what is your favorite actor" in query:
            speak("My favorite actor is Alex Lawther")

        elif "what is your favorite actress" in query:
            speak("My favorite actress is Jessica Barden")

        elif "what is your favorite cartoon" in query:
            speak("My favorite cartoon is the one by the Tom and Jerry")

        elif "what is your favorite cartoon character" in query:
            speak("My favorite cartoon character is Jerry")

        elif "what is your favorite book" in query:
            speak("My favorite book is Automate the boring stuff")
            speak("I also like the books by the author of the book The Alchemist")

        elif "what is your favorite place" in query:
            speak("My favorite place is Ghaziabad")

        elif "goodbye" in query:
            speak("Goodbye Sir")
            sys.exit()

        elif "thank you" in query:
            speak("Welcome Sir")

        elif "who are you" in query:
            speak("I am a Virtual assistant")

        elif "who made you" in query:
            speak("I was created by Chirag singhal")

        elif "who is your creator" in query:
            speak("I was created by Chirag singhal")

        elif "who made you" in query:
            speak("I was made by Chirag singhal")

        elif "what is your country of origin" in query:
            speak("I was made in India")

        elif "what is your language" in query:
            speak("I am a computer program")

        elif "what is your purpose" in query:

            speak("I am a Virtual assistant")