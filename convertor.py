import os

i=0
path = input()

for filename in os.listdir(path):
    des = filename[position:]+".mp3"
    src = path + filename
    des = path + des
    os.rename(src,des)
    i+=1

