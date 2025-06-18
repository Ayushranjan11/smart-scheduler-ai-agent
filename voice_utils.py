# voice_utils.py

import pyttsx3
import speech_recognition as sr

# Initialize TTS engine
engine = pyttsx3.init()

# Optional: adjust voice rate or volume
engine.setProperty('rate', 180)     # Speed (default ~200)
engine.setProperty('volume', 1.0)   # Max volume

def speak(text):
    print(f"🔊 Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"✅ Recognized: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand.")
        return ""
    except sr.RequestError:
        print("❌ API error.")
        return ""
