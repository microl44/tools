import os
import sys
import subprocess
import time
import shutil

username = os.getenv('USERNAME')
source = 'C:\\Users\\' + username + '\\Desktop'
destination = r"C:\tmp\desktop"

for file in os.listdir(source):
	shutil.move(source + r"\\" + file, destination)