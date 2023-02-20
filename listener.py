import pyaudio
import wave
from datetime import datetime


class Recorder:

    def __init__(self):
        self.dev_index = 1
        self.CHUNK = 1024
        self.FORMAT = pyaudio.paInt16
        self.CHANNELS = 2
        self.RATE = 44100
        self.RECORD_SECONDS = 10
        self.WAVE_OUTPUT_FILENAME = ""
        self.output_directory = "./pending/"
        self.p = pyaudio.PyAudio()

    def get_devices(self):
        for i in range(self.p.get_device_count()):
            print(self.p.get_device_info_by_index(i))

    def record(self):

        try:
            stream = self.p.open(format=self.FORMAT,
                            channels=self.CHANNELS,
                            rate=self.RATE,
                            input=True,
                            input_device_index=self.dev_index,
                            frames_per_buffer=self.CHUNK)
            print("* recording")
            frames = []
            for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
                data = stream.read(self.CHUNK)
                frames.append(data)
            print("* done recording")
            stream.stop_stream()
            stream.close()
            self.p.terminate()


            now = datetime.now()
            current_time = now.strftime("%d_%m_%Y_%H_%M_%S")
            self.WAVE_OUTPUT_FILENAME = f"{current_time}.wav"

            output_path = self.output_directory + self.WAVE_OUTPUT_FILENAME

            wf = wave.open(output_path, 'wb')
            wf.setnchannels(self.CHANNELS)
            wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            wf.setframerate(self.RATE)
            wf.writeframes(b''.join(frames))
            wf.close()

        except Exception as err:
            print(err)


if __name__ == "__main__":

    while(True):
        recorder = Recorder()
        recorder.record()

