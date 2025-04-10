Title: Nova - Voice Activated AI Assistant

Nova is a smart voice-controlled virtual assistant developed using Python. It is capable of performing multiple tasks like web browsing, music playback, and reading out the latest news — all with simple voice commands.

This project is aimed at showcasing how voice interfaces can be integrated with real-time functionalities to create a basic yet practical assistant, similar to Alexa or Google Assistant.

Features:

• Voice recognition using the speech_recognition library
• Activated by the wake word "Hello"
• Converts text to speech using both pyttsx3 (offline) and gTTS with pygame (online playback)
• Opens websites like Google, YouTube, Facebook, and LinkedIn using voice commands
• Plays music through links stored in a custom music library module
• Fetches and reads out the latest headlines using NewsAPI
• Future-ready for OpenAI GPT integration to handle general queries

Technology Stack:

• Python
• Libraries used: speech_recognition, pyttsx3, gTTS, pygame, webbrowser, requests
• Future scope: Integration with openai for AI-powered answers

How to Run the Project:

1. Clone the project using Git
2. Install all required libraries using pip
3. Run the main Python file named nova.py
4. Make sure your microphone and speaker are working
5. You can say "Hello" to activate Nova and give any of the supported commands

Example commands:
– Open Google
– Open YouTube
– Play a song
– Read the news

Optional Future Enhancements:

• Integration with GPT models for smarter Q&A
• Addition of weather reports
• Sending emails through voice
• GUI interface using Tkinter or PyQt

Project Author:

Priyanshi Sharma
https://www.linkedin.com/in/priyanshi-sharma-b00167256/
