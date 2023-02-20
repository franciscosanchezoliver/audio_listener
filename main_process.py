import logging
import threading
import time
from files_handler import FilesHandler
from listener import Recorder

def files_handler_thread(name):
    audio_path = './pending'
    files_handler = FilesHandler(audio_path=audio_path, text_output_path='./text')
    files_handler.run()

def listener_thread(name):
    while(True):
        recorder = Recorder()
        recorder.record()


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    listener_t = threading.Thread(target=listener_thread, args=(1,))
    files_handler_thread = threading.Thread(target=files_handler_thread, args=(1,))

    listener_t.start()
    files_handler_thread.start()



    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")