import speech_recognition as sp
import webbrowser
import pyttsx3

recognizer=sp.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
if __name__ == "__main__":
    speak("Hey sir how may I help you")
