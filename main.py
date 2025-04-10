import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
from gtts import gTTS
import pygame
import os

# Initial setups
recognizer = sr.Recognizer()
newsapi = "4105362f7d4e4473ba1e8c186e7d810c"

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')
    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
    response = requests.get(url)
    if response.status_code == 200:
        articles = response.json().get('articles', [])
        for i, article in enumerate(articles[:5]):  # limit to 5 headlines
            speak(f"News {i+1}: {article['title']}")
    else:
        speak("Sorry, I could not fetch news right now.")

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")
    elif c.startswith("play"):
        song = c.split("play", 1)[1].strip()
        link = musiclibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")
    elif "news" in c:
        fetch_news()
    elif "how are you" in c:
        speak("I'm great! How can I help you?")
    elif "your name" in c:
        speak("I'm Nova, your personal voice assistant.")
    elif "stop" in c or "exit" in c:
        speak("Shutting down Nova. Goodbye!")
        exit()
    else:
        speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    speak("Nova Initializing...")

    while True:
        try:
            print("Listening for wake word...")
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                word = recognizer.recognize_google(audio)
                if word.lower() == "hello":
                    speak("Ya")
                    with sr.Microphone() as source:
                        print("Nova Active...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
        except Exception as e:
            print(f"Error: {e}")
