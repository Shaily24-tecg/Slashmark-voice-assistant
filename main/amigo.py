import speech_recognition as sr
import asyncio
import edge_tts
import os
import webbrowser
import wikipedia
from playsound import playsound

VOICE = "en-US-AriaNeural"


# =========================
# TEXT TO SPEECH
# =========================
async def _speak(text):
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save("voice.mp3")


def speak(text):
    print("Amigo:", text)
    asyncio.run(_speak(text))
    playsound("voice.mp3")

    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")


# =========================
# SPEECH TO TEXT
# =========================
def take_command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=7)
        except:
            return None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said:", query)
        return query.lower()

    except:
        return None


# =========================
# YOUR COMMAND LOGIC (INTEGRATED)
# =========================
def process(query):

    if not query:
        speak("I did not understand")
        return

    if "wikipedia" in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak(result)

    elif "open youtube" in query:
        speak("Ok I am opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "open google" in query:
        speak("Ok I am opening Google")
        webbrowser.open("https://google.com")

    elif "open github" in query:
        speak("Ok I am opening GitHub")
        webbrowser.open("https://github.com")

    elif "open stackoverflow" in query:
        speak("Ok I am opening StackOverflow")
        webbrowser.open("https://stackoverflow.com")

    elif "who are you" in query:
        speak("I am Amigo, your voice assistant")

    elif "open whatsapp" in query:
        speak("Ok I am opening WhatsApp")
        path = "C:\\Users\\shail\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
        try:
            os.startfile(path)
        except:
            speak("WhatsApp not found")

    elif "exit" in query or "sleep" in query:
        speak("Ok I am shutting down")
        exit()

    else:
        speak("Command not recognized")


# =========================
# MAIN LOOP
# =========================
if __name__ == "__main__":

    print("\n **************************************************")   
    speak("Amigo assistant activated. Ready for commands.\n")

    while True:
        query = take_command()
        process(query)