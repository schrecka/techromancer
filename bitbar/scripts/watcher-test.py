#!/bin/env python3
import sys
import time
import logging
import os
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

if __name__ == "__main__":
    logging.basicConfig(filename='logger-test.txt', filemode='a', level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    #CHANGE PATH to directory you want to observe
    path = "/Users/Adam/Desktop/techromancer/techromancer/bitbar/scripts/test_dir_test"
    # sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    files = os.listdir(os.curdir)
    mtime_last = {}
    for file in files:
        mtime_last[file] = 0
    try:
        while True:
            time.sleep(1)
            mtime_cur = {}
            for file in files:
                mtime_cur[file] = os.path.getmtime(file)
            if mtime_cur[file] != mtime_last:
                print("File Opened")
            mtime_last = mtime_cur[file]
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
