# Modules Import
import os
import shutil

# Path Info
from_dir = "C:/Users/rouna/Programming/WhitehatJr Projects/learning-python"
to_dir = "C:/Users/rouna/Programming/WhitehatJr Projects/learning-python/Segregated_File"

# Listing files
listOf_files = os.listdir(from_dir)
print(listOf_files)

# Logics

for fileName in listOf_files:
    name, ext = os.path.splitext(fileName)
    if ext == '':
        continue

    if ext in ['.pdf', '.txt', '.docx', '.doc']:
        path_one = from_dir + '/' + fileName
        path_two = to_dir + '/' + 'Documents'
        path_three = to_dir + '/' + 'Documents' + '/' + fileName

        if os.path.exists(path_two):
            print(f"Moving.... {fileName}")
            shutil.move(path_one, path_three)
        else:
            os.makedirs(path_two)
            print(f"Moving.... {fileName}")
            shutil.move(path_one, path_three)
