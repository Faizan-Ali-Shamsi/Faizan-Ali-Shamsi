import speech_recognition as sr
from sele import webdriver

class Voice:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.listen_on_mic()

    def listen_on_mic(self):
        while True:
            try:
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = self.recognizer.listen(source)
                    command = self.recognizer.recognize_google(audio).lower()
                    print(f"You said: {command}")

                    if "search" in command:
                        query = command.split("search ", 1)[-1]
                        print(f"Searching for: {query}")
                        driver = webdriver.Chrome()
                        driver.get(f"https://www.google.com/search?q={query}")

            except sr.UnknownValueError:
                print("Sorry, I could not understand. Please try again.")

# Start the listener
listener = Voice()