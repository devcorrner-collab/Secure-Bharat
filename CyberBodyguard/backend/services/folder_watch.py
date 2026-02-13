import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SecureWatchHandler(FileSystemEventHandler):
    def __init__(self, callback):
        self.callback = callback
        # Sirf in extensions ko scan karna hai (Resource Efficient)
        self.target_extensions = ['.exe', '.msi', '.bat', '.zip', '.rar', '.pdf', '.docx', '.doc', 'com']

    def on_created(self, event):
        if event.is_directory:
            return

        filename = event.src_path.lower()
        
        # Temp files ignore karo
        if filename.endswith('.tmp') or filename.endswith('.crdownload'):
            return

        # Check karo ki ye file target list mein hai ya nahi
        is_target = any(filename.endswith(ext) for ext in self.target_extensions)
        
        if is_target:
            print(f"⚡ SecureBharat Monitor: New File Detected - {event.src_path}")
            time.sleep(1.5) # File write hone ka wait
            self.callback(event.src_path)

class FolderWatcher:
    def __init__(self, callback_func):
        self.watch_path = os.path.join(os.path.expanduser("~"), "Downloads")
        self.observer = Observer()
        self.handler = SecureWatchHandler(callback_func)

    def start(self):
        if os.path.exists(self.watch_path):
            self.observer.schedule(self.handler, self.watch_path, recursive=False)
            self.observer.start()
            print(f" SecureBharat Monitoring: {self.watch_path}")
        else:
            print(" Downloads folder not found.")

    def stop(self):
        self.observer.stop()
        self.observer.join()