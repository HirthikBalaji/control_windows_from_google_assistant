import glob
import os
import time
import pyttsx3
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import urllib.request
import re

# stopwords = set(stopwords.words('english'))
# print("Intialzing processes")

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voice = engine.getProperty("voices")
engine.setProperty("voice", str(voice[2].id))


# functions for basic input output and other functionalities

def speak(txt):
    print("WINDOWS: " + txt)
    engine.say(txt)
    engine.runAndWait()


path = "C:\\Users\\Hirthik Balaji\\Dropbox\\Apps\\Push2Run"

# make listen
try:
    while True:
        lst = os.listdir(path)
        if len(lst) != 0 and "Command.txt" in lst:
            time.sleep(3)
            with open(f"{path}\\Command.txt") as f:
                data = f.read()
            f.close()

            # natural language processing

            word_tokens = word_tokenize(data.lower())

            filtered_sentence = []
            stop_words = set(stopwords.words('english'))
            for w in word_tokens:
                if w not in stop_words:
                    w = w.lower()
                    filtered_sentence.append(w)
            s = (filtered_sentence)
            print(filtered_sentence)

            # opening applications applications

            if ("open" or "run" in s) and "calculator" in s:
                speak("Opening Calculator")
                os.system("calc")

            if ("open" or "run" in s) and "explorer" in s:
                speak("Opening file explorer")
                os.system("explorer")

            if ("open" or "run" in s) and "chrome" in s:
                speak("Opening Chrome")
                os.system("chrome")

            if ("open" or "run" in s) and ("microsoft store" in s) or ("open" and "store" in s) or ("install" in s):
                speak("Opening Microsoft store")
                os.system("start ms-windows-store:")

            if ("open" or "run" in s) and "command" in s:
                speak("opening command prompt")
                os.startfile("C:\\Windows\\System32\\cmd.exe")

            # for all installed programs

            all_apps = glob.glob("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\*.*")
            no_need = glob.glob("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\*.ini")
            app_name = []
            apps = list(set(all_apps).difference(set(no_need)))

            for i in range(len(apps)):
                app_name.append(apps[i].split("\\Programs\\")[1].lower().split(".")[0])

            for x in range(len(app_name)):
                if (app_name[x] in s):
                    speak("Opening " + app_name[x])
                    os.startfile('"' + apps[x] + '"')

            if "play" in data.lower():
                q = data.replace("play", "").replace(" ", '')
                html = urllib.request.urlopen(f"https://www.youtube.com/results?search_query={q}")
                video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
                link = "www.youtube.com/watch?v=" + video_ids[0]
                os.system("brave " + link)

            time.sleep(5)
            os.remove(path + "\\Command.txt")
except KeyboardInterrupt:
    try:
        if len(os.listdir(path)) != 0:
            os.remove(path + "\\Command.txt")
            print("keyboard pass created Aborting !!!")
    except:
        print("keyboard pass created Aborting !!!")
