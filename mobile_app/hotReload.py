import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = subprocess.Popen(self.command, shell=True)

    def on_any_event(self, event):
        if event.src_path.endswith('.py') or event.src_path.endswith('.kv'):
            print(f"{event.src_path} changed. Restarting app...")
            self.process.terminate()
            self.process = subprocess.Popen(self.command, shell=True)

if __name__ == "__main__":
    # Command to run your main.py
    command = "python main.py"
    path = os.getcwd()
    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
