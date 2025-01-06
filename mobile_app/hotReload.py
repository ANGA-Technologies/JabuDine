import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        self.process = None
        self.last_modified = 0  # For debouncing file changes

        self.start_process()

    def start_process(self):
        """Starts the application process."""
        if self.process:
            print("An existing process is already running, terminating it first.")
            self.stop_process()
        print("Starting application...")
        self.process = subprocess.Popen(self.command, shell=True)

    def stop_process(self):
        """Stops the application process."""
        if self.process:
            self.process.terminate()
            self.process.wait()  # Ensure the process fully terminates
            self.process = None
            print("Application process terminated.")

    def on_modified(self, event):
        """Handles file modifications to trigger a restart."""
        if event.src_path.endswith('.py') or event.src_path.endswith('.kv'):
            current_time = time.time()
            # Debounce: Ignore rapid consecutive events
            if current_time - self.last_modified < 1:  # 1 second debounce
                return
            self.last_modified = current_time

            print(f"Detected change in {event.src_path}. Restarting application...")
            self.start_process()

if __name__ == "__main__":
    command = "python main.py"  # Command to run your main application
    path = os.getcwd()          # Directory to watch

    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping observer and shutting down application...")
        observer.stop()
        event_handler.stop_process()  # Ensure the subprocess is terminated
    observer.join()
