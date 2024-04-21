import sys
import tkinter as tk
import threading
import speech_recognition
import pyttsx3 as tts
from openai_requests import get_chat_response

class Assistant:
    
    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.speaker = tts.init()
        self.speaker.setProperty('rate', 150)

        self.root = tk.Tk()
        self.label = tk.Label(text="🦜", font=('arial', 120, "bold"))
        self.label.pack()

        threading.Thread(target=self.start_listening).start()

        self.root.mainloop()

    def ai_response(self, text):
        response = get_chat_response(text)
        return response

    def start_listening(self):
        while True:
            try:
                with speech_recognition.Microphone() as mic:
                    self.recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                    audio = self.recognizer.listen(mic)

                    text = self.recognizer.recognize_google(audio)
                    text = text.lower()
                    print(text)

                    if "hey beetroot" in text:
                        self.label.config(fg="green")
                        self.handle_input(mic)
            except Exception as e:
                print("Error:", e)
                self.label.config(fg="red")
                continue

    def handle_input(self, mic):
        while True:
            try:
                audio = self.recognizer.listen(mic)
                text = self.recognizer.recognize_google(audio)
                text = text.lower()
                print(text)

                if text == "stop":
                    self.speaker.say("Goodbye")
                    self.speaker.runAndWait()
                    self.speaker.stop()
                    self.root.destroy()
                    sys.exit()
                else:
                    response = self.ai_response(text)
                    print(response)
                    self.speaker.say(response)
                    self.speaker.runAndWait()
                    self.label.config(fg="black")

            except Exception as e:
                print("Error:", e)
                self.label.config(fg="red")
                continue

Assistant()
