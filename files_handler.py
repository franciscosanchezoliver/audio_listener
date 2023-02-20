import os
import time
from sound_to_text import TextTranscriber
from datetime import datetime

class FilesHandler:

    def __init__(self, audio_path, text_output_path):
        self.audio_path = audio_path
        self.text_output_path = text_output_path
        self.text_transcriber = TextTranscriber(path_export=text_output_path)

    def check_if_there_are_files_to_process(self):
        there_are_files_to_process = os.path.isfile(self.audio_path)
        return there_are_files_to_process

    def save_text_into_file(self, text, day):
        output_path = self.text_output_path + "/" + day + ".txt"
        print("appending in " + output_path)
        file = open(output_path, "a")
        file.write(text)
        file.close()

    def get_files_in_path(self):
        files = os.listdir(self.audio_path)
        return files

    def run(self):
        while(True):
            files = self.get_files_in_path()

            if len(files) > 0 :
                for file in files:
                    text = self.text_transcriber.transcribe(self.audio_path + '/' + file)
                    day = file.split("/")[-1].split("_")[:3]
                    day = day[2]+day[1]+day[0]
                    self.save_text_into_file(text, day=day)

                    # remove file already transcribed
                    file_to_remove = self.audio_path + '/' + file
                    print("Removing file " + file_to_remove )
                    os.remove(file_to_remove)

            else:
                print("All processed. Waiting for more files")
                time.sleep(3)


if __name__ == "__main__":
    audio_path = './pending'
    files_handler = FilesHandler(audio_path=audio_path, text_output_path='./text')
    files_handler.run()



