import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import openai


# Initialize the speech recognizer
hear = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to speak a response
def say(text):
    engine.say(text)
    engine.runAndWait()

# Function to process voice commands
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print(f"User said: {query}")
            return query
        except Exception as e:
            return say("Some Error Occurred. Sorry from Kratos")
        

# Main Loop
if __name__ == "__main__":
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["Youtube","https://www.youtube.com"],["Instagram","https://www.instagram.com"],
               ["Google","https://www.google.com"],["facebook","https://www.facebook.com"],
               ["twitter","https://www.twitter.com"]]
        for site in sites:
            if f"open {site[0]}".lower() in query.lower():
                say (f"Opening {site[0]}")
                webbrowser.open(site[1])
            else:
                say("No such website in my access.")


        if "hello" in query.lower():
            say("Hello! How can I assist you?")
        elif "what is your name" in query.lower():
            say("My name is Kratos AI.")
        elif "goodbye" in query.lower():
            say("Goodbye!")
            exit()
        else:
            say("I'm not sure how to respond to that.")

                
        

        

    

# Main loop
'''while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            hear.adjust_for_ambient_noise(source)
            audio = hear.listen(source)
            print("Recognizing...")

        command = hear.recognize_google(audio)

        print(f"You said: {command}")

        process_command(command) 
    


    except sr.UnknownValueError:
        say("Sorry, I couldn't understand that.")

    except sr.RequestError as e:
        say(f"Request error: {e}")
    except KeyboardInterrupt:
        break'''

