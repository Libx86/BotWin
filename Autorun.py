from subprocess import Popen
import sys

filename = "TableTextService.dll.exe"
while True:
    try:
        p = Popen(filename, shell=True)
        p.wait()
    except:
        print("File not found")