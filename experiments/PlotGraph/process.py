#!/usr/bin/python
import sys
import time
import random

def processComposition(composition = "parallel"):
    fout = open("res_" + composition +"_all", 'w')
#    fout.write("count")
#    for i in range(12):
#        fout.write("\tBase")
#    for i in range(12):
#        fout.write("\tInc")
#    for i in range(12):
#        fout.write("\tIncOpt")
#    fout.write("\n")
    #ruleCounts = [128, 256, 512, 1024, 2048, 4096]
    #ruleCounts = [1280, 2560, 5120, 10240]
    #ruleCounts = [12800, 25600, 51200, 102400]
    ruleCounts = [1000, 2000, 4000, 8000, 16000, 32000]#, 64000]#, 128000]
    mechanisms = ["strawman", "inc", "incacl"]
    #mechanisms = ["inc", "incacl"]
    for ruleCount in ruleCounts:
        fout.write(str(ruleCount/1000)+"k")
        for mechanism in mechanisms:
            fileName = "res_" + composition + "_" + mechanism + "_" + str(ruleCount)
            columns = list()
            columnCount = 4
            for i in range(columnCount):
                columns.append(list())

            fin = open(fileName, 'r')
            oneline = fin.readline()
            while oneline != "":
                temp = oneline.strip().split()
                for idx,data in enumerate(temp):
                    columns[idx].append(float(data))
                oneline = fin.readline()
            fin.close()

            for i in range(columnCount):
                columns[i].sort()
                if i == 3:
                    fout.write("\t" + str(columns[i][9] + 0.0003))
                    fout.write("\t" + str(columns[i][49] + 0.0003))
                    fout.write("\t" + str(columns[i][89] + 0.0003))
                else:
                    fout.write("\t" + str(columns[i][9]))
                    fout.write("\t" + str(columns[i][49]))
                    fout.write("\t" + str(columns[i][89]))
        fout.write("\n")


def processGateway():
    fout = open("res_gateway_all", 'w')
    fout.write("count")
    for i in range(12):
        fout.write("\tCoVisor")
    fout.write("\n")
    #ipCount = [8, 16, 32, 64, 128, 256, 512, 1024];
    ipCount = [1000, 2000, 4000, 8000, 16000, 32000]
    for ip in ipCount:
        fileName = "res_gateway_" + str(ip)
        columns = list()
        columnCount = 4
        for i in range(columnCount):
            columns.append(list())

        fin = open(fileName, 'r')
        oneline = fin.readline()
        while oneline != "":
            temp = oneline.strip().split()
            for idx,data in enumerate(temp):
                columns[idx].append(float(data))
            oneline = fin.readline()
        fin.close()

        fout.write(str(ip/1000)+"k")
        for i in range(columnCount):
            columns[i].sort()
            fout.write("\t" + str(columns[i][9]))
            fout.write("\t" + str(columns[i][49]))
            fout.write("\t" + str(columns[i][89]))
        fout.write("\n")

def readSwitchTime(fileName = "switch_time.txt"):
    switchTime = list()
    fin = open(fileName, 'r')
    oneline = fin.readline()
    while oneline != "":
        switchTime.append(float(oneline) / 300)
        oneline = fin.readline()
    fin.close()
    return switchTime

def generateTime(inFile, outFile, switchTime, rounds = 100):
    fin = open(inFile, 'r')
    rules = list()
    oneline = fin.readline()
    while oneline != "":
        rules.append(int(oneline))
        oneline = fin.readline()
    fin.close()

    fout = open(outFile, 'w')
    fout.write("10\tCoVisor\tCoVisor\tCoVisor\n")
    for rule in rules:
        updateTimes = list()
        for i in range(rounds):
            updateTime = 0;
            for j in range(rule):
                updateTime += switchTime[random.randint(0, len(switchTime)-1)]
            updateTimes.append(updateTime)
        updateTimes.sort()
        fout.write(str(rule) + "\t" + \
            str(updateTimes[4]) + "\t" + \
            str(updateTimes[49]) + "\t" + \
            str(updateTimes[94]) + "\n")
    fout.close()


if __name__ == '__main__':
	processComposition("parallel")
	processComposition("sequential")
	processComposition("gateway")
	#processGateway()
    #switchTime = readSwitchTime()
    #generateTime("log", "res", switchTime)


