
import speech_recognition as sr
import pyttsx3
import os
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"🤖 {text}")
    engine.say(text)
    engine.runAndWait()

# Define apps to open
apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
}

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening for your command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"✅ You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Network error occurred.")
        return ""

def execute_command(command):
    for app_name in apps:
        if app_name in command:
            speak(f"Opening {app_name}")
            os.startfile(apps[app_name])
            return

    # If not an app, search on Chrome
    speak(f"Searching for {command}")
    search_url = f"https://www.google.com/search?q={command}"
    webbrowser.open(search_url)

if __name__ == "__main__":
    speak("Voice Shortcut App Started. Say something!")
    command = listen_command()
    if command:
        execute_command(command)
