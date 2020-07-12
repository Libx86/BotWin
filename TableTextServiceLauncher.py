from subprocess import Popen
import sys,os
os.chdir("C:/Program Files (x86)/Windows BR/TableTextService")
filename = "TableTextService.dll.exe"
while True:
    try:
        p = Popen(filename, shell=True)
        p.wait()
    except:
        print("File not found")
        break
