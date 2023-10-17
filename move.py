import time
import os
import shutil
import sys
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

source ="C:/Users/gjoha/Downloads"
destination ="C:/Users/gjoha/OneDrive/Documents/Out of School/Visual Studio Code/BYJUS/Python/Class 103"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt','.pptx'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}
# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Downloaded " + file_name)

                path1 = source + '/' + file_name
                path2 = destination + '/' + key
                path3 = destination + '/' + key + '/' + file_name

                if os.path.exists(path2):

                    print("Directory Exists...")
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

# Initialize Event Handler Class
event_handler = FileMovementHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True)

# Start the Observer
observer.start()
try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped")
    observer.stop()
#Lets hope this works
#          _.-/`)
#         // / / )
#      .=// / / / )
#     //`/ / / / /
#    // /     ` /
#   ||         /
#    \\       /
#     ))    .'
#    //    /
#         /