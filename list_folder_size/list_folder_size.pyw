import os
import sys
import subprocess
import time

path = "c:/Users/" + os.environ['USERNAME'] + "/AppData/Local"
dirs = []

if "-h" in sys.argv or "help" in sys.argv or "HELP" in sys.argv or "-H" in sys.argv:
    print("########################################")
    print("Lists folders in order of size by walking through each sub tree.")
    print("Enter an empty string to default to AppData/Local.")
    print("Enter \"roaming\" to default to AppData/Roaming.")
    print("Enter \"low\" to default to AppData/LocalLow.")
    print("")
if len(sys.argv) > 1:
    path = sys.argv[1]
    if sys.argv[1] == "roaming":
        path = "c:/Users/" + os.environ['USERNAME'] + "/AppData/Local"
    elif sys.argv[1] == "low":
        path = "c:/Users/" + os.environ['USERNAME'] + "/AppData/Local"

print("##########################")
print("SEARCHING PATH: " + path)
print("##########################")

def get_dir_size(dir_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(dir_path):
        for file in filenames:
            file_path = os.path.join(dirpath, file)
            if not os.path.islink(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

for the_dir in os.listdir(path):
    if os.path.isdir(path + '/' + the_dir):
        size = int(((get_dir_size(path + '/' + the_dir)) / 1024) / 1024)
        if size > 0:
            dirs.append({"name" : the_dir, "size" : size})

temp = sorted(dirs, key=lambda d: d['size'], reverse=True)
with open('res.txt', 'w+') as file:
    for value in temp:
        file.write(value['name'] + ": " + str(value['size']) + " MB\n")