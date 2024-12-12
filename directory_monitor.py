import time
import json
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os

class DirectoryMonitor(FileSystemEventHandler):
    def __init__(self, log_file):
        self.log_file = log_file

    def log_change(self, event_type, src_path):
        change = {
            "event_type": event_type,
            "src_path": src_path,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        }
        print("Algılanan değişiklik:", change)
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(change) + '\n')

    def on_created(self, event):
        self.log_change("created", event.src_path)

    def on_deleted(self, event):
        self.log_change("deleted", event.src_path)

    def on_modified(self, event):
        self.log_change("modified", event.src_path)

    def on_moved(self, event):
        self.log_change("moved", f"{event.src_path} -> {event.dest_path}")


if __name__ == "__main__":
    log_dir = "/home/ubuntu/bsm/logs"
    monitor_dir = "/home/ubuntu/bsm/test"
    log_file = f"{log_dir}/changes.json"

    # Log dizini yoksa oluştur.
    os.makedirs(log_dir, exist_ok=True)

    event_handler = DirectoryMonitor(log_file)
    observer = Observer()
    observer.schedule(event_handler, monitor_dir, recursive=True)

    print("Monitoring started...")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

