import os
import cv2

path = "../Image/Home Work Image/"
Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file
        Images.append(file_name)

count = len(Images)
frame = cv2.imread(Images[0])
height, width, channels = frame.shape
size = (width, height)

out = cv2.VideoWriter(
    "Friends.avi", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)

for i in range(0, count):
    print(Images[i])
    frame = cv2.imread(Images[i])
    out.write(frame)

out.release()
print("done")
