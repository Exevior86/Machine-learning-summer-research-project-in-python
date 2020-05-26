import subprocess
import time, os, threading

#processes data from the grep command
def getCPUFromFile():
    os.popen('cat CPUTasksMem.txt | grep %Cpu > CPU.txt')
    
def getMemory():
    os.popen('cat CPUTasksMem.txt | grep Mem > Memory.txt')
    
def getTasks():
    os.popen('cat CPUTasksMem.txt | grep Tasks > Tasks.txt')

#separates the memory, tasks, and CPU from the grep file   
def seperate():
    getCPUFromFile()
    getMemory()
    getTasks()
    
# pretty self explanatory, each method gets a particular
# data point    
def getTemp():
    process = os.popen('/opt/vc/bin/vcgencmd measure_temp')
    preprocessed = process.read()
    process.close()
    output = 'Temp.txt'
    fout = open(output, 'a+')
    fout.write(preprocessed)
    fout.close()

def getVoltage():
    process = os.popen('/opt/vc/bin/vcgencmd measure_volts')
    preprocessed = process.read()
    process.close()
    output = 'Volt.txt'
    fout = open(output, 'a+')
    fout.write(preprocessed)
    fout.close()
    
def getCPU():
    process = os.popen('sudo top -b -n1')
    preprocessed = process.read()
    process.close()
    output = 'CPUTasksMem.txt'
    fout = open(output, 'a+')
    fout.write(preprocessed)
    fout.close()

def getTime(sec):
    second = str(sec)
    output = 'Time.txt'
    fout = open(output, 'a+')
    fout.write(second + ',\n')
    fout.close()
    
def repeat(seconds):
    totalTime = 0;
    while (totalTime <= 3600):
        getCPU()
        getVoltage()
        getTemp()
        getTime(totalTime)
        totalTime += seconds
        time.sleep(5)
        print("captured" + str(totalTime))
# repeat just loops through for an hour while collecting
# data by calling the above methods every 5 seconds
repeat(5)
# at the end of collection, separate each data point into it's
# own text file for easier processing
seperate()