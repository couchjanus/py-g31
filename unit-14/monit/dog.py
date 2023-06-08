
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import logging
import logging.config
import time
import sys

class Watcher:
    
    def __init__(self) -> None:
        self.observer = Observer()
        self.watchDir = sys.argv[1] if len(sys.argv) > 1 else '.'
    
    def run(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M-%S')
        logging.config.fileConfig('logging.conf')
        
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDir, recursive = True)
        self.observer.start()
        
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print('Observer Stopped')
            
        self.observer.join()
        
    
class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        logger = logging.getLogger("mainApp")
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print(f"Watch dog recived created event - {event.src_path}")
            logger.info(f"Watch dog recived created event - {event.src_path}")
        elif event.event_type == 'modified':
            print(f"Watch dog recived modified event - {event.src_path}")
            logger.info(f"Watch dog recived modified event - {event.src_path}")

if __name__ == "__main__":
    watcher = Watcher()
    watcher.run()
