#!/usr/bin/python
import sys
import time
import subprocess
import random
from ExprTopo.rftopo import *
from apps import *

def processLog2(logFile, resLogFile):
    fin = open(logFile, 'r')
    fout = open(resLogFile, 'w')

    t00 = 0
    t0 = 0
    t1 = 0
    t2 = 0
    t3 = 0
    oneline = fin.readline()
    while oneline != "":
        if oneline.find("MagicTimestamp\t4") != -1:
            #startTime = int(oneline.strip().split('\t')[-1])
            print "hello"
            break
        oneline = fin.readline()
    oneline = fin.readline()
    while oneline != "":
        if oneline.find("MagicTimestamp\t00") != -1:
            info = oneline.strip().split('\t')
            t00 = int(info[2])
        if oneline.find("MagicTimestamp\t0") != -1:
            info = oneline.strip().split('\t')
            t0 = int(info[2])
        if oneline.find("MagicTimestamp\t1") != -1:
            info = oneline.strip().split('\t')
            t1 = int(info[2])
        if oneline.find("MagicTimestamp\t3") != -1:
            info = oneline.strip().split('\t')
            t3 = int(info[2])
        if oneline.find("MagicTimestamp\t2") != -1:
            info = oneline.strip().split('\t')
            t2 = int(info[2])
            elapse1 = (t0-t00) / 1e6
            elapse2 = (t3-t00) / 1e6
            elapse3 = (t1-t00) / 1e6
            elapse4 = t2 / 1e6
            fout.write(str(elapse1) + '\t'+ str(elapse2) + '\t' + str(elapse3) + '\t' +
                str(elapse4) + '\t' + '\t'.join(info[3:]) + '\n')
        oneline = fin.readline()
    fin.close()
    fout.close()

def processLog(logFile, resLogFile):
    fin = open(logFile, 'r')
    fout = open(resLogFile, 'w')

    startTime = 0
    t0 = 0
    t1 = 0
    t2 = 0
    oneline = fin.readline()
    while oneline != "":
        if oneline.find("MagicTimestamp\t4") != -1:
            #startTime = int(oneline.strip().split('\t')[-1])
            break
        oneline = fin.readline()
    oneline = fin.readline()
    while oneline != "":
        if oneline.find("MagicTimestamp\t2") != -1:
            info = oneline.strip().split('\t')
            time = int(info[2]) / 1e6 # in ms
            fout.write(str(time) + '\t' + '\t'.join(info[3:]) + '\n')
        oneline = fin.readline()
    fin.close()
    fout.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "\tUsage: log_process.py logFile resLogFile"
        sys.exit()

    logFile = sys.argv[1]
    resLogFile = sys.argv[2]
    processLog2(logFile, resLogFile)


