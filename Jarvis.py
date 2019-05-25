import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, My loard")

    elif hour>=12 and hour<18:
        speak("Good Afternoon, My loard")

    else:
        speak("Good Evening, My loard")

    speak("I am Yashika and I am Baandri. Please tell me how may I help you")

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.energy_threshold=200 # for min. audio energy to consider for recording
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtplib.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("acemourya1@gamil.com", " password ")
    server.sendmail("acemourya1@gmail.com", to, content)
    server.close()

if __name__== "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", " ")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir= 'F:\\Ace\\Redmi Note 4\\Documents\\mivideo'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strtime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")

        elif 'open pubg' in query:
            codepath = "C:\\Program Files\\TxGameAssistant\\AppMarket\\AppMarket.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("What should I send? ")
                content = takeCommand()
                to = "yashikasharma789@gmail.com"
                sendEmail(to,content)
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                speak("Sorry my loard. I am not able to send this email ")


