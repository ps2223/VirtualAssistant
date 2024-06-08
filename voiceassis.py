import pyttsx3 # It  helps to fetch system voice
import speech_recognition as sr # It helps to fetch our voice with he help of Microphone
import datetime # To fetch Date & Time
from datetime import date
import wikipedia # To fetch Wikipedia from google
import webbrowser # It helps to oprate web browser
from pywikihow import search_wikihow # It helps to search in google and gives step by step answers
import pyautogui # It helps to control Mouse,Keyboard and other peripherial devices that are connected to system
import cv2 # It helps to Access Camera of the system

engine= pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def say(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# To Greet According to Time with the help of greet module
    
    
def greet():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        say("Good Morning!")

    elif hour>=12 and hour<16:
        say("Good Afternoon!")

    else:
        say("Good Evening!")

    say("This is Kratos desktop assistant. You can use me by voice commands without using mouse and keyboard.")


def takeCommand():
    # it Take Microphone input and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,8)
        r.adjust_for_ambient_noise(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said: {query}\n")

    except Exception as e:
        say("Could you please repeat. I didn't get that.")
        return "None"
    return query
 
# The main file where the code execution takes place

if __name__ == "__main__":
    greet()
    while True:
       query = takeCommand().lower()
       
       # Logic for Executing Tasks based on Query 
       # To search in wikipedia by importing wikipedia module

       if 'wikipedia'in query:
           say('Searching Wikipedia...')
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query, sentences=3)
           say("According to Wikipedia")
           say(results)
     
       # Opening Web Application with the help of webbrowser module

       elif 'open youtube' in query:
           say("opening Youtube")
           webbrowser.open("https://www.youtube.com/")

       elif 'open google' in query:
           try:
               say("Sir, What should I search on Google")
               cm = takeCommand().lower()
               webbrowser.open(f"{cm}")
               say("Showing Results on Google")
           except Exception as e:
               say("Sorry Sir, I could not able to find this")

       elif 'open instagram' in query:
           say("opening instagram") 
           webbrowser.open("instagram.com")

       elif 'open Github' in query:
                say("opening Git Hub") 
                webbrowser.open("github.com")

       elif 'open twitter' in query:
           say("opening twitter") 
           webbrowser.open("twitter.com")

       elif 'open geeks for geeks' in query:
            say("openiing geeks for geeks")
            webbrowser.open("geeksforgeeks.org")


       # To Check time     

       elif 'the time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S") 
           say(f"Sir, the time is {strTime}")
        
       elif ' the date' in query:
           tdate =  date.today()
           say(f"Sir, the date is {tdate}")

       # To open camera    

       elif 'open camera' in query:
           say ("Opening camera")
           cap = cv2.VideoCapture(0)
           while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

           cap.release()
           cv2.destroyAllWindows()      

       # System Volume Control            

       elif 'increase the volume' in query:
           say("Increasing volume")
           pyautogui.press("volumeup")

       elif  "lower the volume" in query:
           say("Decreasing volume")
           pyautogui.press("volumedown")

       elif 'mute' in query:
           say("System sound has muted")
           pyautogui.press("volumemute")

       elif 'unmute' in query:
            say("System sound is unmuted")
            pyautogui.press("volumeunmute")            


       # To check battery percentage with help of psutil module   
            
       elif "what is the battery percentage" in query:
           import psutil # this module helps to check percentage in battery
           battery = psutil.sensors_battery()
           percentage = battery.percent
           say(f"Sir, your system have {percentage} percent battery left")
           if percentage>=75:
               say("Ample battery percentage.")
           elif percentage>40 and percentage<=75:
               say("Battery percentage is decent.")
           elif percentage<=15 and percentage<=30:
               say("Battery percentage is low, Please connect a charger.")
           elif percentage<=15:
               say("Connect to the charger or your pc will be shut down.")

        # To End a Program 
                                 
       elif 'exit' in query:
           say("Take care. Until we meet again")
           break             
  

                
