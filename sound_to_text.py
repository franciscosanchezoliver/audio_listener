import speech_recognition as sr
from datetime import datetime


class TextTranscriber:

    def __init__(self, path_export):
        self.path_export = path_export

    def transcribe(self, file_path):
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")

            # initialize the recognizer
            r = sr.Recognizer()

            # open the file
            with sr.AudioFile(file_path) as source:
                audio_data = r.record(source)
                # Convert from speech to text
                text = r.recognize_google(audio_data)
                text = str(text)
                text = current_time + ";" + text + "\n"
                return text
        except:
            print("Something wrong ocurred while transcribing")
            return ""




