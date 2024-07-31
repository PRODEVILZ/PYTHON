






import pyttsx3
import pyautogui
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random
import time




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
   engine.say(audio)
   engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    speak("Hello,Gautam Sir")
    if hour>=0 and hour<12:
        speak("Good Morning ")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    else:
        speak("Good Evening")
    
    speak("I am    anny . Please tell me how can I assist you")

def takeCommand():
    
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gautamchoudhary983@gmail.com','sjjgnioobibvokzu')
    server.sendmail('gautamchoudhary983@gmail.com',to,content)
    server.close()
    
    

if __name__ == "__main__":




  
  to='gautamc458@gmail.com'
  a=random.randint(1000,9999)
  a=str(a)
  content='chapiee log in OTP = ' + a 
  sendEmail(to,content)
  speak("check your email,sir")
  time.sleep(5)
  speak("say passcode,sir")
  otp=takeCommand()
  otp=otp.replace(" ","")

  if a==otp:

      wishMe()


      while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            
            speak('searching wikipedia... ')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'shutdown' in query:
            os.system('shutdown -s')

        elif 'open google' in query:
            webbrowser.opne("google.com")
        
        elif 'are you listening' in query:
            speak('yes,sir  always in your service')
        
        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        
        elif 'play music' in query:
            music_dir ='C:\\Users\\KALATRI\\Desktop\\python\\music'
            songs = os.listdir(music_dir)
            print(songs)
            b=0
            os.startfile(os.path.join(music_dir, songs[b]))
        
        elif 'next music' in query:
            music_dir ='C:\\Users\\KALATRI\\Desktop\\python\\music'
            songs = os.listdir(music_dir)
            b=b+1
            print(songs)
            os.startfile(os.path.join(music_dir, songs[b]))
        
        elif 'previous music' in query:
            music_dir ='C:\\Users\\KALATRI\\Desktop\\python\\music'
            songs = os.listdir(music_dir)
            b=b-1
            print(songs)
            os.startfile(os.path.join(music_dir, songs[b]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
         
        elif 'thank you ' in query:
             speak("not mind,Sir")
        
        elif '10 + volume' in query:
            pyautogui.press("volumeup",5)

        elif '25 + volume' in query:
            pyautogui.press("volumeup",15)

        elif '50 + volume' in query:
            pyautogui.press("volumeup",20)

        elif '10 - volume' in query:
            pyautogui.press("volumedown",5)

        elif '25 - volume' in query:
            pyautogui.press("volumedown",15)
        
        elif '50 - volume' in query:
            pyautogui.press("volumedown",25)
        
        elif 'full volume' in query:
            pyautogui.press("volumeup",100)

        elif 'mute' in query:
            pyautogui.press("volumedown",100)
       

        elif 'hello ' in query:
             speak("hello  Sir      is that anything I can do for you")

        
        elif 'open code ' in query:
             codePath = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
             os.startfile(codePath)

        elif 'send a email' in query:
    
             speak("who do you want to send")
             to=takeCommand()
             to=to.replace(" ","")
             to=to.lower()
             speak("What should I say")
             content = takeCommand()
             
             sendEmail(to,content)
             speak("Email has been sent!")
  else:
    speak("wrong password")
    x=2

speak("unauthrized identification")
        
              


             
    
       
         
         
        
        
        
        

        



    
