import speech_recognition as sr
import pyttsx3
from jarvis_core import processCommand

engine = pyttsx3.init()

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

recognizer = sr.Recognizer()

speak("Initializing Jarvis")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening for wake word...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source)

        word = recognizer.recognize_google(audio)

        if word.lower() == "jarvis":
            speak("How may I help you?")
            with sr.Microphone() as source:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio)

            response = processCommand(command)
            speak(response)

    except Exception as e:
        print("Error:", e)
