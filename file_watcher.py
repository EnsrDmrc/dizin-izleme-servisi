import os
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime

LOG_FILE = "/home/ubuntu/bsm/logs/changes.json"

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.log_change("modified", event)

    def on_created(self, event):
        self.log_change("created", event)

    def on_deleted(self, event):
        self.log_change("deleted", event)

    def log_change(self, action, event):
        change = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "path": event.src_path,
            "is_directory": event.is_directory
        }
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'w') as f:
                json.dump([], f)
        with open(LOG_FILE, 'r+') as f:
            data = json.load(f)
            data.append(change)
            f.seek(0)
            json.dump(data, f, indent=4)

if __name__ == "__main__":
    path = "/home/ubuntu/bsm/test"
    observer = Observer()
    event_handler = ChangeHandler()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    print(f"Monitoring changes in: {path}")
    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

