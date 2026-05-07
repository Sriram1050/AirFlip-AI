import speech_recognition as sr
import re
class VoiceController:
    def __init__(self):
        self.recognizer = sr.Recognizer()
    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            try:
                audio = self.recognizer.listen(source, timeout=5)
                text = self.recognizer.recognize_google(audio)
                print("You said:", text)
                match = re.search(r'\d+', text)
                if match:
                    return int(match.group())
            except:
                return None
        return None