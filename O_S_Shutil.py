# Imports
import os
import shutil

# Variables Declaration
from_dir: str = 'C:/Users/rouna/Programming/WhitehatJr Projects/learning-python/C102_assets-main/C102_assets-main'
to_dir: str = 'C:/Users/rouna/Programming/WhitehatJr Projects/learning-python/Segregated_File'
list_of_files: list = os.listdir(from_dir)

# Control Variable
fileName: str

for fileName in list_of_files:
    name: str
    extension: str
    name, extension = os.path.splitext(fileName)
    if extension == '':
        continue

    if extension in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        path1: str = from_dir + '/' + fileName
        path2: str = to_dir + '/' + 'ImageFiles'
        path3: str = to_dir + '/' + 'ImageFiles' + '/' + fileName

        if os.path.exists(path2):
            print("Moving..." + fileName)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving..." + fileName)
            shutil.move(path1, path3)
