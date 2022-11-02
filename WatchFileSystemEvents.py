import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/rouna/Downloads"
to_dir = "C:/Users/rouna/Downloads/Store_File"

directory_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}


class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created!")
        name, extension = os.path.splitext(event.src_path)
        time.sleep(2)
        for key, value in directory_tree.items():
            if extension in value:
                file_name = os.path.basename(event.src_path)
                print(f"Hurray, Downloaded, {file_name}")
                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):
                    print("Directory Exists...")
                    print("Moving the file...." + file_name)
                    shutil.move(path1, path3)
                    time.sleep(2)
                else:
                    print("Making Directory to store the file....")
                    os.makedirs(path2)
                    print("Moving the file....")
                    shutil.move(path1, path3)
                    time.sleep(2)

    def on_deleted(self, event):
        print(f"Oops! Someone Deleted {event.src_path}")


event_handler = FileEventHandler()

observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)

observer.start()

try:
    while True:
        time.sleep(2)
        print("Looking for file...")
except KeyboardInterrupt:
    print("Program Stopped!")
    observer.stop()

if __name__ == "__main__":
    pass
