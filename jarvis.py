import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import sys
import pyjokes
import requests
from requests import get
import pyautogui
from bs4 import BeautifulSoup
import pywikihow
from pywikihow import search_wikihow
import psutil
import speedtest
from PIL import Image
import keyboard
import time
# from newsapi import base_news


# from newsapi import NewsApiClient
# from key import my_api_key

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)
# engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    startTime = datetime.datetime.now().strftime("%H:%M")
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print(f"Good Morning Boss, its {startTime}")
        speak(f"Good Morning boss, its {startTime}")

    elif hour>=12 and hour<18:
        print(f"Good afternoon Boss, its {startTime}")
        speak(f"Good afternoon boss, its {startTime}")

    else:
        print(f"Good Evening Boss, its {startTime}")
        speak(f"Good Evening boss, its {startTime}")

    # print(f"Boss the time is {startTime}")
    # speak(f"Boss the time is {startTime}")

    print("I am online and here to help you boss")
    speak("I am online and here to help you boss")

def takecommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"Boss said : {query}\n")

    except Exception as e:
        print("Boss, I did not get that. Sorry")
        speak("Boss, I did not get that, sorry")
    
        print("\n")
        return "None"
    return query

#news {Function}

def news():
    main_url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=API_KEY=e93c526a7fbd4b26a6c9e20a025ff698"

    main_page = requests.get(main_url).json()
    articles = main_page["article"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        speak(f"today's {day[1]} news is : {head[1]}")

def logoff():

    import pyautogui

    pyautogui.press('win')
    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.press('right')

    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')
    pyautogui.press('up')

    pyautogui.press('enter')

def shut():
    import pyautogui

    pyautogui.press('win')
    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.press('enter')


# def sendEmail(to, content):


if __name__ == "__main__":
    wishMe()

    while True:
        query = takecommand().lower()
        # email to anil
        if "email to anil" in query:
            try:
                print("What should I say him?")
                speak("what should I say him")
                content = takecommand()
                to = "kumaranil66563@gmail.com"
                # sendEmail(to, content)
                print("Boss I have successfully sent the email")
                speak("boss I have successfully sent the email")
            except Exception as e:
                print("Boss I was unable to send this email as you did not define send email function yet")
                speak("Boss I was Sorry boss, I did not understand this to send this email as you did not define send email function yet")

        # Hello, hi, hlo, good morning, night, evening
        elif "hello" in query:
            print("Hello boss, how are you?")
            speak("Hello boss, how are you")

        elif "i am fine" in query:
            print("Good to hear!")
            speak("Good to hear")

        # elif "hi" in query:
        #     print("Hi boss, how are you?")
        #     speak("hi boss, how are you")

        elif "hlo" in query:
            print("Hello boss, how are you?")
            speak("Hello boss, how are you")

        elif "how are you" in query:
            print("I am fine boss, how are you?")
            speak("I am fine boss, how are you")

        elif "good" in query:
            print("Good to hear from you, Boss")
            speak("Good to hear from you, Boss")

        elif "morning" in query:
            print("Good morning, boss")
            speak("Good morning, boss")
            print("\n")

        elif "afternoon" in query:
            print("Good afternoon, boss")
            speak("Good afternoon, boss")

        elif "evening" in query:
            print("Good evening, boss")
            speak("Good evening, boss")

        elif "night" in query:
            print("Good night, boss")
            speak("Good night, boss")

        # Time
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            print(f"Boss the time is {strTime}")
            speak(f"Boss the time is {strTime}")
        
        # Searching WikiPedia
        elif 'wikipedia' in query:
            print("Searching Wikipedia...")
            speak("Searching Wikipedia...")

            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            
            print("According to Wikipedia - ")
            speak("According to Wikipedia")

            print(results)
            speak(results)

        # Openning links

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "play song in youtube" in query:
            webbrowser.open("https://www.youtube.com/watch?v=MFtMUBVcM0U")

        elif "open ts factories" in query:
            webbrowser.open("https://tsfactories.cgg.gov.in/")

        # opening Whats App
        elif "open whatsapp" in query:
            webbrowser.open("https://web.whatsapp.com")

        # opening Amazon
        elif "open amazon" in query:
            webbrowser.open("https://amazon.in")

        # opening Flipkart
        elif "open flipkart" in query:
            webbrowser.open("https://flipkart.com")

        # opening srikaram
        elif "open sreekaram" in query:
            webbrowser.open("https://www.zee5.com/tvshows/details/srikaram-shubhakaram/0-6-42")

        elif "open srikaram" in query:
            webbrowser.open("https://www.zee5.com/tvshows/details/srikaram-shubhakaram/0-6-42")

        # searching on youtube
        elif "search on youtube" in query:
            print("Boss, what Should I search for you?")
            speak("Boss, what Should I search for you")
            yy = takecommand().lower()
            webbrowser.open(f"https://www.youtube.com/results?search_query={yy}")

        # searching on google
        elif "search on google" in query:
            print("Boss, what Should I search for you?")
            speak("Boss, what Should I search for you")
            gg = takecommand().lower()
            webbrowser.open(f"{gg}")

        elif "Download app" in query:
            print("Boss, what Should I download for you")
            speak("Boss, what Should I download for you")
            dd = takecommand().lower()
            webbrowser.open(f"https://www.google.com/search?q={dd}")

        # Local automation

        elif "initiate security" in query:
            from security import cam
            cam()

        elif "security camera" in query:
            from security import cam
            cam()

        elif "start monitoring" in query:
            from security import cam
            cam()

        elif "monitor this area" in query:
            from security import cam
            cam()

        elif "lock" in query:
            logoff()

        elif "log off" in query:
            logoff()

        elif "someone" in query:
            logoff()


        # ------------------------------------------------------

        elif "shutdown" in query:
            shut()

        elif "turn off" in query:
            shut()

        elif "power off" in query:
            shut()

        elif "show me all iron man suits" in query:
            m1 = Image.open(r'E:\My down\iron man\mark-1.jpg')
            m1.show()
            speak("boss, This is Mark 1. I was not there at that time. But happy to be here with you now")

            time.sleep(2)

            m2  = Image.open(r'E:\My down\iron man\mark-2.jpg')
            m2.show()
            speak("boss, This is Mark 2. This was our first beautiful suit")

            time.sleep(2)

            m3 = Image.open(r"E:\My down\iron man\mark-3.png")
            m3.show()
            speak("boss, This is mark 3")

            time.sleep(2)

            m5 = Image.open(r"E:\My down\iron man\mark-5.png")
            m5.show()
            speak("boss, This is mark 5. Did you remember that scence when you first wore it. It was horrible fight with Ivan Vanko.")

            time.sleep(2)

            m6 = Image.open(r"E:\My down\iron man\mark-6.png")
            m6.show()
            speak("Boss, This is mark 6. This come to you automattically by checking the bracelets position")

            time.sleep(2)

            m10 = Image.open(r"E:\My down\iron man\mark-10.jpg")
            m10.show()
            speak("Boss, This is mark 10")

            time.sleep(2)

            m42 = Image.open(r"E:\My down\iron man\mark-42.jpg")
            m42.show()
            speak("boss, This is mark 42. This automatically comes to you.")

            time.sleep(2)

            m45 = Image.open(r"E:\My down\iron man\mark-45.jpg")
            m45.show()
            speak("Boss, This is mark 45. We fought with ultron using this suit. I tried to make him good but it was not possible.")

            time.sleep(2)

            m46 = Image.open(r"E:\My down\iron man\mark-46.jpg")
            m46.show()
            speak("Boss, This is mark 46. We fought with captain using this suit.")

            time.sleep(2)

            m47 = Image.open(r"E:\My down\iron man\mark-47.png")
            m47.show()
            speak("Boss, This is mark 47.")

            time.sleep(2)

            m50 = Image.open(r"E:\My down\iron man\mark-50.png")
            m50.show()
            speak("Boss, This is mark 50. It was built using nano tech. We fought with thanos first time with this suit.")

            time.sleep(2)

            m85 = Image.open(r"E:\My down\iron man\mark-85.jpg")
            m85.show()
            speak("Boss, This is mark 85. We defeated thanos with this suit.")

            time.sleep(2)
    
            speak("boss, Thats all on iron man")


        elif "play song" in query:
            music_dir = "G:\\Music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
        
        # Screen Recording
        elif "screen record" in query:
            print("Ok Boss, Screen Recording has been started")
            speak("Ok boss, screen Recording has been started")
            time.sleep(1)
            import screen_rec
            screen_rec.screen()

            break

        # Password Generator
        elif 'generate a password' in query:
            print("A Random Password for you is Being Generated")
            speak("A Random Password for you is Being Generated")
            time.sleep(1)
            from pass_generator import password
            its = password()
            print(its)

        # volume controlling
        elif "volume up" in query:
            print("Raising Volume")
            pyautogui.press("volumeup")

        elif "increase volume" in query:
            print("Raising Volume")
            pyautogui.press("volumeup")

        elif "decrease volume" in query:
            print("Lowering Volume")
            pyautogui.press("volumedown")

        elif "volume down" in query:
            print("Lowering Volume")
            pyautogui.press("volumedown")

        elif "mute audio" in query:
            print("Muted the audio")
            pyautogui.press("volumemute")

        # elif "unmute audio" in query:
        #     pyautogui.press("voulumemute")
        #     print("Unmuted audio")
        #     speak("Un muted audio")

        # switching windows
        elif "change window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            #time.sleep(1)
            pyautogui.keyUp("alt")

        #show desktop
        elif "show home" in query:
            keyboard.press_and_release('win+m')

        #mute mic
        elif "mute mic" in query:
            keyboard.press_and_release('Fn+f10')

        #close this
        elif "close this" in query:
            keyboard.press_and_release('alt+f4')

        #battery percent
        elif "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            print(f"Boss the battery percent on our system is {percentage}%")
            speak(f"Boss the battery percent on our system is {percentage} percent")

        #alarm
        elif "alarm" in query:
            print("Boss, please tell me at which time should I set alarm.")
            speak("Boss please tell me at which time should i set alarm")
            tt = takecommand()
            tt = tt.replace("set alarm at ", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            import MyAlarm
            MyAlarm.alarm(tt)

        # Opening apps

        elif "camera" in query:
            wcpath = "C:\\Program Files (x86)\\CyberLink\\YouCam\\YouCam.exe"
            os.startfile(wcpath)

        elif "open code" in query:
            vpath = "E:\\vs code\\Microsoft VS Code\\Code.exe"
            os.startfile(vpath)

        elif "open zoom" in query:
            zpath = "C:\\Users\\hp1\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zpath)

        elif "open calculator" in query:
            cpath = "C:\\Users\\hp1\\Desktop\\Calculator.lnk"
            os.startfile(cpath)

        elif "open command prompt" in query:
            os.system('start cmd')

        # Other tasks

        # Quotations
        # elif "tell me" in query:
        #     api = "https://api.quotable.io/random"
        #     quotes = []
        #     quote_number = 0

        #     def preload_quotes():
        #         global quotes

        #         print("**Loading**")
        #         for x in range(10):
        #             random_quote = requests.get(api).json()
        #             content = random_quote['content']
        #             author= random_quote['author']
        #             quote = content + "\n\n"+ "By " + author
        #             quote = random.choice(quote)
        #             quotes.append(quote)
        #             print(quote)
        #             speak(quote)

        #     preload_quotes()

            # def get_random_quote():
            #     # global quote
            #     rdj = random.choice(quote)
            #     print(rdj)
            #     speak(rdj)

            # get_random_quote()


        # Location
        elif "where am i" in query:
            print("Boss, check the location")
            speak("boss check the location")
            print("\n")
            # from delete import loc
            # loc()

        elif "where are we" in query:
            print("Boss, check the location")
            speak("boss check the location")
            print("\n")
            # from delete import loc
            # loc()
            
        # Find joke
        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)


        # Who made you
        elif "who made you" in query:
            print("I was made by Mr.Venkatesh in Aug, 2021")
            speak("I was made by, mister venkatesh in august, 2021")


        # Telling news
        elif "tell me news" in query:
            print("Please wait, fetching the latest news boss")
            speak("Please wait, fetching the latest news boss")
            news()

        # ip address
        # elif "ip address" in query:
        #     ip = get('https://api.ipify.org').text
        #     print("Your IP Address is", ip)
        #     speak(f"your ip adress is {ip}")

        # Temperature
        elif "weather" in query:
            search = "weather in hyderabad"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div",class_="BNeawe").text
            print(f"The temperature in Hyderabad is {temp}")
            speak(f"The temperature in Hyderabad is {temp}")

        # opening shopping
        elif "shopping" in query:
            import shopping
            print("Ok Boss, I've opened Shopping Sites for you")
            speak("Ok Boss, I've opened shopping sites for you")
            shopping()

        elif "shop" in query:
            import shopping
            print("Ok Boss, I've opened Shopping Sites for you")
            speak("Ok Boss, I've opened shopping sites for you")
            shopping()

        elif "I need essentials" in query:
            import shopping
            print("Ok Boss, I've opened Shopping Sites for you")
            speak("Ok Boss, I've opened shopping sites for you")
            shopping()

        elif "Groceries" in query:
            import shopping
            print("Ok Boss, I've opened Shopping Sites for you")
            speak("Ok Boss, I've opened shopping sites for you")
            shopping()

        # Covid cases


        # how to do mode
        elif "activate how to do mode" in query:
            print("Boss, how to do mode is activated.")
            speak("Boss, how to do mode is activated.")
            while True:
                print("Please tell me what you want to know.")
                speak("Please tell me what you want to know.")
                how = takecommand()
                try:
                    if "exit" in how:
                        print("Ok boss, how to do mode is closed")
                        speak("Ok boss, how to do mode is closed")
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to) == 1
                        how_to[0].print()
                        print(how_to[0].summary)
                        speak(how_to[0].summary)
                except Exception as e:
                    print("Sorry boss, I am not able to find this")
                    speak("Sorry boss, I am not able to find this")
        

        # internet speed
        elif "internet speed" in query:
            print("Boss, please wait I am checking the Internet Speed")
            speak("Boss please wait i am checking the Internet Speed")
            st = speedtest.Speedtest()
            dl = st.download()/1000000
            up = st.upload()/1000000
            print(f"Boss the downloading speed we have is ~ {int(dl)} mbps and the uploading speed we have is ~ {int(up)} mbps.")
            speak(f"Boss the downloading speed we have is approximately {int(dl)} mbps and the uploading speed we have is approximately {int(up) } mbps")


        # Closing 

        elif "bye" in query:
            print("Thank you Boss. Lets meet later. Bye! ")
            speak("Thank you Boss. Lets meet later. Bye! ")
            sys.exit()

        elif "quit" in query:
            print("Ok Bye")
            speak("Ok Bye Boss")
            sys.exit()


        # else:
        #     print("Boss I did not understand that. Sorry")
        #     speak("Boss I did not understand that. Sorry")
