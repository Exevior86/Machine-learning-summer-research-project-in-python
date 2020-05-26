import csv

# must convert the memory to a nominal format that can
# be used in the data model
def convertMemory():
    words = []
    f = open("Memory.txt")
    mem = f.readlines()
    for i in mem:
        memWord = float(i[43:48])
        memWord = memWord * 1000
        if memWord < 10000:
            continue
        words.append(int(memWord))
    return words
    
# same as the memory, appends only the data we want that is
# the temperature, eliminates non nominal data
def convertTemp():
    words = []
    f = open("Temp.txt")
    x = f.readlines()
    for i in x:
        word = i[5:9]
        words.append(word)
    return words
    
# same as the memory, appends only the data we want that is
# the temperature, eliminates non nominal data
def convertTasks():
    words = []
    f = open("Tasks.txt")
    x = f.readlines()
    for i in x:
        word = i[7:10]
        words.append(word)
    return words

# same as the memory, appends only the data we want that is
# the temperature, eliminates non nominal data
def convertVolt():
    words = []
    f = open("Volt.txt")
    x = f.readlines()
    for i in x:
        word = i[5:11]
        words.append(word)
    return words
 
# same as the memory, appends only the data we want that is
# the temperature, eliminates non nominal data
def convertTime():
    words = []
    f = open("Time.txt")
    x = f.readlines()
    for i in x:
        i = i.replace("\n", "") #must delete new line characters
        word = i
        words.append(word)
    return words

# same as the memory, appends only the data we want that is
# the temperature, eliminates non nominal data    
def convertCPU():
    words = []
    f = open("CPU.txt")
    x = f.readlines()
    for i in x:
        word = float(i[36:40])
        word = 100 - word     #cpu usage is opposite of what we want
        words.append(word)    #so I subract from 100 to get the total usage
    return words

# After separating all data into a nominal format
# we then combine all of them into one CSV for use 
# in the machine learning models
def combine():
    temp = convertTemp()
    task = convertTasks()
    cpu = convertCPU()
    time = convertTime()
    volts = convertVolt()
    memory = convertMemory()
    row = []
    csvex = csv.writer(open("attck1", "a+"), delimiter=',', quotechar = ' ')
    for i in range(len(task)):
        A = str(temp[i])
        B = str(task[i])
        C = str(cpu[i])
        D = str(time[i])
        E = str(volts[i])
        F = str(memory[i])
        row = E + "," + A + "," + B + "," + D + "," + C + "," + F  
        csvex.writerow([row])
    
combine()