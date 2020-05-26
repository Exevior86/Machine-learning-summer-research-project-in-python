# program to send files constantly to a server through the pi once a connection
# has been established
import subprocess
import time, os, threading

def sendFile(files, seconds):
    toSend = files
    for i in toSend:
        path = i
        print(i)
        destination = 'wow@192.168.1.15:/home/wow/Desktop/Data'
        process = os.popen('scp ' + path + ' ' + destination)
        preprocessed = process.read()
        process.close()
        print('success')
        time.sleep(seconds)
    
def findFiles():
    path = '/home/pi/Desktop/DataDump/'
    files = []
    
    for r, d, f in os.walk(path):
        for file in f:
            files.append(os.path.join(r, file))
    
    #for f in files:
        #print(f)
    return files    
        
toFind = findFiles()
sendFile(toFind, 90)