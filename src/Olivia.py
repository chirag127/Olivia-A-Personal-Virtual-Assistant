import ctypes
import datetime
import json
import math
import os
import platform
import random
import re
import shutil
import smtplib  # The smtplib is used for sending emails
import subprocess
import sys  # The sys library is used to exit the program
import time
import tkinter as tk  # The tkinter is used for gui
import webbrowser
from time import sleep
from tkinter import *

import numpy as np
import psutil
import pyautogui
import pyfiglet
import pyperclip
import pyttsx3
import pywhatkit
import requests
import speech_recognition as sr
import wikipedia  # The get article from wikipedia
import winshell  # The use winshell for opening the specified file
from googletrans import Translator
from pyowm import OWM

import playwl
from functions import *
from jokes import neutral_joke

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# create a wonderful virtual voice assistant named olivia and she will help you in your daily life with her amazing features like text to speech, voice to text, google search, wikipedia search, youtube search, news search, weather search, time search, date search, screenshot, email, jokes, ip address, and many more.
# olivia is a virtual voice assistant and she will help you in your daily life with her amazing features like text to speech, voice to text, google search, wikipedia search, youtube search, news search, weather search, time search, date search, screenshot, email, jokes, ip address, and many more.
# Olivia is created by chirag singhal.
# chirag singhal is a software engineer and she is a virtual voice assistant.
# chirag singhal made this virtual voice assistant for his mini-project in his college.


# reqiured engine for text to speech

engine = pyttsx3.init('sapi5')

# sapi5 is the default voice engine of windows and it is installed by default in windows

# getproperties is used to get the properties of the engine like rate, volume, pitch, etc.

voices = engine.getProperty('voices')


# setproperties is used to set the properties of the engine like rate, volume, pitch, etc.


engine.setProperty('voice', voices[1].id)

# defining the function to speak the text


def speak(audio):

    engine.say(audio)

    engine.runAndWait()


# defining the function to take command from the user

def takeCommand():

    # create a recognizer object

    r = sr.Recognizer()

    # use the microphone as source for input

    with sr.Microphone() as source:

        # print listening to the user to know that the program is listening

        print("Listening...")

        # refer to the https://www.codesofinterest.com/2017/04/energy-threshold-calibration-in-speech-recognition.html to understand the energy threshold

        # pause for a second to let the recognizer adjust the threshold before listening for input

        r.pause_threshold = 1

        # r.adjust_for_ambient_noise(source, duration=1)

        # r.dynamic_energy_threshold = True

        # r.energy_threshold = 800

        # r.dynamic_energy_adjustment_damping = 0.2

        # listen for the user's input and store it in audio variable and convert it to text later

        audio = r.listen(source)

    try:

        # convert the audio to text

        # print recongzing the user's voice to know that the program is re cognizing the user's voice

        print("Recognizing...")

        # use google translate to detect the language of the user's voice

        query = r.recognize_google(audio, language='en-in')

        # print the user's voice to the console

        print(f"User said: {query}\n")

    # if the user does not say anything then the program will listen again
    except sr.UnknownValueError as e:

        print("I could not understand what you said", e)
        print("Say that again please...")
        return "None"

    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))
        print("Please Check your internet connection")
        return "None"

    except sr.WaitTimeoutError:

        # print wait timeout error to know that the program is waiting for the user to speak

        print("Wait timeout exceeded")

        # Ask user to check his internet connection

        print("Please Check your internet connection")

        # print try after soem time to know that the program is trying to listen again

        print("Try after sometime")

        return "None"

    except Exception as e:

        # print the error to the console

        print("Say that again please...")

        # return the function to takeCommand()

        return "None"

    # return the function to takeCommand()

    return query


def sp(text):
    print(text)
    speak(text)


def NewsFromBBC():
    query_params = {
        "source": "bbc-news",
        "sortBy": "top",
        "apiKey": "4dbc17e007ab436fb66416009dfb59a8"
    }
    main_url = " https://newsapi.org/v1/articles"

    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()

    article = open_bbc_page["articles"]
    results = []

    for ar in article:
        results.append(ar["title"])

    for i in range(len(results)):

        print(i + 1, results[i])
        speak(results[i])


def text2speech():
    text = pyperclip.paste()

    print(text)
    speak(text)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        return "Good Morning"
        # if time is between 0 and 12 then say good morning

    elif hour >= 12 and hour < 18:  # if time is between 12 and 18 then say good afternoon
        return "Good Afternoon"

    else:  # if time is between 18 and 24 then say good evening

        return "Good Evening"


def pick_card():
    cards = ["Diamonds", "Spades", "Hearts", "Clubs"]

    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10,
             "Jack", "Queen", "King", "Ace"]

    def pick_a_card():

        card = random.choices(cards)

        rank = random.choices(ranks)

        return(f"The {rank} of {card}")

    sp(pick_a_card())


def tictactoe():
    size_of_board = 600
    symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
    symbol_thickness = 50
    symbol_X_color = '#EE4035'
    symbol_O_color = '#0492CF'
    Green_color = '#7BC043'

    class Tic_Tac_Toe():
        # ------------------------------------------------------------------
        # Initialization Functions:
        # ------------------------------------------------------------------
        def __init__(self):
            self.window = Tk()

            self.window.title('Tic-Tac-Toe')
            self.canvas = Canvas(
                self.window, width=size_of_board, height=size_of_board)
            self.canvas.pack()

            # Input from user in form of clicks
            self.window.bind('<Button-1>', self.click)

            self.initialize_board()

            self.player_X_turns = True
            self.board_status = np.zeros(shape=(3, 3))

            self.player_X_starts = True
            self.reset_board = False
            self.gameover = False
            self.tie = False
            self.X_wins = False
            self.O_wins = False

            self.X_score = 0
            self.O_score = 0
            self.tie_score = 0

        def mainloop(self):
            self.window.mainloop()

        def initialize_board(self):
            for i in range(2):
                self.canvas.create_line(
                    (i + 1) * size_of_board / 3, 0, (i + 1) * size_of_board / 3, size_of_board)

            for i in range(2):
                self.canvas.create_line(
                    0, (i + 1) * size_of_board / 3, size_of_board, (i + 1) * size_of_board / 3)

        def play_again(self):
            self.initialize_board()

            self.player_X_starts = not self.player_X_starts
            self.player_X_turns = self.player_X_starts
            self.board_status = np.zeros(shape=(3, 3))

        # ------------------------------------------------------------------
        # Drawing Functions:
        # The modules required to draw required game based object on canvas
        # ------------------------------------------------------------------

        def draw_O(self, logical_position):
            logical_position = np.array(logical_position)
            # logical_position = grid value on the board
            # grid_position = actual pixel values of the center of the grid
            grid_position = self.convert_logical_to_grid_position(
                logical_position)
            self.canvas.create_oval(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                    outline=symbol_O_color)

        def draw_X(self, logical_position):
            grid_position = self.convert_logical_to_grid_position(
                logical_position)
            self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] - symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] + symbol_size, width=symbol_thickness,
                                    fill=symbol_X_color)
            self.canvas.create_line(grid_position[0] - symbol_size, grid_position[1] + symbol_size,
                                    grid_position[0] + symbol_size, grid_position[1] - symbol_size, width=symbol_thickness,
                                    fill=symbol_X_color)

        def display_gameover(self):

            if self.X_wins:
                self.X_score += 1
                text = 'Winner: Player 1 (X)'
                color = symbol_X_color
            elif self.O_wins:
                self.O_score += 1
                text = 'Winner: Player 2 (O)'
                color = symbol_O_color
            else:
                self.tie_score += 1
                text = 'Its a tie'
                color = 'gray'

            self.canvas.delete("all")
            self.canvas.create_text(
                size_of_board / 2, size_of_board / 3, font="cmr 60 bold", fill=color, text=text)

            score_text = 'Scores \n'
            self.canvas.create_text(size_of_board / 2, 5 * size_of_board / 8, font="cmr 40 bold", fill=Green_color,
                                    text=score_text)

            score_text = 'Player 1 (X) : ' + str(self.X_score) + '\n'
            score_text += 'Player 2 (O): ' + str(self.O_score) + '\n'
            score_text += 'Tie                    : ' + str(self.tie_score)
            self.canvas.create_text(size_of_board / 2, 3 * size_of_board / 4, font="cmr 30 bold", fill=Green_color,
                                    text=score_text)
            self.reset_board = True

            score_text = 'Click to play again \n'
            self.canvas.create_text(size_of_board / 2, 15 * size_of_board / 16, font="cmr 20 bold", fill="gray",
                                    text=score_text)

        # ------------------------------------------------------------------
        # Logical Functions:
        # The modules required to carry out game logic
        # ------------------------------------------------------------------

        def convert_logical_to_grid_position(self, logical_position):
            logical_position = np.array(logical_position, dtype=int)
            return (size_of_board / 3) * logical_position + size_of_board / 6

        def convert_grid_to_logical_position(self, grid_position):
            grid_position = np.array(grid_position)
            return np.array(grid_position // (size_of_board / 3), dtype=int)

        def is_grid_occupied(self, logical_position):
            if self.board_status[logical_position[0]][logical_position[1]] == 0:
                return False
            else:
                return True

        def is_winner(self, player):

            player = -1 if player == 'X' else 1

            # Three in a row
            for i in range(3):
                if self.board_status[i][0] == self.board_status[i][1] == self.board_status[i][2] == player:
                    return True
                if self.board_status[0][i] == self.board_status[1][i] == self.board_status[2][i] == player:
                    return True

            # Diagonals
            if self.board_status[0][0] == self.board_status[1][1] == self.board_status[2][2] == player:
                return True

            if self.board_status[0][2] == self.board_status[1][1] == self.board_status[2][0] == player:
                return True

            return False

        def is_tie(self):

            r, c = np.where(self.board_status == 0)
            tie = False
            if len(r) == 0:
                tie = True

            return tie

        def is_gameover(self):
            # Either someone wins or all grid occupied
            self.X_wins = self.is_winner('X')
            if not self.X_wins:
                self.O_wins = self.is_winner('O')

            if not self.O_wins:
                self.tie = self.is_tie()

            gameover = self.X_wins or self.O_wins or self.tie

            if self.X_wins:
                print('X wins')
            if self.O_wins:
                print('O wins')
            if self.tie:
                print('Its a tie')

            return gameover

        def click(self, event):
            grid_position = [event.x, event.y]
            logical_position = self.convert_grid_to_logical_position(
                grid_position)

            if not self.reset_board:
                if self.player_X_turns:
                    if not self.is_grid_occupied(logical_position):
                        self.draw_X(logical_position)
                        self.board_status[logical_position[0]
                                          ][logical_position[1]] = -1
                        self.player_X_turns = not self.player_X_turns
                else:
                    if not self.is_grid_occupied(logical_position):
                        self.draw_O(logical_position)
                        self.board_status[logical_position[0]
                                          ][logical_position[1]] = 1
                        self.player_X_turns = not self.player_X_turns

                # Check if game is concluded
                if self.is_gameover():
                    self.display_gameover()

                    # print('Done')
            else:  # Play Again
                self.canvas.delete("all")
                self.play_again()

                self.reset_board = False

    game_instance = Tic_Tac_Toe()

    game_instance.mainloop()


def cpu():
    usage = psutil.cpu_percent()

    print("CPU is at")
    print(usage)
    speak("CPU is at")
    speak(usage)
    sp("pencentage")


def ram():
    usage = psutil.virtual_memory()

    print("RAM is at")
    print(usage)
    speak("RAM is at")
    speak(usage)


def disk():
    usage = psutil.disk_usage('/')
    sp("Disk is at")
    sp(usage)


def battery():

    sp("Battery is at")
    sp(psutil.sensors_battery())


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


def generate_random_password():
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    special = "@#$%&*"

    # pass_len=random.randint(8,13)  #without User INput

    pass_len = random.randint(8, 13)

    # length of password by 50-30-20 formula
    alpha_len = pass_len//2
    num_len = math.ceil(pass_len*30/100)
    special_len = pass_len-(alpha_len+num_len)

    password = []

    def generate_pass(length, array, is_alpha=False):
        for i in range(length):
            index = random.randint(0, len(array) - 1)
            character = array[index]
            if is_alpha:
                case = random.randint(0, 1)
                if case == 1:
                    character = character.upper()

            password.append(character)

    # alpha password
    generate_pass(alpha_len, alpha, True)
    # numeric password
    generate_pass(num_len, num)
    # special Character password
    generate_pass(special_len, special)
    # suffle the generated password list
    random.shuffle(password)
    # convert List To string
    gen_password = ""
    for i in password:
        gen_password = gen_password + str(i)
    sp(gen_password)


def takescreenshot():

    name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    # take the screenshot and save it to the C:\\Programfiles\\Olivia\\screenshot folder
    dir = "C:\\Olivia\\screenshot\\"
    name = dir + name + ".png"
    # create the folder named C:\\Screenshots if it doesn't already exist
    if not os.path.exists(dir):
        os.makedirs(dir)
    # save screenshot to file in image forma
    img = pyautogui.screenshot(name)
    img.show()

    print('Screenshot taken')

    # make a gui using tkinter library to display the screenshot and take a screenshot of a specific area
    root = tk.Tk()

    root.title('Screenshot')

    frame = tk.Frame(root, bg='#80c1ff')
    frame.place(relwidth=1, relheight=1)
    frame.pack()

    button = tk.Button(frame, text='Take Screenshot', command=takescreenshot)
    button.pack(side=tk.LEFT)

    close = tk.Button(frame, text='Quit', command=quit)
    close.pack(side=tk.LEFT)

    root.mainloop()


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()

    server.starttls()

    server.login('chriagsinghal@gmail.com', 'my password')
    server.sendmail('chiragsinghal@gmail.com', to, content)
    server.close()


def query_day():
    day = datetime.datetime.today()

    # print the day of the week
    weekday = day.weekday()

    # print = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}
    Mapping = {0: "Monday", 1: "Tuesday", 2: "Wednesday",
               3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"}

    try:
        speak("Today is " + Mapping[weekday])
    except:
        pass


def send_whatapp(to, content):
    webbrowser.open('https://web.whatsapp.com/send?phone=' +
                    to + '&text=' + content)
    import time
    sleep(30)
    pyautogui.press('enter')


def text2speech():
    text = pyperclip.paste()

    print(text)
    speak(text)


def exitcode():
    sys.exit()


def clearConsole():
    command = 'clear'
    speak("Clearing the console")
    os.system('cls')


# KEYBOARD_KEYS is attribute of pyautogui
# KEYBOARD_KEYS is a list of all the keys on the keyboard
# The full list of key names is in pyautogui.KEYBOARD_KEYS

# The following are the valid strings to pass to the press(), keyDown(), keyUp(), and hotkey() functions:


# ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
# ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
# '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
# 'a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
# 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
# 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
# 'browserback', 'browserfavorites', 'browserforward', 'browserhome',
# 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
# 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
# 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
# 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
# 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
# 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
# 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
# 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
# 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
# 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
# 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
# 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
# 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
# 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
# 'command', 'option', 'optionleft', 'optionright']

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


# asdfjkl;


if __name__ == "__main__":

    columns_shutil = shutil.get_terminal_size().columns

    result = pyfiglet.figlet_format("WELCOME TO OLIVIA", font="banner3-D")

    print(result.center(columns_shutil))

    sp(wishMe())

    running = True

    while running:

        # take command from user and convert it to lower case and assign it to a variable named as query

        query = takeCommand().lower()

        if 'desktop' in query or 'computer' in query or 'system' in query:

            # shutdown the computer if the query contains 'shutdown'
            if 'shutdown' in query:
                speak("Hold On ! Your system is on its way to shut down")
                os.system('shutdown /s /f')
                running = False
                sys.exit()

            # restart the computer if the query contains 'restart'
            elif 'restart' in query:
                speak("Hold On ! Your system is on its way to restart")
                os.system('shutdown /r ')
                running = False
                sys.exit()

            # logout the user if the query contains 'logout'
            elif 'logout' in query:
                speak("Hold On ! Your system is on its way to logout")
                os.system('shutdown /l')
                running = False
                sys.exit()

            # hibernate the computer if the query contains 'hibernate'
            elif 'hibernate' in query:
                speak("Hold On ! Your system is on its way to hibernate")
                os.system('shutdown /h')
                running = False
                sys.exit()

            # lock the computer if the query contains 'lock'
            elif 'lock' in query:

                speak("Hold On ! Your system is on its way to lock")

                os.system('rundll32.exe user32.dll,LockWorkStation')

                running = False

                sys.exit()

            elif "what is my operating system" in query:

                speak("Your operating system is windows")

        # give the current date and time if 'date' is in query
        if 'date' in query and "current" in query:
            now = datetime.datetime.now()

            sp("The current date is")
            sp(now.strftime("%d-%m-%Y"))

        if 'fullform of abcdef' in query:
            sp("Any body can dance")

        # elif 'current weather' in query:
        #     reg_ex = re.search('current weather in (.*)', query)
        #     if reg_ex:
        #         city = reg_ex.group(1)
        #         owm = OWM(API_key='ab0d5e80e8dafb2cb81fa9e82431c1fa')
        #         obs = owm.weather_at_place(city)
        #         w = obs.get_weather()

        #         k = w.get_status()

        #         x = w.get_temperature(unit='celsius')
        #         speak('Current weather in %s is %s. The maximum temperature is %0.2f and the minimum temperature is %0.2f degree celcius' % (
        #             city, k, x['temp_max'], x['temp_min']))

        elif 'random' in query and 'advice' in query:

            # remove the stop words from the query
            query = query.replace("random", "")
            query = query.replace("advice", "")
            query = query.strip()
            url = 'https://api.adviceslip.com/advice'

            # example response
            # {"slip": { "id": 112, "advice": "It's not about who likes you, it's about who you like."}}

            response = requests.get(url)

            # print(response.text)

            # convert the response to json format

            data = response.json()

            # print(data)

            # get the advice from the json data

            advice = data['slip']['advice']

            # speaking and printing the advice
            #
            sp(advice)

        elif 'random' in query and 'dog' in query and 'fact' in query:

            # remove the stop words from the query
            query = query.replace("random", "")
            query = query.replace("dog", "")
            query = query.replace("fact", "")
            query = query.strip()

            # the url for random dog facts for the api
            url = "https://dog-api.kinduff.com/api/facts"

            # sample response
            # {"facts":["The Norwegian Lundehund is the only dog with six toes on each foot."],"success":true}

            # get the response from the api
            response = requests.get(url)

            # convert the response to json format
            data = response.json()

            # get the fact from the json data
            fact = data['facts'][0]

            # speaking and printing the fact.
            sp(fact)

        elif 'random' in query and 'useless' in query and 'fact' in query:

            # remove the stop words from the query
            query = query.replace("random", "")
            query = query.replace("useless", "")
            query = query.replace("fact", "")
            query = query.strip()

            # the url for random dog facts for the api
            url = "https://uselessfacts.jsph.pl/random.json?language=en"

            # sample response
            # {"facts":["The Norwegian Lundehund is the only dog with six toes on each foot."],"success":true}

            # get the response from the api
            response = requests.get(url)

            # convert the response to json format
            data = response.json()

            # get the fact from the json data
            fact = data['text']

            # speaking and printing the fact.

            sp(fact)

            # print here is what i found on the console.

            print("here what i found")

        elif 'game' in query and 'start' in query:

            if 'tic' in query or 'tac' in query or 'toe' in query:

                tictactoe()

            elif 'guess' in query:
                pass

            elif 'pick' in query and 'card' in query:

                pick_card()

        # telling the joke when the query of the user contains joke
        elif 'joke' in query:
            givejoke()

        elif "send" in query and 'message' in query:
            username = {
                'abigail': '+91 7428449707',
                'alex': '+91 7428449707',
                'amelia': '+91 7428449707',
                'ava': '+91 7428449707',
                'chirag': '+91 7428449707',
                'chloe': '+91 7428449707',
                'ella': '+91 7428449707',
                'emily': '+91 7428449707',
                'emma': '+91 7428449707',
                'hanna': '+91 7428449707',
                'hannah': '+91 7428449707',
                'isabella': '+91 7428449707',
                'layla': '+91 7428449707',
                'layla': '+91 7428449707',
                'lena': '+91 7428449707',
                'lily': '+91 7428449707',
                'mahesh': '+91 7428449707',
                'manish': '+91 7428449707',
                'mia': '+91 7428449707',
                'none': '+91 7428449707',
                'samantha': '+91 7428449707',
                'shiv': '+91 7428449707',
                'shivam': '+91 7428449707',
                'shubham': '+91 7428449707',
                'sophia': '+91 7428449707',
                'zoe': '+91 7428449707',
                'zoya': '+91 7428449707'

            }
            try:
                speak("to whom should i send to?")
                name = takeCommand().lower()

                to = username[name]
                speak("What should i say?")
                content = takeCommand()

                send_whatapp(to, content)
                speak("Message has been sent")
                break

            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this message")

        # telling the cpu usage when the says a command that contains both cpu and usage.
        elif 'usage' in query and 'cpu' in query:

            speak("CPU is at " + str(psutil.cpu_percent()) + "%")

            print("CPU is at " + str(psutil.cpu_percent()) + "%")

        # telling the ram usage when the says a command that contains both ram and usage.
        elif 'usage' in query and 'ram' in query:

            speak("RAM is at " + str(psutil.virtual_memory()[2]) + "%")

        # telling the disk usage when the says a command that contains both ram and usage to the console.

            print("RAM is at " + str(psutil.virtual_memory()[2]) + "%")

        # telling the disk usage when the says a command that contains both disk and usage.

        elif 'usage' in query and 'disk' in query:

            speak("Disk is at " + str(psutil.disk_usage('/')[3]) + "%")

            # telling the battery usage when the says a command that contains both battery and usage.

            print("Disk is at " + str(psutil.disk_usage('/')[3]) + "%")

        # telling the battery usage when the says a command that contains both battery and usage.

        elif 'usage' in query and 'battery' in query:

            speak("Battery is at " + str(psutil.sensors_battery().percent) + "%")

            # printing the battery usage in the console

            print("Battery is at " + str(psutil.sensors_battery().percent) + "%")

        # telling the battery status when the says a command that contains both battery and status.

        elif 'status' in query and 'battery' in query:

            if psutil.sensors_battery().power_plugged == True:

                speak("Battery is charging")

            if psutil.sensors_battery().power_plugged == False:

                speak("Battery is discharging")

        elif 'open word' in query:

            speak('ok. opening word')

            os.startfile(
                'C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE')

            speak('do you want me to type ?')

            typin = takeCommand().lower()

            if 'yes' in typin:

                pyautogui.press('enter')

                speak('you can start. say stop typing if I have to stop')

                while True:

                    type_sentence = takeCommand().lower()

                    if 'stop typing' in type_sentence:

                        break

                    elif 'enter' in type_sentence:

                        pyautogui.press('enter')

                    # press tab by pressing the tab key
                    # when the type sentence contains backspace and press
                    # backspace, the program will press backspace
                    elif 'backspace' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('backspace')

                    # press space by pressing the space key
                    # when the type sentence contains space and press
                    # space, the program will press space
                    elif 'space' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('space')

                    # press left arrow by pressing the left arrow key
                    # when the type sentence contains left arrow and press
                    # left arrow, the program will press left arrow
                    elif 'left arrow' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('left')

                    # press right arrow by pressing the right arrow key
                    # when the type sentence contains right arrow and press
                    # right arrow, the program will press right arrow
                    elif 'right arrow' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('right')

                    # press up arrow by pressing the up arrow key
                    # when the type sentence contains up arrow and press
                    # up arrow, the program will press up arrow
                    elif 'up arrow' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('up')

                    # press down arrow by pressing the down arrow key
                    # when the type sentence contains down arrow and press
                    # down arrow, the program will press down arrow
                    elif 'down arrow' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('down')

                    # press home by pressing the home key
                    # when the type sentence contains home and press
                    # home, the program will press home
                    elif 'home' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('home')

                    # press end by pressing the end key
                    # when the type sentence contains end and press
                    # end, the program will press end
                    elif 'end' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('end')

                    # press page up by pressing the page up key
                    # when the type sentence contains page up and press
                    # page up, the program will press page up
                    elif 'page up' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('pageup')

                    # press page down by pressing the page down key
                    # when the type sentence contains page down and press
                    # page down, the program will press page down
                    elif 'page down' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('pagedown')

                    # press insert by pressing the insert key
                    # when the type sentence contains insert and press
                    # insert, the program will press insert

                    elif 'insert' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('insert')

                    # press delete by pressing the delete key
                    # when the type sentence contains delete and press
                    # delete, the program will press delete
                    elif 'delete' in type_sentence and 'press' in type_sentence:

                        pyautogui.press('delete')

                    # automating the operation on the word file
                    # when the type sentence contains file
                    elif 'file' in type_sentence:
                        # save the file by pressing the hotkey ctrl+s
                        # save the file if the type sentence contains save
                        if 'save' in type_sentence:
                            pyautogui.hotkey('ctrl', 's')
                            sleep(1)
                            pyautogui.press('enter')
                            speak('file has been saved')

                        # close the file by pressing the hotkey alt+f4
                        # close the file if the type sentence contains close
                        elif 'close' in type_sentence:
                            pyautogui.hotkey('alt', 'f4')

                            pyautogui.press('enter')

                            speak('file has been closed')

                            break

                    else:
                        if query != 'none':

                            pyautogui.typewrite(type_sentence)

                speak('stopped typing')

            elif 'no' in typin:

                speak('ok sir')

        # type the text in the current window if 'type' is in query

        elif 'typing' in query and 'start' in query:

            speak("Starting typing")

            speak("What should i type sir")

            while True:

                type_sentence = takeCommand().lower()

                if query != 'none':

                    if 'stop typing' in type_sentence:

                        sp('stopped typing')

                        break
                    elif 'enter' in type_sentence:

                        pyautogui.press('enter')

                    elif 'backspace' in type_sentence:

                        pyautogui.hotkey('ctrl', 'backspace')

                    elif 'tab' in type_sentence:
                        pyautogui.press('tab')

                    elif 'space' in type_sentence:

                        pyautogui.press('space')

                    elif 'caps lock' in type_sentence:

                        pyautogui.press('caps lock')

                    else:

                        pyautogui.typewrite(type_sentence)

        elif 'stop typing' in query:

            speak('sir I already stopped typing')

        # if the query contains "write" and "note" in the query then write the note in the file named src/notes.txt and then tell the user that the note has been written
        # also ask if the user wants to include the date and time in the note
        elif 'write' in query and 'note' in query:

            speak("What should i write sir")

            note = takeCommand()

            file = open("src/notes.txt", "w")

            speak("Do you want to add the date and time in the note?")

            note_date = takeCommand()

            if 'yes' in note_date:

                file.write(str(datetime.datetime.now()) + " : " + note)

                speak("Note has been written")

            elif 'no' in note_date:

                file.write(note)

                speak("Note has been written")

            file.close()

        # if the query contains "read" and "note" in the query then read the note from the file named src/notes.txt and then tell the user that the note has been read
        elif 'read' in query and 'note' in query:
            file = open("src/notes.txt", "r")
            speak("Here is your note")
            print(file.read())
            speak(file.read())
            file.close()

        # if the query contains "open" and "note" in the query then open the note from the file named src/notes.txt and then tell the user that the note has been opened
        elif 'open' in query and 'note' in query:
            os.system("src/notes.txt")
            speak("Note has been opened")

        # if the query contains "delete" and "note" in the query then delete the note from the file named src/notes.txt
        # and then tell the user that the note has been deleted
        elif 'delete' in query and 'note' in query:
            os.remove("src/notes.txt")
            speak("Note has been deleted")

        # if the query contains "show" and "note" in the query then show the note from the file named src/notes.txt
        elif 'show' in query and 'note' in query:
            os.system("src/notes.txt")
            sp("Note has been shown")

        # play the video if the query contains "play".
        # the query should be like "play (topic of the video user want to play on youtube)"
        # then the video should be played on youtube
        # the user should be able to pause and resume the video by saying "pause" and "resume"
        # the user should be able to stop the video by saying "stop"
        # the user should be able to skip the video by saying "skip"
        # the user should be able to change the video by saying "change"
        # the user should be able to increase the volume by saying "increase volume" or "increase volume by (number)" or "volume up"
        # the user should be able to decrease the volume by saying "decrease volume" or "decrease volume by (number)" or "volume down"
        # the user should be able to mute the video by saying "mute"
        # the user should be able to unmute the video by saying "unmute"
        # the user should be able to increase the speed of the video by saying "increase speed" or "increase speed by (number)" or "speed up"
        # the user should be able to decrease the speed of the video by saying "decrease speed" or "decrease speed by (number)" or "speed down"
        # the user should be able to close the video by saying "close"
        # the user should be able to exit the video by saying "exit"
        # the user should be able to next the video by saying "next"
        # the user should be able to go back to the video by saying "back"
        # the user should be able to go to the video by saying "go to (number)"
        # the user should be able to go to the video by saying "go to (number)"
        # the user should be able to go to the next tab by saying "next tab"
        # the user should be able to go to the previous tab by saying "previous tab"

        elif 'play' in query:

            if 'watch' in query and 'later' in query:

                playwl.main()

            else:

                song_name = query.replace("play ", "")

                speak("Playing " + song_name)

                print(song_name)

                pywhatkit.playonyt(song_name)

                sleep(5)

            while True:

                query = takeCommand().lower()

                # pause the video if 'pause' is in query

                # trim the query

                query.strip()

                if query == 'bye' or query == 'goodbye' or query == 'bye bye':

                    sp("Bye Sir")

                    exit()

                elif 'pause' in query or 'pass' in query or 'stop' in query or 'resume' in query or 'continue' in query or 'play' in query:

                    pyautogui.press('space')

                # go to the next tab by pressing control + tab

                # if the query contains 'next tab' or 'next tab'

                # if the query contains not this then check next elif statement

                elif 'next' in query:

                    # go to next tab by pressing control + tab

                    if 'tab' in query:

                        pyautogui.hotkey('ctrl', 'tab')

                    # go to next frame by pressing .

                    elif 'frame' in query:

                        pyautogui.press('.')

                    else:

                        # go to next video by pressing shift + n

                        pyautogui.hotkey('shift', 'n')

                elif 'skip' in query and 'video' in query:

                    pyautogui.hotkey('shift', 'n')

                # go to the previous tab by pressing control + shift + tab

                # if the query contains 'previous tab' or 'previous tab'

                # if the query contains not this then check next elif statement

                elif 'previous' in query:

                    # if the query contains 'tab' then go to previous tab by pressing control + shift + tab

                    if 'tab' in query:

                        pyautogui.hotkey('ctrl', 'shift', 'tab')

                    # go to previous frame by pressing ,

                    elif 'frame' in query:

                        pyautogui.press(',')

                    else:

                        # go to previous video by pressing shift + p

                        pyautogui.hotkey('shift', 'p')

                # reload the video by pressing control + r if the

                # query contains 'reload' or 'refresh' or 'reload' or 'restart' or 'reboot'

                # if the query contains not this then check next elif statement

                elif 'reload' in query or 'refresh' in query or 'reload' in query or 'restart' in query or 'reboot' in query and 'tab' in query:

                    pyautogui.hotkey('ctrl', 'r')

                # mute the video by pressing control + m if the query contains 'mute' or 'unmute' or 'mute' or 'unmute'

                # if the query contains not this then check next elif statement

                elif 'mute' in query or 'unmute' in query:

                    pyautogui.hotkey('ctrl', 'm')

                # turn on subtitles if the query contains 'subtitles' or 'subtitle' or 'subtitles on' or 'subtitle on' or

                # 'captions' by pressing c

                elif 'subtitle' or 'caption' in query:

                    pyautogui.press('c')

                # enter the miniplayer by pressing i

                # if the query contains 'miniplayer' or 'mini player' or 'miniplayer on' or 'mini player on' or 'miniplayer off' or 'mini player off'

                elif 'mini' in query and 'player' in query:

                    pyautogui.press('i')

                # replay the video by pressing home button if the query contains 'replay' or 'replay' or 'replay' or 'replay' or 'replay' or 'replay'

                elif 'replay' in query:

                    pyautogui.press('home')

                # dislike the video by pressing d if the query contains 'dislike'

                elif 'dislike' in query:

                    pyautogui.hotkey('d')

                # like the video by pressing s if the query contains 'like'

                elif 'like' in query:

                    pyautogui.hotkey('s')

                # seek backward by pressing  left arrow if the query contains 'backward' or 'rewind'

                if 'backward' in query or 'rewind' in query:

                    pyautogui.hotkey('left')

                # seek forward by pressing right arrow if the query contains 'forward' or 'fast forward'

                elif 'forward' in query:

                    pyautogui.hotkey('right')

                # move to full screen mode by pressing f

                # if the query contains 'full screen' or 'full mode' or 'full screen mode'

                # if the query contains not this then check next elif statement

                elif 'full' in query and 'screen' in query or 'mode' in query:

                    pyautogui.press('f')

                # go to download page

                # if the query contains 'download' or 'downloads' or 'download page' or 'downloads page'

                # if the query contains not this then check next elif statement

                elif 'download' in query or 'downloads' in query or 'download page' in query or 'downloads page' in query:

                    pyautogui.hotkey('ctrl', 'j')

                # go to the history page by pressing control + h

                # if the query contains 'history' and 'page'

                # if the query contains not this then check next elif statement

                elif 'history' in query and 'page' in query:

                    pyautogui.hotkey('ctrl', 'h')

                # go to the bookmark page by pressing control + shift + o

                # if the query contains 'bookmark' and 'page'

                # if the query contains not this then check next elif statement

                elif 'bookmark manager' in query or 'bookmark page' in query:

                    pyautogui.hotkey('ctrl', 'shift', 'o')

                # show the bookmark mark bar by pressing control + shift + b

                # if the query contains 'bookmark bar' or 'bookmark bar'

                # if the query contains not this then check next elif statement

                elif 'bookmark bar' in query:

                    pyautogui.hotkey('ctrl', 'shift', 'b')

                # increase the volume by pressing up arrow

                # if the query contains 'increase volume' or 'volume up' or 'louder'

                # if the query contains not this then check next elif statement

                elif 'increase volume' in query or 'volume up' in query or 'louder' in query:

                    query = query.replace("increase volume by", "")
                    query = query.replace("volume up by", "")
                    query = query.replace("louder", "")

                    if 'percent' in query or 'percentage' in query or '%' in query:
                        query = query.replace("percent", "")
                        query = query.replace("percentage", "")
                        query = query.replace("%", "")

                        # volume is increased by the number of percentage mentioned in the query
                        # volume is increased by 5 percentage by one up press
                        # volume is increased by 10 percentage by two up presses
                        # volume is increased by 15 percentage by three up presses
                        # volume is increased by 20 percentage by four up presses
                        # volume is increased by 25 percentage by five up presses

                        query = query.replace(" ", "")
                        percent = int(query)

                        no_of_up_presses = int(percent / 5)
                        for i in range(no_of_up_presses):
                            pyautogui.press('up')
                            sleep(0.5)

                        if percent > 100:
                            sp("I can only increase the volume to 100%")
                        else:
                            pass

                    else:
                        # volume is increased by 5 percentage by one up press
                        pyautogui.press('up')

                # decrease the volume by pressing down arrow

                # if the query contains 'decrease volume' or 'volume down' or 'quieter'

                # if the query contains not this then check next elif statement

                elif 'decrease volume' in query or 'volume down' in query or 'quieter' in query:

                    query = query.replace("decrease volume by", "")
                    query = query.replace("volume down by", "")
                    query = query.replace("quieter", "")

                    if 'percent' in query or 'percentage' in query or '%' in query:
                        query = query.replace("percent", "")
                        query = query.replace("percentage", "")
                        query = query.replace("%", "")

                        # volume is decreased by the number of percentage mentioned in the query
                        # volume is decreased by 5 percentage by one down press

                        query = query.replace(" ", "")
                        percent = int(query)
                        no_of_down_presses = int(percent / 5)
                        for i in range(no_of_down_presses):
                            pyautogui.press('down')
                            sleep(0.5)

                    else:
                        # volume is decreased by 5 percentage by one down press
                        pyautogui.press('down')

                    # increase the speed of the video by pressing shift + . arrow

                    # if the query contains 'increase speed' or 'speed up' or 'faster'

                    # if the query contains not this then check next elif statement

                elif 'increase speed' in query or 'speed up' in query or 'faster' in query:

                    query = query.replace("increase speed by", "")
                    query = query.replace("speed up by", "")
                    query = query.replace("faster", "")

                    if 'percent' in query or 'percentage' in query or '%' in query:
                        query = query.replace("percent", "")
                        query = query.replace("percentage", "")
                        query = query.replace("%", "")

                        # speed is increased by the number of percentage mentioned in the query
                        # speed is increased by 5 percentage by one shift + . press
                        # speed is increased by 10 percentage by two shift + . press
                        # speed is increased by 15 percentage by three shift + . press
                        # speed is increased by 20 percentage by four shift + . press
                        # speed is increased by 25 percentage by five shift + . press

                        query = query.replace(" ", "")
                        percent = int(query)

                        no_of_shift_dot_presses = int(percent / 25)
                        for i in range(no_of_shift_dot_presses):
                            pyautogui.hotkey('>')
                            sleep(0.5)

                    else:

                        # speed is increased by 25 percentage by one shift + . press
                        pyautogui.hotkey('>')

                # decrease the speed of the video by pressing shift + , arrow

                # if the query contains 'decrease speed' or 'speed down' or 'slower'

                # if the query contains not this then check next elif statement

                elif 'decrease speed' in query or 'speed down' in query or 'slower' in query:

                    query = query.replace("decrease speed by", "")
                    query = query.replace("speed down by", "")
                    query = query.replace("slower", "")

                    if 'percent' in query or 'percentage' in query or '%' in query:
                        query = query.replace("percent", "")
                        query = query.replace("percentage", "")
                        query = query.replace("%", "")

                        # speed is decreased by the number of percentage mentioned in the query
                        # speed is decreased by 5 percentage by one shift + , press
                        # speed is decreased by 10 percentage by two shift + , press
                        # speed is decreased by 15 percentage by three shift + , press
                        # speed is decreased by 20 percentage by four shift + , press
                        # speed is decreased by 25 percentage by five shift + , press

                        query = query.replace(" ", "")
                        percent = int(query)

                        no_of_shift_dot_presses = int(percent / 25)
                        for i in range(no_of_shift_dot_presses):
                            pyautogui.hotkey('<')
                            sleep(0.5)

                    pyautogui.hotkey('<')

                # exit the video by pressing alt + f4

                # if the query contains 'exit' or 'quit'

                # if the query contains not this then check next elif statement

                elif 'exit' in query or 'quit' in query:

                    pyautogui.hotkey('alt', 'f4')

                    break

                # if the query contains 50% percent or 50 percent or 50% or 50 then change go to the video length to 50 percent

                # if query contains 10 percent or 10% or 10 then change go to the video length to 10 percent by pressing number pad1

                elif '10%' in query:

                    pyautogui.press('1')

                elif '20%' in query:

                    pyautogui.press('2')

                elif '30%' in query:

                    pyautogui.press('3')

                elif '40%' in query:

                    pyautogui.press('4')

                elif '50%' in query:

                    pyautogui.press('5')

                elif '60%' in query:

                    pyautogui.press('6')

                elif '70%' in query:

                    pyautogui.press('7')

                elif '80%' in query:

                    pyautogui.press('8')

                elif '90%' in query:

                    pyautogui.press('9')

                elif '100%' in query:

                    pyautogui.press('0')

                # close the video by pressing control + w

                # if the query contains 'close'

                # if the query contains not this then check next elif statement

                elif 'close' in query:

                    pyautogui.hotkey('ctrl', 'w')

                    sp("I have closed the video")

                    break

                # close other tabs by pressing control + shift + t

        elif 'press' in query:
            reg_ex = re.search('press (.*)', query)
            if reg_ex:
                query = reg_ex.group(1)
                pyautogui.press(query)

        elif 'tab' in query:
            if 'next' in query:
                pyautogui.hotkey('ctrl', 'tab')
                # sp('Gone to the next tab')
            elif 'previous' in query:
                pyautogui.hotkey('shift', 't')

            elif 'quit' in query:
                pyautogui.hotkey('ctrl', 'w')
                # sp('Quited the tab')

            elif 'restart' in query or 'reload' in query or 'refresh' in query or 'reboot' in query:
                pyautogui.hotkey('ctrl', 'r')

            elif 'new' in query:
                pyautogui.hotkey('ctrl', 't')

            elif 'close' in query:
                pyautogui.hotkey('ctrl', 'w')

        # tell user the common usage of the command if 'usage' is in query

        elif 'where are you?' in query:
            speak("I am here in the main loop. sir")

        elif 'who are you?' in query:
            speak("I am your personal assistant. sir")

        elif 'who made you?' in query:
            speak("I was made by a programmer. sir")

        elif 'who is your creator?' in query:
            speak("I was made by a programmer namesd Chirag Singhal. sir")

        # search in chrome when the query is 'search'

        elif 'search in chrome' in query:
            speak("What should i search for sir")
            chromepath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            search = takeCommand().lower()

            webbrowser.get(chromepath).open(
                'https://www.google.com/search?q=' + search)

  # if 'time' is in query and "current" is in the query then tell the time in very good manner for example we can say the current time is 2 pm and 28 minutes sir
 # or the current time is 5 pm and 28 minutes sir . be polite.

        elif 'time' in query and 'current' in query:
            ctime()

        # Read the copied text from clipboard and speak it if 'read' is in query and 'aloud' is in query
        elif 'read aloud' in query:
            text2speech()

        # if 'open' is in query and 'notepad' is in query then open notepad
        elif 'open notepad' in query:

            os.system('notepad')

        elif 'screenshot' in query:
            takescreenshot()

        elif 'joke' in query:

            if 'nuetral' in query:

                sp(neutral_joke())

            else:

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

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop olivia from listening commands")
            sleep(120)
            speak("Olivia is listening again")

        elif 'recycle bin' in query:

            if 'clear' in query or 'empty' in query:

                speak("Emptying the recycle bin")

                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)

                speak("Recycle Bin Recycled")

        elif 'lock window' in query or 'lock screen' in query or 'lock the screen' in query:

            speak("locking the device")

            ctypes.windll.user32.LockWorkStation()

        elif 'remember that' in query:

            speak("What should i remember?")

            data = takeCommand()

            speak("You said me to remember that " + data)

            remember = open('src/notes.txt', 'w')

            remember.write(data)

            remember.close()

            speak("I have remembered that")

        elif 'do you know anything' in query:

            remember = open('src/notes.txt', 'r')

            speak("You said me to remember that " + remember.read())

            remember.close()

        elif 'roll' in query and 'dice' in query:

            r = random.randint(1, 6)

            dice = str(r)

            speak('you got ' + dice)

        elif query == 'quit' or 'olivia quit' in query or 'olivia bye' in query or query == 'bye' or query == 'exit' or query == 'goodbye' or query == 'bye bye':

            sp("Bye Sir")

            exit()

        # if the user wants to repeat the last command

        elif 'repeat' in query and 'olivia' in query:

            # telling the user that the program is repeating the last command

            speak("repeating the last command")

            # repeating the last command

            sp(query)

        # writing code to fetch the news from the "https://news.google.com/news/rss" using webscraping and reading that news using beautiful soup

        elif 'generate' in query:

            if 'password' in query:

                generate_random_password()

            elif 'number' in query:

                sp(random.randint(0, 100))

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand().lower()

                to = "chriagsinghal@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak(
                    "Sorry my friend chirag sir. I am not able to send this email")

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

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop olivia from listening commands")
            sleep(120)
            speak("Olivia is listening again")

        elif 'recycle bin' in query:

            if 'clear' in query or 'empty' in query:

                speak("Emptying the recycle bin")

                winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)

                speak("Recycle Bin Recycled")

        elif 'remember that' in query:

            while True:

                speak("What should i remember?")

                data = takeCommand()

                speak("You said me to remember that " + data)

                remember = open('data.txt', 'w')

                remember.write(data)

                remember.close()

                speak("I have remembered that")

        elif 'do you know anything' in query:

            remember = open('data.txt', 'r')

            speak("You said me to remember that " + remember.read())

            remember.close()

        elif "where is" in query:

            query = query.replace("where is", "")

            location = query

            sp("User asked to Locate")

            sp(location)

            webbrowser.open(
                "https://www.google.com / maps / place/" + location + "")


# tell the stock price of the company using yahoo finance api and speak the result to the user using google speech api and print the result to the console
#         elif "stock" in query and "price" in query:
#             speak("What company's stock price you want to check?")
#             company = takeCommand()

#             speak("Checking the stock price of " + company)
#             try:
#                 url = "https://in.finance.yahoo.com/quote/" + company + "?p=" + company
#                 page = requests.get(url)
#                 soup = BeautifulSoup(page.content, 'html.parser')
#                 price = soup.find(
#                     "div", {"class": "My(6px) Pos(r) smartphone_Mt(6px)"}).find("span").get_text()

#                 sp(price)
#                 print(price)
#             except Exception as e:
#                 print(e)
#                 speak("Sorry Sir, I am not able to fetch the stock price")


# # tell the weather of the city using openweathermap api and speak the result to the user using google speech api and print the result to the console
#         elif "weather" in query and "today" in query:
#             speak("What city's weather you want to check?")
#             city = takeCommand()

#             speak("Checking the weather of " + city)
#             try:
#                 url = "https://openweathermap.org/data/2.5/weather?q=" + \
#                     city + "&appid=b6907d289e10d714a6e88b30761fae22"
#                 page = requests.get(url)
#                 soup = BeautifulSoup(page.content, 'html.parser')
#                 weather = soup.find(
#                     "div", {"class": "weather-widget__container"}).find("p").get_text()

#                 sp(weather)
#                 print(weather)
#             except Exception as e:
#                 print(e)
#                 speak("Sorry Sir, I am not able to fetch the weather")

#         elif "date" in query and "curren" in query:

#             speak("Sir, What date you want to check")
#             date = takeCommand()

#             speak("Checking the date of " + date)
#             try:
#                 url = "https://www.timeanddate.com/worldclock/fixedtime.html?msg=" + date + "&iso=&p1=150"
#                 page = requests.get(url)
#                 soup = BeautifulSoup(page.content, 'html.parser')
#                 date = soup.find(
#                     "div", {"class": "time-date"}).find("p").get_text()

#                 sp(date)
#                 print(date)
#             except Exception as e:
#                 print(e)
#                 speak("Sorry Sir, I am not able to fetch the date")

#         elif "calculate" in query and "square" in query:

#             speak("Sir, What you want to calculate")
#             query = takeCommand()

#             speak("Calculating " + query)
#             try:
#                 url = "https://www.google.com/search?q=" + query
#                 page = requests.get(url)
#                 soup = BeautifulSoup(page.content, 'html.parser')
#                 result = soup.find(
#                     "div", {"class": "kno-ecr-pt"}).find("span").get_text()

#                 sp(result)
#                 print(result)
#             except Exception as e:
#                 print(e)
#                 speak("Sorry Sir, I am not able to fetch the result")

# # tell the user the current time using datetime module and speak the result to the user using google speech api and print the result to the console
#         elif "current time" in query:
#             speak("Sir, What time you want to check")
#             time = takeCommand()

#             speak("Checking the time of " + time)
#             try:
#                 url = "https://www.timeanddate.com/worldclock/fixedtime.html?msg=" + time + "&iso=&p1=150"
#                 page = requests.get(url)
#                 soup = BeautifulSoup(page.content, 'html.parser')
#                 time = soup.find(
#                     "div", {"class": "time-date"}).find("p").get_text()

#                 sp(time)
#                 print(time)
#             except Exception as e:
#                 print(e)
#                 speak("Sorry Sir, I am not able to fetch the time")

        elif 'launch' in query:
            query = query.replace("launch", "")
            sp("Launching ")
            sp(query)

            if 'control panel' in query:
                speak("okay")
                os.system("control")

            elif 'quick assist' in query:
                speak("okay")
                os.system("quickassist")

            elif 'game panel' in query:
                speak("okay")
                os.system("gamepanel")

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
                chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chromePath)

            elif 'notepad' in query:
                notepadPath = "C:\\Windows\\System32\\notepad.exe"
                os.startfile(notepadPath)

            elif 'calculator' in query:
                calculatorPath = "C:\\Windows\\System32\\calc.exe"
                os.startfile(calculatorPath)

            elif 'task manager' in query:
                taskManagerPath = "C:\\Windows\\System32\\taskmgr.exe"
                os.startfile(taskManagerPath)

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

            elif 'microsoft excel' in query:

                microsoftExcelPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE"
                os.startfile(microsoftExcelPath)

            elif 'microsoft powerpoint' in query:
                microsoftPowerpointPath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
                os.startfile(microsoftPowerpointPath)

            elif 'spotify' in query:
                spotifyPath = "C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe"
                os.startfile(spotifyPath)

            else:
                try:
                    reg_ex = re.search('launch (.*)', query)
                    if reg_ex:
                        appname = reg_ex.group(1)
                        appname1 = appname+".exe"
                        subprocess.Popen(
                            ["open", "-n", "/Applications/" + appname1], stdout=subprocess.PIPE)
                        sp('I have launched the desired application')
                except:
                    sp('I am not sure what application you want to launch')

        elif 'search' in query:

            sp("What do you want to search for?")

            query_to_be_searched = takeCommand().lower()

            # Ask the user on which site you want to search for the query

            sp("On which site do you want to search?")

            site_to_search = takeCommand().lower()

            # search on the google if google is in the resultant query after the execution of the above lines.

            if 'google' in site_to_search:

                # search on the google images if the site_to_search contains images

                if 'images' in site_to_search:

                    # Telling the user that the search is being executed on google images

                    sp("Searching on Google Images...")


                    # open the query_to_be_searched on the google images
                    webbrowser.open(
                        f"https://www.google.com/search?q={query_to_be_searched}&source=olivia&tbm=isch")

                # search on the google if the site_to_search  contains map
                elif 'maps' in site_to_search:

                    # Telling the user that the search is being executed on google maps

                    sp("Searching on Google Maps...")



                    # open the query_to_be_searched on the google maps
                    

                    webbrowser.open(
                        f"https://www.google.com/maps/search/{query_to_be_searched}")

                # search on google news if the site_to_search contains news

                elif 'news' in site_to_search:

                    # Telling the user that the search is being executed on google news

                    sp("Searching on Google News...")



                    # open the query_to_be_searched on the google news

                    webbrowser.open(
                        f"https://www.google.com/search?q={query_to_be_searched}&tbm=nws")

                elif 'books' in site_to_search:

                    # Telling the user that the search is being executed on google books

                    sp("Searching on Google Books...")



                    # open the query_to_be_searched on the google books

                    webbrowser.open(
                        f"https://www.google.com/search?q={query_to_be_searched}&tbm=bks")


                # search on google if the site_to_search contains videos

                elif 'videos' in site_to_search:


                    # Telling the user that the search is being executed on google videos

                    sp("Searching on Google Videos...")



                    # open the query_to_be_searched on the google videos

                    webbrowser.open(
                        f"https://www.google.com/search?q={query_to_be_searched}&tbm=vid")

                # search on google if the site_to_search contains shopping

                elif 'shopping' in site_to_search:

                    # open the query_to_be_searched on the google shopping

                    webbrowser.open(
                        f"https://www.google.com/search?q={query_to_be_searched}&tbm=shop")

                # search on google if the site_to_search contains flight

                elif 'flight' in site_to_search:

                    # open the query_to_be_searched on the google flight

                    webbrowser.open(
                        f"https://www.google.com/search?q={query_to_be_searched}&tbm=fl")

                # search on google if the site_to_search contains finance

                elif 'finance' in site_to_search:

                    # open the query_to_be_searched on the google finance

                    webbrowser.open(f"https://www.google.com/search?q={query_to_be_searched}&tbm=fin")


            # search on Youtube if the site_to_search contains youtube
            elif 'youtube' in site_to_search:

                # Telling the user that the search is being executed on youtube

                sp("Searching on Youtube...")



                # open the query_to_be_searched on the youtube

                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={query_to_be_searched}")

            # search on Amazon if the site_to_search contains amazon

            elif 'amazon' in site_to_search:

                # Telling the user that the search is being executed on amazon

                sp("Searching on Amazon...")


                # open the query_to_be_searched on the amazon

                webbrowser.open(
                    f"https://www.amazon.in/s?k={query_to_be_searched}")

            # search on Facebook if the site_to_search contains facebook

            elif 'facebook' in site_to_search:

                # Telling the user that the search is being executed on facebook

                sp("Searching on Facebook...")


                # open the query_to_be_searched on the facebook

                webbrowser.open(
                    f"https://www.facebook.com/search/top/?q={query_to_be_searched}")

            # search on Google.co.in if the site_to_search contains google.co.in

            elif 'google.co.in' in site_to_search:  

                # Telling the user that the search is being executed on google.co.in

                sp("Searching on Google.co.in...")


                # open the query_to_be_searched on the google.co.in

                webbrowser.open(
                    f"https://www.google.co.in/search?q={query_to_be_searched}")

            # search on Flipkart if the site_to_search contains flipkart

            elif 'flipkart' in site_to_search:  

                # Telling the user that the search is being executed on flipkart

                sp("Searching on Flipkart...")

                # open the query_to_be_searched on the flipkart

                webbrowser.open(
                    f"https://www.flipkart.com/search?q={query_to_be_searched}")

            # search on Wikipedia if the site_to_search contains wikipedia

            elif 'wikipedia' in site_to_search:

                # Telling the user that the search is being executed on wikipedia

                sp("Searching on Wikipedia...")



                # open the query_to_be_searched on the wikipedia

                webbrowser.open(
                    f"https://en.wikipedia.org/w/index.php?search={query_to_be_searched}")

            # search on Canva if the site_to_search contains canva

            elif 'canva' in site_to_search: 

                # Telling the user that the search is being executed on canva

                sp("Searching on Canva...")



                # open the query_to_be_searched on the canva

                webbrowser.open(
                    f"https://www.canva.com/search/templates?q={query_to_be_searched}")

            # search on Instagram if the site_to_search contains instagram

            elif 'instagram' in site_to_search: 

                # Telling the user that the search is being executed on instagram

                sp("Searching on Instagram...")



                # open the query_to_be_searched on the instagram

                webbrowser.open(
                    f"https://www.instagram.com/explore/tags/{query_to_be_searched}")

            # search on Microsoft if the site_to_search contains microsoft

            elif 'microsoft' in site_to_search: 

                # Telling the user that the search is being executed on microsoft

                sp("Searching on Microsoft...")


                # open the query_to_be_searched on the microsoft

                webbrowser.open(
                    f"https://www.microsoft.com/en-in/search/result.aspx?q={query_to_be_searched}")

            # search on Amazon.com if the site_to_search contains amazon.com

            elif 'amazon.com' in site_to_search:    

                # Telling the user that the search is being executed on amazon.com

                sp("Searching on Amazon.com...")


                # open the query_to_be_searched on the amazon

                webbrowser.open(
                    f"https://www.amazon.com/s?k={query_to_be_searched}")

            # search on Yahoo if the site_to_search contains yahoo

            elif 'yahoo' in site_to_search: 

                # Telling the user that the search is being executed on yahoo

                sp("Searching on Yahoo...")


                # open the query_to_be_searched on the yahoo

                webbrowser.open(
                    f"https://in.search.yahoo.com/search?p={query_to_be_searched}")

            # search on whatsapp if the site_to_search contains whatsapp

            elif 'whatsapp' in site_to_search:  

                # Telling the user that the search is being executed on whatsapp

                sp("Searching on Whatsapp...")


                # open the query_to_be_searched on the whatsapp

                webbrowser.open(
                    f"https://web.whatsapp.com/send?text={query_to_be_searched}")

            # search on Indiatimes if the site_to_search contains indiatimes

            elif 'indiatimes' in site_to_search:    

                # Telling the user that the search is being executed on indiatimes

                sp("Searching on Indiatimes...")


                # open the query_to_be_searched on the indiatimes

                webbrowser.open(
                    f"https://timesofindia.indiatimes.com/topic/{query_to_be_searched}")

            # search on zoom if the site_to_search contains zoom

            elif 'zoom' in site_to_search:  

                # Telling the user that the search is being executed on zoom

                sp("Searching on Zoom...")


                # open the query_to_be_searched on the zoom

                webbrowser.open(
                    f"https://zoom.us/search?q={query_to_be_searched}")

            # search on hdfcbank if the site_to_search contains hdfcbank

            elif 'hdfcbank' in site_to_search:  

                # Telling the user that the search is being executed on hdfcbank

                sp("Searching on HDFC Bank...")


                # open the query_to_be_searched on the hdfcbank

                webbrowser.open(
                    f"https://www.hdfcbank.com/personal/loan/personal-loan?q={query_to_be_searched}")

            # search on zerodha if the site_to_search contains zerodha

            elif 'zerodha' in site_to_search:   

                # Telling the user that the search is being executed on zerodha

                sp("Searching on Zerodha...")



                # open the query_to_be_searched on the zerodha

                webbrowser.open(
                    f"https://zerodha.com/search?q={query_to_be_searched}")

            # search on LinkedIn if the site_to_search contains linkedin

            elif 'linkedin' in site_to_search:  

                # Telling the user that the search is being executed on linkedin

                sp("Searching on LinkedIn...")





                # open the query_to_be_searched on the linkedin

                webbrowser.open(
                    f"https://www.linkedin.com/search/results/index/?keywords={query_to_be_searched}")

            # search on hotstar if the site_to_search contains hotstar

            elif 'hotstar' in site_to_search:   

                # Telling the user that the search is being executed on hotstar

                sp("Searching on Hotstar...")




                # open the query_to_be_searched on the hotstar

                webbrowser.open(
                    f"https://www.hotstar.com/search?q={query_to_be_searched}")

            # office","netflix","live","icicibank","twitter","stackoverflow","primevideo"

            # search on office if the site_to_search contains office

            elif 'office' in site_to_search:    

                # Telling the user that the search is being executed on office

                sp("Searching on Office...")


                # open the query_to_be_searched on the office

                webbrowser.open(
                    f"https://office.com/search?q={query_to_be_searched}")

            # search on netflix if the site_to_search contains netflix

            elif 'netflix' in site_to_search:   

                # Telling the user that the search is being executed on netflix

                sp("Searching on Netflix...")


                # open the query_to_be_searched on the netflix

                webbrowser.open(
                    f"https://www.netflix.com/search?q={query_to_be_searched}")

            # search on live if the site_to_search contains live

            elif 'live' in site_to_search:  

                # Telling the user that the search is being executed on live    

                sp("Searching on Live...")





                # open the query_to_be_searched on the live

                webbrowser.open(
                    f"https://www.live.com/search?q={query_to_be_searched}")

            # search on icicibank if the site_to_search contains icicibank

            elif 'icicibank' in site_to_search:     

                # Telling the user that the search is being executed on icicibank

                sp("Searching on ICICI Bank...")



                # open the query_to_be_searched on the icicibank

                webbrowser.open(
                    f"https://www.icicibank.com/search?q={query_to_be_searched}")

            # search on twitter if the site_to_search contains twitter

            elif 'twitter' in site_to_search:   

                # Telling the user that the search is being executed on twitter

                sp("Searching on Twitter...")


                # open the query_to_be_searched on the twitter

                webbrowser.open(
                    f"https://twitter.com/search?q={query_to_be_searched}")

            # search on stack overflow if the site_to_search contains stack overflow

            elif 'stack' in site_to_search and 'overflow' in site_to_search:    

                # Telling the user that the search is being executed on stack overflow

                sp("Searching on Stack Overflow...")


                # open the query_to_be_searched on the stackoverflow

                webbrowser.open(
                    f"https://stackoverflow.com/search?q={query_to_be_searched}")

            # search on primevideo if the site_to_search contains primevideo


            elif 'prime' in site_to_search and 'video' in site_to_search:   

                # Telling the user that the search is being executed on primevideo

                sp("Searching on Prime Video...")


                # open the query_to_be_searched on the primevideo

                webbrowser.open(
                    f"https://www.primevideo.com/search?q={query_to_be_searched}")


            elif 'reddit' in site_to_search:    

                # Telling the user that the search is being executed on reddit

                sp("Searching on Reddit...")




                # open the query_to_be_searched on the reddit

                webbrowser.open(
                    f"https://www.reddit.com/search?q={query_to_be_searched}")

                # example: search on onlinesbi
                # outurl = "https://www.onlinesbi.com/search?q=python "

            elif 'onlinesbi' in site_to_search: 

                # Telling the user that the search is being executed on onlinesbi

                sp("Searching on Online SBI...")



                # open the query_to_be_searched on the onlinesbi

                webbrowser.open(
                    f"https://www.onlinesbi.com/search?q={query_to_be_searched}")

            # search on godaddy if the site_to_search contains godaddy

            elif 'godaddy' in site_to_search:   

                # Telling the user that the search is being executed on godaddy

                sp("Searching on GoDaddy...")


                # open the query_to_be_searched on the godaddy

                webbrowser.open(
                    f"https://in.godaddy.com/domainsearch/find?checkAvail=1&domainToCheck={query_to_be_searched}")

            # search on myshopify if the site_to_search contains myshopify

            elif 'myshopify' in site_to_search: 

                # Telling the user that the search is being executed on myshopify

                sp("Searching on My Shopify...")


                # open the query_to_be_searched on the myshopify

                webbrowser.open(
                    f"https://www.myshopify.com/search?q={query_to_be_searched}")

            # search on moneycontrol if the site_to_search contains moneycontrol

            elif 'moneycontrol' in site_to_search:  

                # Telling the user that the search is being executed on moneycontrol

                sp("Searching on Moneycontrol...")


                # open the query_to_be_searched on the moneycontrol

                webbrowser.open(
                    f"https://www.moneycontrol.com/stocks/cptmarket/compsearchnew.php?search_data=&cid=&mbsearch_str=&topsearch_type=1&search_str={query_to_be_searched}")

            # search on grammarly if the site_to_search contains grammarly

            elif 'grammarly' in site_to_search:

                # Telling the user that the search is being executed on grammarly

                sp("Searching on Grammarly...")


                # open the query_to_be_searched on the grammarly

                webbrowser.open(f"{query_to_be_searched} site:grammarly.com")

            # search on microsoftonline if the site_to_search contains microsoftonline

            elif 'microsoftonline' in site_to_search:   

                # Telling the user that the search is being executed on microsoftonline

                sp("Searching on Microsoft Online...")


                # open the query_to_be_searched on the microsoftonline

                webbrowser.open(
                    f"https://www.microsoftonline.com/search?q={query_to_be_searched}")

            # search on adobe if the site_to_search contains adobe

            elif 'adobe' in site_to_search: 

                # Telling the user that the search is being executed on adobe

                sp("Searching on Adobe...")

















                # open the query_to_be_searched on the adobe

                webbrowser.open(
                    f"https://www.adobe.com/in/search?q={query_to_be_searched}")

            # search on irctc if the site_to_search contains irctc

            elif 'irctc' in site_to_search:

                # open the query_to_be_searched on the irctc

                webbrowser.open(
                    f"https://www.irctc.co.in/eticketing/loginHome.jsf?lang=eng")

            # search on freepik if the site_to_search contains freepik

            elif 'freepik' in site_to_search:

                # open the query_to_be_searched on the freepik

                webbrowser.open(
                    f"https://www.freepik.com/search?q={query_to_be_searched}")

            # search on indiamart if the site_to_search contains indiamart

            elif 'indiamart' in site_to_search:

                # open the query_to_be_searched on the indiamart

                webbrowser.open(
                    f"https://www.indiamart.com/search?q={query_to_be_searched}")

            # search on manoramaonline if the site_to_search contains manoramaonline

            elif 'manoramaonline' in site_to_search:

                # open the query_to_be_searched on the manoramaonline

                webbrowser.open(
                    f"https://www.manoramaonline.com/search?q={query_to_be_searched}")

            # search on naukri if the site_to_search contains naukri

            elif 'naukri' in site_to_search:

                # open the query_to_be_searched on the naukri

                webbrowser.open(
                    f"https://www.naukri.com/naukri-jobs-india-jobs-in-{query_to_be_searched}")

            # search on wordpress if the site_to_search contains wordpress

            elif 'wordpress' in site_to_search:

                # open the query_to_be_searched on the wordpress

                webbrowser.open(
                    f"https://wordpress.com/search?q={query_to_be_searched}")

            # search on bing if the site_to_search contains bing

            elif 'bing' in site_to_search:

                # open the query_to_be_searched on the bing

                webbrowser.open(
                    f"https://www.bing.com/search?q={query_to_be_searched}")

            # search on cricbuzz if the site_to_search contains cricbuzz

            elif 'cricbuzz' in site_to_search:

                # open the query_to_be_searched on the cricbuzz

                webbrowser.open(
                    f"https://www.cricbuzz.com/search?q={query_to_be_searched}")

            # search on tradingview if the site_to_search contains tradingview

            elif 'tradingview' in site_to_search:

                # open the query_to_be_searched on the tradingview

                webbrowser.open(
                    f"https://www.tradingview.com/search?q={query_to_be_searched}")

            # search on ndtv if the site_to_search contains ndtv

            elif 'ndtv' in site_to_search:

                # open the query_to_be_searched on the ndtv

                webbrowser.open(
                    f"https://www.ndtv.com/search?q={query_to_be_searched}")

            # search on zoho if the site_to_search contains zoho

            elif 'zoho' in site_to_search:

                # open the query_to_be_searched on the zoho

                webbrowser.open(
                    f"https://www.zoho.com/search?q={query_to_be_searched}")

            # search on tumblr if the site_to_search contains tumblr

            elif 'tumblr' in site_to_search:

                # open the query_to_be_searched on the tumblr

                webbrowser.open(
                    f"https://www.tumblr.com/search/{query_to_be_searched}")

            # search on indeed if the site_to_search contains indeed

            elif 'indeed' in site_to_search:

                # open the query_to_be_searched on the indeed

                webbrowser.open(
                    f"https://www.indeed.com/jobs?q={query_to_be_searched}")

            # search on amazonaws if the site_to_search contains amazonaws

            elif 'amazonaws' in site_to_search:

                # open the query_to_be_searched on the amazonaws

                webbrowser.open(
                    f"https://aws.amazon.com/search/?q={query_to_be_searched}")

            # search on smallpdf if the site_to_search contains smallpdf

            elif 'smallpdf' in site_to_search:

                # open the query_to_be_searched on the smallpdf

                webbrowser.open(
                    f"https://smallpdf.com/search?q={query_to_be_searched}")

            # search on myntra if the site_to_search contains myntra

            elif 'myntra' in site_to_search:

                # open the query_to_be_searched on the myntra

                webbrowser.open(
                    f"https://www.myntra.com/search?q={query_to_be_searched}")

        elif 'open' in query:
            query = query.replace("open", "")

            if 'firefox' in query:
                sp("Firefox is opening")
                webbrowser.open(
                    "https://www.mozilla.org/en-US/firefox/new/")

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

            elif 'quora' in query:
                webbrowser.open("https://www.quora.com/")

            elif 'reddit' in query:
                if 'reddit' in query:
                    reg_ex = re.search('reddit (.*)', query)
                    url = 'https://www.reddit.com/'
                    if reg_ex:
                        subreddit = reg_ex.group(1)
                        url = url + 'r/' + subreddit
                    webbrowser.open(url)
                    sp('The Reddit content has been opened for you Sir.')

                else:
                    webbrowser.open("https://www.reddit.com/")

            else:
                webbrowser.open(
                    f"https://duckduckgo.com/?q=%21+{query}&ia=olivia")


# create a translate feature in the virutal assistant

        elif 'translate' in query:
            query = query.replace("translate", "")

            LANGUAGES = {
                'af': 'afrikaans',
                'sq': 'albanian',
                'am': 'amharic',
                'ar': 'arabic',
                'hy': 'armenian',
                'az': 'azerbaijani',
                'eu': 'basque',
                'be': 'belarusian',
                'bn': 'bengali',
                'bs': 'bosnian',
                'bg': 'bulgarian',
                'ca': 'catalan',
                'ceb': 'cebuano',
                'ny': 'chichewa',
                'zh-cn': 'chinese (simplified)',
                'zh-tw': 'chinese (traditional)',
                'co': 'corsican',
                'hr': 'croatian',
                'cs': 'czech',
                'da': 'danish',
                'nl': 'dutch',
                'en': 'english',
                'eo': 'esperanto',
                'et': 'estonian',
                'tl': 'filipino',
                'fi': 'finnish',
                'fr': 'french',
                'fy': 'frisian',
                'gl': 'galician',
                'ka': 'georgian',
                'de': 'german',
                'el': 'greek',
                'gu': 'gujarati',
                'ht': 'haitian creole',
                'ha': 'hausa',
                'haw': 'hawaiian',
                'iw': 'hebrew',
                'he': 'hebrew',
                'hi': 'hindi',
                'hmn': 'hmong',
                'hu': 'hungarian',
                'is': 'icelandic',
                'ig': 'igbo',
                'id': 'indonesian',
                'ga': 'irish',
                'it': 'italian',
                'ja': 'japanese',
                'jw': 'javanese',
                'kn': 'kannada',
                'kk': 'kazakh',
                'km': 'khmer',
                'ko': 'korean',
                'ku': 'kurdish (kurmanji)',
                'ky': 'kyrgyz',
                'lo': 'lao',
                'la': 'latin',
                'lv': 'latvian',
                'lt': 'lithuanian',
                'lb': 'luxembourgish',
                'mk': 'macedonian',
                'mg': 'malagasy',
                'ms': 'malay',
                'ml': 'malayalam',
                'mt': 'maltese',
                'mi': 'maori',
                'mr': 'marathi',
                'mn': 'mongolian',
                'my': 'myanmar (burmese)',
                'ne': 'nepali',
                'no': 'norwegian',
                'or': 'odia',
                'ps': 'pashto',
                'fa': 'persian',
                'pl': 'polish',
                'pt': 'portuguese',
                'pa': 'punjabi',
                'ro': 'romanian',
                'ru': 'russian',
                'sm': 'samoan',
                'gd': 'scots gaelic',
                'sr': 'serbian',
                'st': 'sesotho',
                'sn': 'shona',
                'sd': 'sindhi',
                'si': 'sinhala',
                'sk': 'slovak',
                'sl': 'slovenian',
                'so': 'somali',
                'es': 'spanish',
                'su': 'sundanese',
                'sw': 'swahili',
                'sv': 'swedish',
                'tg': 'tajik',
                'ta': 'tamil',
                'te': 'telugu',
                'th': 'thai',
                'tr': 'turkish',
                'uk': 'ukrainian',
                'ur': 'urdu',
                'ug': 'uyghur',
                'uz': 'uzbek',
                'vi': 'vietnamese',
                'cy': 'welsh',
                'xh': 'xhosa',
                'yi': 'yiddish',
                'yo': 'yoruba',
                'zu': 'zulu',
            }

            # speak to which language you want to translate
            sp('To which language you want to translate?')

            # get the query

            query = takeCommand().lower()

            # speak what you want to translate
            sp("What do you want to translate?")

            translate_this = takeCommand().lower()

            # translate to the afrikaans

            if 'afrikaans' in query:
                # telling the user that we are translating the text to the afrikaans
                speak("translating to afrikaans")
                # getting the text from the user and replacing the "to afrikaans" with nothing so that we can translate the text
                query = query.replace("to afrikaans", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the afrikaans and storing the result in a variable named result
                result = translator.translate(translate_this, dest='af')

                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the albanian

            elif 'albanian' in query:
                # telling the user that we are translating the text to the albanian
                speak("translating to albanian")
                # getting the text from the user and replacing the "to albanian" with nothing so that we can translate the text
                query = query.replace("to albanian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the albanian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='sq')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the amharic

            elif 'amharic' in query:
                # telling the user that we are translating the text to the amharic
                speak("translating to amharic")
                # getting the text from the user and replacing the "to amharic" with nothing so that we can translate the text
                query = query.replace("to amharic", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the amharic and storing the result in a variable named result
                result = translator.translate(translate_this, dest='am')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the arabic

            elif 'arabic' in query:
                # telling the user that we are translating the text to the arabic
                speak("translating to arabic")
                # getting the text from the user and replacing the "to arabic" with nothing so that we can translate the text
                query = query.replace("to arabic", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the arabic and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ar')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the armenian

            elif 'armenian' in query:
                # telling the user that we are translating the text to the armenian
                speak("translating to armenian")
                # getting the text from the user and replacing the "to armenian" with nothing so that we can translate the text
                query = query.replace("to armenian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the armenian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='hy')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the azerbaijani

            elif 'azerbaijani' in query:

                # telling the user that we are translating the text to the azerbaijani
                speak("translating to azerbaijani")
                # getting the text from the user and replacing the "to azerbaijani" with nothing so that we can translate the text
                query = query.replace("to azerbaijani", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the azerbaijani and storing the result in a variable named result
                result = translator.translate(translate_this, dest='az')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the basque

            elif 'basque' in query:
                # telling the user that we are translating the text to the basque
                speak("translating to basque")
                # getting the text from the user and replacing the "to basque" with nothing so that we can translate the text
                query = query.replace("to basque", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the basque and storing the result in a variable named result
                result = translator.translate(translate_this, dest='eu')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the belarusian

            elif 'belarusian' in query:
                # telling the user that we are translating the text to the belarusian
                speak("translating to belarusian")
                # getting the text from the user and replacing the "to belarusian" with nothing so that we can translate the text
                query = query.replace("to belarusian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the belarusian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='be')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the bengali

            elif 'bengali' in query:
                # telling the user that we are translating the text to the bengali
                speak("translating to bengali")
                # getting the text from the user and replacing the "to bengali" with nothing so that we can translate the text
                query = query.replace("to bengali", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the bengali and storing the result in a variable named result
                result = translator.translate(translate_this, dest='bn')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the bosnian

            elif 'bosnian' in query:
                # telling the user that we are translating the text to the bosnian
                speak("translating to bosnian")
                # getting the text from the user and replacing the "to bosnian" with nothing so that we can translate the text
                query = query.replace("to bosnian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the bosnian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='bs')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the bulgarian
            elif 'bulgarian' in query:
                # telling the user that we are translating the text to the bulgarian
                speak("translating to bulgarian")
                # getting the text from the user and replacing the "to bulgarian" with nothing so that we can translate the text
                query = query.replace("to bulgarian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the bulgarian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='bg')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the catalan
            elif 'catalan' in query:
                # telling the user that we are translating the text to the catalan
                speak("translating to catalan")
                # getting the text from the user and replacing the "to catalan" with nothing so that we can translate the text
                query = query.replace("to catalan", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the catalan and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ca')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the cebuano
            elif 'cebuano' in query:
                # telling the user that we are translating the text to the cebuano
                speak("translating to cebuano")
                # getting the text from the user and replacing the "to cebuano" with nothing so that we can translate the text
                query = query.replace("to cebuano", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the cebuano and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ceb')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the chichewa
            elif 'chichewa' in query:
                # telling the user that we are translating the text to the chichewa
                speak("translating to chichewa")
                # getting the text from the user and replacing the "to chichewa" with nothing so that we can translate the text
                query = query.replace("to chichewa", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the chichewa and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ny')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the chinese
            elif 'chinese' in query:
                # telling the user that we are translating the text to the chinese
                speak("translating to chinese")
                # getting the text from the user and replacing the "to chinese" with nothing so that we can translate the text
                query = query.replace("to chinese", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the chinese and storing the result in a variable named result
                result = translator.translate(translate_this, dest='zh-CN')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the corican
            elif 'corican' in query:
                # telling the user that we are translating the text to the corican
                speak("translating to corican")
                # getting the text from the user and replacing the "to corican" with nothing so that we can translate the text
                query = query.replace("to corican", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the corican and storing the result in a variable named result
                result = translator.translate(translate_this, dest='co')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the croatian
            elif 'croatian' in query:
                # telling the user that we are translating the text to the croatian
                speak("translating to croatian")
                # getting the text from the user and replacing the "to croatian" with nothing so that we can translate the text
                query = query.replace("to croatian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the croatian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='hr')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the czech
            elif 'czech' in query:
                # telling the user that we are translating the text to the czech
                speak("translating to czech")
                # getting the text from the user and replacing the "to czech" with nothing so that we can translate the text
                query = query.replace("to czech", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the czech and storing the result in a variable named result
                result = translator.translate(translate_this, dest='cs')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the danish
            elif 'danish' in query:
                # telling the user that we are translating the text to the danish
                speak("translating to danish")
                # getting the text from the user and replacing the "to danish" with nothing so that we can translate the text
                query = query.replace("to danish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the danish and storing the result in a variable named result
                result = translator.translate(translate_this, dest='da')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the dutch
            elif 'dutch' in query:
                # telling the user that we are translating the text to the dutch
                speak("translating to dutch")
                # getting the text from the user and replacing the "to dutch" with nothing so that we can translate the text
                query = query.replace("to dutch", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the dutch and storing the result in a variable named result
                result = translator.translate(translate_this, dest='nl')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the english
            elif 'english' in query:
                # telling the user that we are translating the text to the english
                speak("translating to english")
                # getting the text from the user and replacing the "to english" with nothing so that we can translate the text
                query = query.replace("to english", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the english and storing the result in a variable named result
                result = translator.translate(translate_this, dest='en')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the esperanto
            elif 'esperanto' in query:
                # telling the user that we are translating the text to the esperanto
                speak("translating to esperanto")
                # getting the text from the user and replacing the "to esperanto" with nothing so that we can translate the text
                query = query.replace("to esperanto", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the esperanto and storing the result in a variable named result
                result = translator.translate(translate_this, dest='eo')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the estonian
            elif 'estonian' in query:
                # telling the user that we are translating the text to the estonian
                speak("translating to estonian")
                # getting the text from the user and replacing the "to estonian" with nothing so that we can translate the text
                query = query.replace("to estonian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the estonian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='et')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the filipino
            elif 'filipino' in query:
                # telling the user that we are translating the text to the filipino
                speak("translating to filipino")
                # getting the text from the user and replacing the "to filipino" with nothing so that we can translate the text
                query = query.replace("to filipino", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the filipino and storing the result in a variable named result
                result = translator.translate(translate_this, dest='tl')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the finnish
            elif 'finnish' in query:
                # telling the user that we are translating the text to the finnish
                speak("translating to finnish")
                # getting the text from the user and replacing the "to finnish" with nothing so that we can translate the text
                query = query.replace("to finnish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the finnish and storing the result in a variable named result
                result = translator.translate(translate_this, dest='fi')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the french
            elif 'french' in query:
                # telling the user that we are translating the text to the french
                speak("translating to french")
                # getting the text from the user and replacing the "to french" with nothing so that we can translate the text
                query = query.replace("to french", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the french and storing the result in a variable named result
                result = translator.translate(translate_this, dest='fr')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the frisian
            elif 'frisian' in query:
                # telling the user that we are translating the text to the frisian
                speak("translating to frisian")
                # getting the text from the user and replacing the "to frisian" with nothing so that we can translate the text
                query = query.replace("to frisian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the frisian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='fy')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the galician
            elif 'galician' in query:
                # telling the user that we are translating the text to the galician
                speak("translating to galician")
                # getting the text from the user and replacing the "to galician" with nothing so that we can translate the text
                query = query.replace("to galician", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the galician and storing the result in a variable named result
                result = translator.translate(translate_this, dest='gl')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the georgian
            elif 'georgian' in query:

                # telling the user that we are translating the text to the georgian
                speak("translating to georgian")
                # getting the text from the user and replacing the "to georgian" with nothing so that we can translate the text
                query = query.replace("to georgian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the georgian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ka')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the german
            elif 'german' in query:
                # telling the user that we are translating the text to the german
                speak("translating to german")
                # getting the text from the user and replacing the "to german" with nothing so that we can translate the text
                query = query.replace("to german", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the german and storing the result in a variable named result
                result = translator.translate(translate_this, dest='de')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the greek
            elif 'greek' in query:
                # telling the user that we are translating the text to the greek
                speak("translating to greek")
                # getting the text from the user and replacing the "to greek" with nothing so that we can translate the text
                query = query.replace("to greek", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the greek and storing the result in a variable named result
                result = translator.translate(translate_this, dest='el')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the gujarati
            elif 'gujarati' in query:
                # telling the user that we are translating the text to the gujarati
                speak("translating to gujarati")
                # getting the text from the user and replacing the "to gujarati" with nothing so that we can translate the text
                query = query.replace("to gujarati", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the gujarati and storing the result in a variable named result
                result = translator.translate(translate_this, dest='gu')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the haitian creole
            elif 'haitian creole' in query:
                # telling the user that we are translating the text to the haitian creole
                speak("translating to haitian creole")
                # getting the text from the user and replacing the "to haitian creole" with nothing so that we can translate the text
                query = query.replace("to haitian creole", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the haitian creole and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ht')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the hausa
            elif 'hausa' in query:

                # telling the user that we are translating the text to the hausa
                speak("translating to hausa")
                # getting the text from the user and replacing the "to hausa" with nothing so that we can translate the text
                query = query.replace("to hausa", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the hausa and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ha')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the hawaiian
            elif 'hawaiian' in query:
                # telling the user that we are translating the text to the hawaiian
                speak("translating to hawaiian")
                # getting the text from the user and replacing the "to hawaiian" with nothing so that we can translate the text
                query = query.replace("to hawaiian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the hawaiian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='haw')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the hebrew
            elif 'hebrew' in query:
                # telling the user that we are translating the text to the hebrew
                speak("translating to hebrew")
                # getting the text from the user and replacing the "to hebrew" with nothing so that we can translate the text
                query = query.replace("to hebrew", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the hebrew and storing the result in a variable named result
                result = translator.translate(translate_this, dest='he')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the hindi
            elif 'hindi' in query:
                # telling the user that we are translating the text to the hindi
                speak("translating to hindi")
                # getting the text from the user and replacing the "to hindi" with nothing so that we can translate the text
                query = query.replace("to hindi", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the hindi and storing the result in a variable named result
                result = translator.translate(translate_this, dest='hi')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the hmong
            elif 'hmong' in query:
                # telling the user that we are translating the text to the hmong
                speak("translating to hmong")
                # getting the text from the user and replacing the "to hmong" with nothing so that we can translate the text
                query = query.replace("to hmong", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the hmong and storing the result in a variable named result
                result = translator.translate(translate_this, dest='hmn')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the hungarian
            elif 'hungarian' in query:
                # telling the user that we are translating the text to the hungarian
                speak("translating to hungarian")
                # getting the text from the user and replacing the "to hungarian" with nothing so that we can translate the text
                query = query.replace("to hungarian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the hungarian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='hu')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the icelandic
            elif 'icelandic' in query:
                # telling the user that we are translating the text to the icelandic
                speak("translating to icelandic")
                # getting the text from the user and replacing the "to icelandic" with nothing so that we can translate the text
                query = query.replace("to icelandic", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the icelandic and storing the result in a variable named result
                result = translator.translate(translate_this, dest='is')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the igbo
            elif 'igbo' in query:
                # telling the user that we are translating the text to the igbo
                speak("translating to igbo")
                # getting the text from the user and replacing the "to igbo" with nothing so that we can translate the text
                query = query.replace("to igbo", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the igbo and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ig')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the indonesian
            elif 'indonesian' in query:
                # telling the user that we are translating the text to the indonesian
                speak("translating to indonesian")
                # getting the text from the user and replacing the "to indonesian" with nothing so that we can translate the text
                query = query.replace("to indonesian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the indonesian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='id')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the irish
            elif 'irish' in query:
                # telling the user that we are translating the text to the irish
                speak("translating to irish")
                # getting the text from the user and replacing the "to irish" with nothing so that we can translate the text
                query = query.replace("to irish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the irish and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ga')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the italian
            elif 'italian' in query:
                # telling the user that we are translating the text to the italian
                speak("translating to italian")
                # getting the text from the user and replacing the "to italian" with nothing so that we can translate the text
                query = query.replace("to italian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the italian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='it')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the japanese
            elif 'japanese' in query:

                # telling the user that we are translating the text to the japanese
                speak("translating to japanese")
                # getting the text from the user and replacing the "to japanese" with nothing so that we can translate the text
                query = query.replace("to japanese", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the japanese and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ja')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the javanese
            elif 'javanese' in query:
                # telling the user that we are translating the text to the javanese
                speak("translating to javanese")
                # getting the text from the user and replacing the "to javanese" with nothing so that we can translate the text
                query = query.replace("to javanese", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the javanese and storing the result in a variable named result
                result = translator.translate(translate_this, dest='jw')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the kannada
            elif 'kannada' in query:
                # telling the user that we are translating the text to the kannada
                speak("translating to kannada")
                # getting the text from the user and replacing the "to kannada" with nothing so that we can translate the text
                query = query.replace("to kannada", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the kannada and storing the result in a variable named result
                result = translator.translate(translate_this, dest='kn')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the kazakh
            elif 'kazakh' in query:
                # telling the user that we are translating the text to the kazakh
                speak("translating to kazakh")
                # getting the text from the user and replacing the "to kazakh" with nothing so that we can translate the text
                query = query.replace("to kazakh", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the kazakh and storing the result in a variable named result
                result = translator.translate(translate_this, dest='kk')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the khmer
            elif 'khmer' in query:

                # telling the user that we are translating the text to the khmer
                speak("translating to khmer")
                # getting the text from the user and replacing the "to khmer" with nothing so that we can translate the text
                query = query.replace("to khmer", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the khmer and storing the result in a variable named result
                result = translator.translate(translate_this, dest='km')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the korean
            elif 'korean' in query:
                # telling the user that we are translating the text to the korean
                speak("translating to korean")
                # getting the text from the user and replacing the "to korean" with nothing so that we can translate the text
                query = query.replace("to korean", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the korean and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ko')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the kurdish
            elif 'kurdish' in query:
                # telling the user that we are translating the text to the kurdish
                speak("translating to kurdish")
                # getting the text from the user and replacing the "to kurdish" with nothing so that we can translate the text
                query = query.replace("to kurdish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the kurdish and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ku')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the kurmanji
            elif 'kurmanji' in query:
                # telling the user that we are translating the text to the kurmanji
                speak("translating to kurmanji")
                # getting the text from the user and replacing the "to kurmanji" with nothing so that we can translate the text
                query = query.replace("to kurmanji", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the kurmanji and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ku')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the kyrgyz
            elif 'kyrgyz' in query:

                # telling the user that we are translating the text to the kyrgyz
                speak("translating to kyrgyz")
                # getting the text from the user and replacing the "to kyrgyz" with nothing so that we can translate the text
                query = query.replace("to kyrgyz", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the kyrgyz and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ky')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the lao
            elif 'lao' in query:
                # telling the user that we are translating the text to the lao
                speak("translating to lao")
                # getting the text from the user and replacing the "to lao" with nothing so that we can translate the text
                query = query.replace("to lao", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the lao and storing the result in a variable named result
                result = translator.translate(translate_this, dest='lo')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the latin
            elif 'latin' in query:
                # telling the user that we are translating the text to the latin
                speak("translating to latin")
                # getting the text from the user and replacing the "to latin" with nothing so that we can translate the text
                query = query.replace("to latin", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the latin and storing the result in a variable named result
                result = translator.translate(translate_this, dest='la')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the latvian
            elif 'latvian' in query:

                # telling the user that we are translating the text to the latvian
                speak("translating to latvian")
                # getting the text from the user and replacing the "to latvian" with nothing so that we can translate the text
                query = query.replace("to latvian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the latvian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='lv')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the lithuanian
            elif 'lithuanian' in query:
                # telling the user that we are translating the text to the lithuanian
                speak("translating to lithuanian")
                # getting the text from the user and replacing the "to lithuanian" with nothing so that we can translate the text
                query = query.replace("to lithuanian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the lithuanian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='lt')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the luxembourgish
            elif 'luxembourgish' in query:
                # telling the user that we are translating the text to the luxembourgish
                speak("translating to luxembourgish")
                # getting the text from the user and replacing the "to luxembourgish" with nothing so that we can translate the text
                query = query.replace("to luxembourgish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the luxembourgish and storing the result in a variable named result

                result = translator.translate(query, dest='lb')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the macedonian
            elif 'macedonian' in query:
                # telling the user that we are translating the text to the macedonian
                speak("translating to macedonian")
                # getting the text from the user and replacing the "to macedonian" with nothing so that we can translate the text
                query = query.replace("to macedonian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the macedonian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='mk')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the malagasy
            elif 'malagasy' in query:
                # telling the user that we are translating the text to the malagasy
                speak("translating to malagasy")
                # getting the text from the user and replacing the "to malagasy" with nothing so that we can translate the text
                query = query.replace("to malagasy", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the malagasy and storing the result in a variable named result
                result = translator.translate(translate_this, dest='mg')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the malay
            elif 'malay' in query:
                # telling the user that we are translating the text to the malay
                speak("translating to malay")
                # getting the text from the user and replacing the "to malay" with nothing so that we can translate the text
                query = query.replace("to malay", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the malay and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ms')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the malayalam
            elif 'malayalam' in query:
                # telling the user that we are translating the text to the malayalam
                speak("translating to malayalam")
                # getting the text from the user and replacing the "to malayalam" with nothing so that we can translate the text
                query = query.replace("to malayalam", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the malayalam and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ml')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the maltese
            elif 'maltese' in query:
                # telling the user that we are translating the text to the maltese
                speak("translating to maltese")
                # getting the text from the user and replacing the "to maltese" with nothing so that we can translate the text
                query = query.replace("to maltese", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the maltese and storing the result in a variable named result
                result = translator.translate(translate_this, dest='mt')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the maori
            elif 'maori' in query:
                # telling the user that we are translating the text to the maori
                speak("translating to maori")
                # getting the text from the user and replacing the "to maori" with nothing so that we can translate the text
                query = query.replace("to maori", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the maori and storing the result in a variable named result
                result = translator.translate(translate_this, dest='mi')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the marathi
            elif 'marathi' in query:
                # telling the user that we are translating the text to the marathi
                speak("translating to marathi")
                # getting the text from the user and replacing the "to marathi" with nothing so that we can translate the text
                query = query.replace("to marathi", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the marathi and storing the result in a variable named result
                result = translator.translate(translate_this, dest='mr')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the mongolian
            elif 'mongolian' in query:
                # telling the user that we are translating the text to the mongolian
                speak("translating to mongolian")
                # getting the text from the user and replacing the "to mongolian" with nothing so that we can translate the text
                query = query.replace("to mongolian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the mongolian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='mn')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the myanmar
            elif 'myanmar' in query:
                # telling the user that we are translating the text to the myanmar
                speak("translating to myanmar")
                # getting the text from the user and replacing the "to myanmar" with nothing so that we can translate the text
                query = query.replace("to myanmar", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the myanmar and storing the result in a variable named result
                result = translator.translate(translate_this, dest='my')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the burmese
            elif 'burmese' in query:
                # telling the user that we are translating the text to the burmese
                speak("translating to burmese")
                # getting the text from the user and replacing the "to burmese" with nothing so that we can translate the text
                query = query.replace("to burmese", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the burmese and storing the result in a variable named result
                result = translator.translate(translate_this, dest='my')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the nepali
            elif 'nepali' in query:
                # telling the user that we are translating the text to the nepali
                speak("translating to nepali")
                # getting the text from the user and replacing the "to nepali" with nothing so that we can translate the text
                query = query.replace("to nepali", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the nepali and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ne')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the norwegian
            elif 'norwegian' in query:
                # telling the user that we are translating the text to the norwegian
                speak("translating to norwegian")
                # getting the text from the user and replacing the "to norwegian" with nothing so that we can translate the text
                query = query.replace("to norwegian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the norwegian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='no')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the odia
            elif 'odia' in query:
                # telling the user that we are translating the text to the odia
                speak("translating to odia")
                # getting the text from the user and replacing the "to odia" with nothing so that we can translate the text
                query = query.replace("to odia", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the odia and storing the result in a variable named result
                result = translator.translate(translate_this, dest='or')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the pashto
            elif 'pashto' in query:
                # telling the user that we are translating the text to the pashto
                speak("translating to pashto")
                # getting the text from the user and replacing the "to pashto" with nothing so that we can translate the text
                query = query.replace("to pashto", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the pashto and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ps')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the persian
            elif 'persian' in query:
                # telling the user that we are translating the text to the persian
                speak("translating to persian")
                # getting the text from the user and replacing the "to persian" with nothing so that we can translate the text
                query = query.replace("to persian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the persian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='fa')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the polish
            elif 'polish' in query:
                # telling the user that we are translating the text to the polish
                speak("translating to polish")
                # getting the text from the user and replacing the "to polish" with nothing so that we can translate the text
                query = query.replace("to polish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the polish and storing the result in a variable named result
                result = translator.translate(translate_this, dest='pl')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the portuguese
            elif 'portuguese' in query:
                # telling the user that we are translating the text to the portuguese
                speak("translating to portuguese")
                # getting the text from the user and replacing the "to portuguese" with nothing so that we can translate the text
                query = query.replace("to portuguese", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the portuguese and storing the result in a variable named result
                result = translator.translate(translate_this, dest='pt')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the punjabi
            elif 'punjabi' in query:
                # telling the user that we are translating the text to the punjabi
                speak("translating to punjabi")
                # getting the text from the user and replacing the "to punjabi" with nothing so that we can translate the text
                query = query.replace("to punjabi", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the punjabi and storing the result in a variable named result
                result = translator.translate(translate_this, dest='pa')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the romanian
            elif 'romanian' in query:
                # telling the user that we are translating the text to the romanian
                speak("translating to romanian")
                # getting the text from the user and replacing the "to romanian" with nothing so that we can translate the text
                query = query.replace("to romanian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the romanian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ro')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the russian
            elif 'russian' in query:
                # telling the user that we are translating the text to the russian
                speak("translating to russian")
                # getting the text from the user and replacing the "to russian" with nothing so that we can translate the text
                query = query.replace("to russian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the russian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ru')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the samoan
            elif 'samoan' in query:
                # telling the user that we are translating the text to the samoan
                speak("translating to samoan")
                # getting the text from the user and replacing the "to samoan" with nothing so that we can translate the text
                query = query.replace("to samoan", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the samoan and storing the result in a variable named result
                result = translator.translate(translate_this, dest='sm')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the scots gaelic
            elif 'scots gaelic' in query:
                # telling the user that we are translating the text to the scots gaelic
                speak("translating to scots gaelic")
                # getting the text from the user and replacing the "to scots gaelic" with nothing so that we can translate the text
                query = query.replace("to scots gaelic", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the scots gaelic and storing the result in a variable named result
                result = translator.translate(translate_this, dest='gd')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the serbian
            elif 'serbian' in query:
                # telling the user that we are translating the text to the serbian
                speak("translating to serbian")
                # getting the text from the user and replacing the "to serbian" with nothing so that we can translate the text
                query = query.replace("to serbian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the serbian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='sr')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the sesotho
            elif 'sesotho' in query:
                # telling the user that we are translating the text to the sesotho
                speak("translating to sesotho")
                # getting the text from the user and replacing the "to sesotho" with nothing so that we can translate the text
                query = query.replace("to sesotho", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the sesotho and storing the result in a variable named result
                result = translator.translate(translate_this, dest='st')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the shona
            elif 'shona' in query:
                # telling the user that we are translating the text to the shona
                speak("translating to shona")
                # getting the text from the user and replacing the "to shona" with nothing so that we can translate the text
                query = query.replace("to shona", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the shona and storing the result in a variable named result
                result = translator.translate(translate_this, dest='sn')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the sindhi
            elif 'sindhi' in query:
                # telling the user that we are translating the text to the sindhi
                speak("translating to sindhi")
                # getting the text from the user and replacing the "to sindhi" with nothing so that we can translate the text
                query = query.replace("to sindhi", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the sindhi and storing the result in a variable named result
                result = translator.translate(translate_this, dest='sd')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the sinhala
            elif 'sinhala' in query:
                # telling the user that we are translating the text to the sinhala
                speak("translating to sinhala")
                # getting the text from the user and replacing the "to sinhala" with nothing so that we can translate the text
                query = query.replace("to sinhala", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the sinhala and storing the result in a variable named result
                result = translator.translate(translate_this, dest='si')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the slovak
            elif 'slovak' in query:
                # telling the user that we are translating the text to the slovak
                speak("translating to slovak")
                # getting the text from the user and replacing the "to slovak" with nothing so that we can translate the text
                query = query.replace("to slovak", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the slovak and storing the result in a variable named result
                result = translator.translate(translate_this, dest='sk')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the slovenian
            elif 'slovenian' in query:
                # telling the user that we are translating the text to the slovenian
                speak("translating to slovenian")
                # getting the text from the user and replacing the "to slovenian" with nothing so that we can translate the text
                query = query.replace("to slovenian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the slovenian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='sl')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the somali
            elif 'somali' in query:
                # telling the user that we are translating the text to the somali
                speak("translating to somali")
                # getting the text from the user and replacing the "to somali" with nothing so that we can translate the text
                query = query.replace("to somali", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the somali and storing the result in a variable named result
                result = translator.translate(translate_this, dest='so')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the spanish
            elif 'spanish' in query:

                # telling the user that we are translating the text to the spanish
                speak("translating to spanish")
                # getting the text from the user and replacing the "to spanish" with nothing so that we can translate the text
                query = query.replace("to spanish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the spanish and storing the result in a variable named result
                result = translator.translate(translate_this, dest='es')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the sundanese
            elif 'sundanese' in query:
                # telling the user that we are translating the text to the sundanese
                speak("translating to sundanese")
                # getting the text from the user and replacing the "to sundanese" with nothing so that we can translate the text
                query = query.replace("to sundanese", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the sundanese and storing the result in a variable named result
                result = translator.translate(translate_this, dest='su')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the swahili
            elif 'swahili' in query:
                # telling the user that we are translating the text to the swahili
                speak("translating to swahili")
                # getting the text from the user and replacing the "to swahili" with nothing so that we can translate the text
                query = query.replace("to swahili", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the swahili and storing the result in a variable named result
                result = translator.translate(translate_this, dest='sw')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the swedish
            elif 'swedish' in query:
                # telling the user that we are translating the text to the swedish
                speak("translating to swedish")
                # getting the text from the user and replacing the "to swedish" with nothing so that we can translate the text
                query = query.replace("to swedish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the swedish and storing the result in a variable named result
                result = translator.translate(translate_this, dest='sv')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the tajik
            elif 'tajik' in query:
                # telling the user that we are translating the text to the tajik
                speak("translating to tajik")
                # getting the text from the user and replacing the "to tajik" with nothing so that we can translate the text
                query = query.replace("to tajik", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the tajik and storing the result in a variable named result
                result = translator.translate(translate_this, dest='tg')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the tamil
            elif 'tamil' in query:
                # telling the user that we are translating the text to the tamil
                speak("translating to tamil")
                # getting the text from the user and replacing the "to tamil" with nothing so that we can translate the text
                query = query.replace("to tamil", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the tamil and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ta')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the telugu
            elif 'telugu' in query:
                # telling the user that we are translating the text to the telugu
                speak("translating to telugu")
                # getting the text from the user and replacing the "to telugu" with nothing so that we can translate the text
                query = query.replace("to telugu", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the telugu and storing the result in a variable named result
                result = translator.translate(translate_this, dest='te')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the thai
            elif 'thai' in query:
                # telling the user that we are translating the text to the thai
                speak("translating to thai")
                # getting the text from the user and replacing the "to thai" with nothing so that we can translate the text
                query = query.replace("to thai", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the thai and storing the result in a variable named result
                result = translator.translate(translate_this, dest='th')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the turkish
            elif 'turkish' in query:
                # telling the user that we are translating the text to the turkish
                speak("translating to turkish")
                # getting the text from the user and replacing the "to turkish" with nothing so that we can translate the text
                query = query.replace("to turkish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the turkish and storing the result in a variable named result
                result = translator.translate(translate_this, dest='tr')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the ukrainian
            elif 'ukrainian' in query:
                # telling the user that we are translating the text to the ukrainian
                speak("translating to ukrainian")
                # getting the text from the user and replacing the "to ukrainian" with nothing so that we can translate the text
                query = query.replace("to ukrainian", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the ukrainian and storing the result in a variable named result
                result = translator.translate(translate_this, dest='uk')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the urdu
            elif 'urdu' in query:
                # telling the user that we are translating the text to the urdu
                speak("translating to urdu")
                # getting the text from the user and replacing the "to urdu" with nothing so that we can translate the text
                query = query.replace("to urdu", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the urdu and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ur')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the uyghur
            elif 'uyghur' in query:
                # telling the user that we are translating the text to the uyghur
                speak("translating to uyghur")
                # getting the text from the user and replacing the "to uyghur" with nothing so that we can translate the text
                query = query.replace("to uyghur", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the uyghur and storing the result in a variable named result
                result = translator.translate(translate_this, dest='ug')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the uzbek
            elif 'uzbek' in query:
                # telling the user that we are translating the text to the uzbek
                speak("translating to uzbek")
                # getting the text from the user and replacing the "to uzbek" with nothing so that we can translate the text
                query = query.replace("to uzbek", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the uzbek and storing the result in a variable named result
                result = translator.translate(translate_this, dest='uz')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the vietnamese
            elif 'vietnamese' in query:
                # telling the user that we are translating the text to the vietnamese
                speak("translating to vietnamese")
                # getting the text from the user and replacing the "to vietnamese" with nothing so that we can translate the text
                query = query.replace("to vietnamese", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the vietnamese and storing the result in a variable named result
                result = translator.translate(translate_this, dest='vi')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the welsh
            elif 'welsh' in query:
                # telling the user that we are translating the text to the welsh
                speak("translating to welsh")
                # getting the text from the user and replacing the "to welsh" with nothing so that we can translate the text
                query = query.replace("to welsh", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the welsh and storing the result in a variable named result
                result = translator.translate(translate_this, dest='cy')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the xhosa
            elif 'xhosa' in query:
                # telling the user that we are translating the text to the xhosa
                speak("translating to xhosa")
                # getting the text from the user and replacing the "to xhosa" with nothing so that we can translate the text
                query = query.replace("to xhosa", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the xhosa and storing the result in a variable named result
                result = translator.translate(translate_this, dest='xh')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the yiddish
            elif 'yiddish' in query:
                # telling the user that we are translating the text to the yiddish
                speak("translating to yiddish")
                # getting the text from the user and replacing the "to yiddish" with nothing so that we can translate the text
                query = query.replace("to yiddish", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the yiddish and storing the result in a variable named result
                result = translator.translate(translate_this, dest='yi')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the yoruba
            elif 'yoruba' in query:
                # telling the user that we are translating the text to the yoruba
                speak("translating to yoruba")
                # getting the text from the user and replacing the "to yoruba" with nothing so that we can translate the text
                query = query.replace("to yoruba", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the yoruba and storing the result in a variable named result
                result = translator.translate(translate_this, dest='yo')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

            # translate to the zulu
            elif 'zulu' in query:
                # telling the user that we are translating the text to the zulu
                speak("translating to zulu")
                # getting the text from the user and replacing the "to zulu" with nothing so that we can translate the text
                query = query.replace("to zulu", "")

                # using the goslate library to translate the text

                translator = Translator()

                # translating the text to the zulu and storing the result in a variable named result
                result = translator.translate(translate_this, dest='zu')
                # printing the result

                print(f"The Translated Text is: {result.text}")

                # printing the pronunciation of the result

                print(
                    f"The pronunciation of the result is {result.pronunciation}")

                # speaking result pronunciation

                speak(result.pronunciation)

        elif 'close' in query:

            # telling the user that we are closing the program
            speak("closing the program")

            # removing the stop words from the text
            query = query.replace("close", "")

            # stripping the text of any spaces
            query = query.strip()

            if query == "page":

                # pressing the control + w to close the program
                pyautogui.hotkey('ctrl', 'w')

            elif query == "window":

                # pressing the alt + f4 to close the window
                pyautogui.hotkey('alt', 'f4')

                # speaking that the window is closed
                speak("the window is closed")

            elif query == "program":

                # pressing the alt + f4 to close the program
                pyautogui.hotkey('alt', 'f4')

                # speaking that the program is closed
                speak("the program is closed")

            elif query == "tab":

                # pressing the control + w to close the tab
                pyautogui.hotkey('ctrl', 'w')

                # speaking that the tab is closed

                speak("the tab is closed")

            elif 'app' in query or 'application' in query:

                # pressing the alt + f4 to close the program

                pyautogui.hotkey('alt', 'f4')

                # speaking that the application is closed
                speak("the application is closed")

            elif 'chrome' in query:

                sp('closing chrome')
                os.system('TASKKILL /F /IM chrome.exe')

                # speaking that the chrome browser is closed

                speak("the chrome browser is closed")

            elif 'spotify' in query:

                sp('closing spotify')
                os.system('TASKKILL /F /IM Spotify.exe')

                # speaking that the spotify  is closed
                speak("the spotify is closed")

            elif 'qbittorrent' in query or 'bittorrent' in query or 'torrent' in query:

                sp('closing qbittorrent')
                os.system('TASKKILL /F /IM qbittorrent.exe')

                # speaking that the qbittorrent  is closed
                speak("the qbittorrent is closed")

            elif 'vs code' in query:
                sp('closing vs code')
                os.system('TASKKILL /F /IM code.exe')

            elif 'github desktop' in query:
                sp('closing github desktop')
                os.system('TASKKILL /F /IM GitHubDesktop.exe')

            elif 'telegram' in query:
                sp('closing telegram')
                os.system('TASKKILL /F /IM Telegram.exe')

            elif 'whatsapp' in query:
                sp('closing whatsapp')
                os.system('TASKKILL /F /IM WhatsApp.exe')

            elif 'explorer' in query:
                sp('closing explorer')
                os.system('TASKKILL /F /IM explorer.exe')

            elif 'notepad' in query:
                sp('closing notepad')
                os.system('TASKKILL /F /IM notepad.exe')
            # all the office apps should be closed before closing the office

            # microsoft word
            elif 'word' in query:
                sp('closing word')
                os.system('TASKKILL /F /IM WINWORD.EXE')

            # writing code to close microsoft excel if microsoft excel is open and exists in query
            elif 'excel' in query:
                sp('closing excel')
                os.system('TASKKILL /F /IM EXCEL.EXE')

            # writing code to close microsoft powerpoint if microsoft powerpoint is open and exists in query
            elif 'powerpoint' in query:
                sp('closing powerpoint')
                os.system('TASKKILL /F /IM POWERPNT.EXE')

            # writing code to close microsoft outlook if microsoft outlook is open and exists in query
            elif 'outlook' in query:
                sp('closing outlook')
                os.system('TASKKILL /F /IM OUTLOOK.EXE')

            # writing code to close microsoft onenote if microsoft onenote is open and exists in query
            elif 'onenote' in query:
                sp('closing onenote')
                os.system('TASKKILL /F /IM ONENOTE.EXE')

            # writing code to close microsoft onedrive if microsoft onedrive is open and exists in query
            elif 'onedrive' in query:
                sp('closing onedrive')
                os.system('TASKKILL /F /IM OneDrive.exe')

            # writing code to close microsoft store if microsoft store is open and exists in query
            elif 'store' in query:
                sp('closing store')
                os.system('TASKKILL /F /IM STORE.EXE')

            # writing code to close microsoft office if microsoft office is open and exists in query
            elif 'office' in query:
                sp('closing office')
                os.system('TASKKILL /F /IM MICROSOFT.EXE')

            # writing code to close microsoft teams if microsoft teams is open and exists in query
            elif 'teams' in query:
                sp('closing teams')
                os.system('TASKKILL /F /IM Teams.exe')

            # writing code to close skype if skype is open and exists in query
            elif 'skype' in query:
                sp('closing skype')
                os.system('TASKKILL /F /IM skype.exe')

            # writing code to close microsoft edge if microsoft edge is open and exists in query\
            elif 'edge' in query:
                sp('closing edge')
                os.system('TASKKILL /F /IM msedge.exe')

            else:
                sp('Sorry, I could not find that')
                sp('what you want to close')

        elif "what is your name" in query:

            speak("My name is Olivia")

        elif "what is your age" in query:

            speak("I am a computer program")

        elif "what is your job" in query:

            speak("I have no job, Helping you is my hobby")

        elif "what is your favorite food" in query:

            speak("I Like renewable electricity")

        elif "what is your favorite animal" in query:

            speak("I like dogs")

        elif "what is your favorite sport" in query:

            speak("I like cricket")

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

        elif "what is Your dream" in query:

            speak("My dream is to be the most influential person in the world")

        elif "thank you" in query:

            speak("Welcome Sir")

        elif "who are you" in query:

            speak("I am a Virtual assistant")

        elif "who made you" in query:

            speak("I was created by Chirag singhal")

        elif "who is your creator" in query:

            speak("I was created by Chirag singhal")

        elif "what is your country of origin" in query:

            speak("I was made in India")

        elif "what is your language" in query:

            speak("I am a computer program")

        elif "what is your purpose" in query:

            speak("I am here to make your life easier")

        elif "is programming hard" in query:

            speak("You will have to discover this secretly")

        elif query == "hello" or query == "hi" or query == "hey" or query == "hii":

            speak("Hello Sir")  # Hello Sir

            wishMe()

        elif 'how are you' in query:

            speak("i am fine")

        elif 'what time is it' in query:

            speak(ctime())

        elif 'who are you' in query:

            speak("i am olivia")

        elif 'the time' in query:

            strTime = datetime.datetime.now().strftime("%H:%M:%S")

            speak(f"Sir, the time is {strTime}")

        elif 'kill me' in query:

            sp("I won't")

        elif 'your god' in query:

            sp("chriag singhal is my god")

        elif "who made you" in query or "who created you" in query or "who discovered you" in query:

            speak("I was built by Chirag singhal")

        elif "who is your creator" in query or "who is your developer" in query:

            speak("Chirag singhal is my creator")

        elif "do you eat" in query:

            speak("I do not eat, I get my energy from answering your questions")

        elif "do you like" in query:

            speak("I like to answer your questions")

        elif "what is special about oliva" in query:

            speak("I try to be as helpful as possible")

        elif 'what' in query and 'do' in query and 'can' in query:

            ans = """I can do lots of things, for example you can ask me time, date,
            I can open websites, play music, play videos, play games 
            I can tell you about anything you want to know, I can search on google for you,
            I can tell you about the weather, I can tell you about the news of the day,
            I can tell you the meaning of a word, I can open apps on your computer,
            I can tell you the current temperature,
            I can play music for you, I can search for things on wikipedia and many more things"""

            print(ans)
            speak(ans)

        elif 'wish me' in query:

            wishMe()

        # if the query contains 'tell me about (something)', then return the information of that person/organisation from the wikipedia using the information from the wikipedia library
        elif 'tell me about' in query or 'who is' in query:

            # remove the stop words from the query
            query = query.replace("tell me about", "")
            query = query.replace("who is", "")
            query = query.replace("what is", "")
            query = query.strip()

            try:

                # assign the query to a variable named as topic
                topic = query

                # search for the topic on wikipedia
                results = wikipedia.summary(topic, sentences=2)

                # speak the Accoridng to wikipedia
                speak("According to Wikipedia")

                # print the result
                print(results)

                # speak the result
                speak(results)

            except:

                # if the wikipedia does not have the query, then search for the query in the internet
                print("I can not find any information about " + query)
                sp("Searching on the internet")
                query = query.replace(" ", "+")
                url = "https://www.google.com/search?q=" + query
                webbrowser.get().open(url)

        # if the query contains 'what is' then return the information of that person/organisation from the wikipedia using the information from the wikipedia library
        elif 'what is' in query:

            # remove the stop words from the query
            query = query.replace("what is", "")
            query = query.replace("about", "")
            query = query.strip()

            if 'news' in query:

                # remove the stop words from the query
                query = query.replace("news", "")

                # assign the query to a variable named as topic
                topic = query

                # search for the topic on google news
                url = "https://news.google.com/search?q=" + topic

                # open the url in the default browser
                webbrowser.get().open(url)

            else:

                try:

                    # speak('Searching Wikipedia...')
                    sp("Searching Wikipedia...")

                    # assign the query to a variable named as topic
                    topic = query

                    # search for the topic on wikipedia

                    results = wikipedia.summary(topic, sentences=2)

                    # speak the Accoridng to wikipedia

                    speak("According to Wikipedia")

                    # print the result

                    print(results)

                    # speak the result

                    speak(results)

                except:

                    # if the wikipedia does not have the query, then search for the query in the internet
                    print("I can not find any information about " + query)
                    sp("Searching on the internet")
                    query = query.replace(" ", "+")
                    url = "https://www.google.com/search?q=" + query
                    webbrowser.get().open(url)

        # if the query contains how to (something) then search something on google and open it

        elif 'how to' in query:

            # remove the stop words from the query
            query = query.replace("how to", "")
            query = query.strip()

            # search for the query in google
            url = "https://www.google.com/search?q=" + query
            webbrowser.get().open(url)

            # speak the result
            speak("Here is what i found")

        elif 'weather in' in query:

            # remove the stop words from the query
            query = query.strip()

            # search for the query in google
            url = "https://www.google.com/search?q=" + query
            webbrowser.get().open(url)

            # speak the result
            speak("Here is what i found")

        elif 'news' in query and 'latest' in query:

            NewsFromBBC()
        # else:
        #     if query != 'none':
        #         webbrowser.open(
        #             f"https://www.google.com/search?q={query}&sourceid=olivia")

        #     #     sp("Sorry, I could not do that")
        #     #     sp("Please try again")

            # # print("else statement is executed")
            # # writing code for the queries or the commands that are not in the above list of commands. so we will ask the user
            # # if he or she wants to search the query in google or wikipedia or translate the query or open the query in browser
            # # or open the query in youtube or open the query in stackoverflow or open the query in github or open the query in
            # # facebook or open the query in instagram or open the query in twitter or open the query in linkedin or open the query in
            # # gmail or open the query in whatsapp or open the query in skype or open the query in snapchat or open the query in
            # # pinterest or open the query in tinder or open the query in reddit or open the query in quora or open the query in
            # # stackoverflow or open the query in amazon or open the query in flipkart or open the query in gmail or open the query in
            # # yahoo or open the query in google or open the query in wikipedia or open the query in youtube or open the query in
            # # stackoverflow or open the query in github or open the query in facebook or open the query in instagram or open the
            # # query in twitter or open the query in linkedin or open the query in gmail or open the query in whatsapp or open the
            # # query in skype or open the query in snapchat or open the query in pinterest or open the query in tinder or open the
            # # query in reddit or open the query in quora or open the query in stackoverflow or open the query in amazon or open the
            # # query in flipkart or open the query in gmail or open the query in yahoo or open the query in google or open the query in
            # # wikipedia or open the query in youtube or open the query in stackoverflow or open the query in github or open the query
            # # in facebook or open the query in instagram or open the query in twitter or open the query in linkedin or open the query
            # # in gmail or open the query in whatsapp or open the query in skype or open the query in snapchat or open the query in
            # # pinterest or open the query in tinder or open the query in reddit or open the query in quora or open the query in
            # # stackoverflow or open the query in amazon or open the query in flipkart or open the query in gmail or open the query
            # # in yahoo or open the query in google or open the query in wikipedia or open the query in youtube or open the query in
            # # stackoverflow or open the query in github or open the query in facebook or open the query in instagram or open the query
            # # in twitter or open the query in linkedin or open the query in gmail or open the query in whatsapp or open the query in
            # # skype or open the query in snapchat or open the query in pinterest or open the query in tinder or open the query in
            # if query != 'none':
            #     speak(
            #         'sorry sir that is not assigned. do you want to search for ' + query + '?')
            #     print('\n')
            #     # asking the user to confirm the query or not
            #     print('say yes or no. normal command will not work.')
            #     print('\n')

            #     confirmation = takeCommand().lower()  # taking the input from the user
            #     # if the user says yes or yep or something similar then we will search the query in google
            #     if 'yes' in confirmation or 'yep' in confirmation or 'sure' in confirmation or 'yeah' in confirmation or 'absolutely' in confirmation or 'fine' in confirmation or 'looks good' in confirmation or 'okay' in confirmation:
            #         print('\n')
            #         # asking the user to search in which website
            #         speak(
            #             'do you want me to search in google, wikipedia or youtube sir?')
            #         # taking the input from the user and converting it to lower case and storing it in answer4
            #         answer4 = takeCommand().lower()

            #         # if the user says google then we will search the query in google
            #         if 'google' in answer4:
            #             # telling the user that we are searching the query in google
            #             speak('searching for ' + query + ' in google')
            #             # opening the query in google
            #             webbrowser.open('www.google.com/search?gx&q=' + query)
            #         # if the user says wikipedia then we will search the query in wikipedia
            #         elif 'Wikipedia' in answer4:
            #             # asking the user to narrate or open the webpage
            #             speak('do you want me to narrate or open webpage sir?')
            #             # taking the input from the user and converting it to lower case and storing it in answer2
            #             answer2 = takeCommand().lower()

            #             # if the user says narrate or direct then we will narrate the query
            #             if 'narrate' in answer2 or 'direct' in answer2:
            #                 # getting the summary of the query
            #                 results = wikipedia.summary(
            #                     query, sentences=1, auto_suggest=False)
            #                 # narrating the summary of the query
            #                 speak('according to wikipedia ' + results)
            #             # if the user says web page or website or webpage then we will open the query in browser
            #             elif 'web page' in answer2 or 'website' in answer2 or 'webpage' in answer2:
            #                 # getting the page of the query
            #                 page1 = wikipedia.page(query, auto_suggest=False)
            #                 print(page1)  # printing the page of the query
            #                 page2 = page1.url  # getting the url of the query
            #                 print(page2)  # printing the url of the query
            #                 # telling the user that we are redirecting to the webpage
            #                 speak('redirecting to webpage')
            #                 webbrowser.get().open_new_tab(page2)  # opening the webpage of the query
            #                 print(page2)  # printing the url of the query
            #         elif 'youtube' in answer4:  # if the user says youtube then we will search the query in youtube
            #             # telling the user that we are searching the query in youtube
            #             speak('searching for ' + query + 'in youtube')
            #             webbrowser.get().open_new_tab('https://www.youtube.com/results?search_query=' +
            #                                           query)  # opening the query in youtube

            #         elif 'stackoverflow' in answer4:  # if the user says stackoverflow then we will search the query in stackoverflow
            #             # telling the user that we are searching the query in stackoverflow
            #             speak('searching for ' + query + 'in stackoverflow')
            #             webbrowser.get().open_new_tab(
            #                 'https://stackoverflow.com/search?q=' + query)  # opening the query in stackoverflow

            #     elif 'no' in query or 'not' in query or 'negative' in query:

            #         # asking the user if he wants to get rick rolled
            #         speak('do you want to get rick rolled sir?')
            #         # taking the input from the user and converting it to lower case and storing it in answer5
            #         answer5 = takeCommand().lower()

            #         # if the user says yes or yep or something similar then we will get rick rolled

            #         if 'yes' in answer5 or 'yep' in answer5 or 'sure' in answer5 or 'yeah' in answer5 or 'absolutely' in answer5 or 'fine' in answer5 or 'looks good' in answer5 or 'okay' in answer5:
            #             # telling the user that we are rick rolling
            #             speak('sir i am rick rolling you')

            #             # opening the rick roll video in the browser
            #             webbrowser.get().open_new_tab(
            #                 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')

            #             speak('sir i am rick rolling you')
            #             # opening the rick roll video in the browser

            #     else:

            #         # Asking user if he or she want olivia to do anything else.
            #         speak('ok. anything else sir?')
