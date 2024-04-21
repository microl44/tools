import os
import sys
import subprocess
import time
import shutil

username = os.getenv('USERNAME')
source = 'C:\\tmp\\desktop'
destination = "C:\\Users\\" + username + "\\Desktop"

for file in os.listdir(source):
	print(file)
	shutil.move(source + "\\" + file, destination)