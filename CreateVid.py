import os
import cv2

path = "Imgs"
imgs = []

for i in os.listdir(path):
    name, ext = os.path.splitext(i)
    if ext in [".gif", ".png", ".jpg", ".jpeg", ".jfif"]:
        file_name = path+"/"+i
        print(file_name)
        imgs.append(file_name)

frame = cv2.imread(imgs[0])
height, width, chanels = frame.shape
print(width, height)

out = cv2.VideoWriter("output.mp4", cv2.VideoWriter_fourcc(*'DIVX'), 0.8, (width,height))
for i in range(0,len(imgs)):
    frame = cv2.imread(imgs[i])
    out.write(frame)

out.release()
