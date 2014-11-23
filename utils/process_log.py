#!/usr/bin/env python

import sys
import urllib2

def process():
    fin = open("ovx.log","r")
    fout = open("ovx_processed.log", "w")
    thread_log = {}
    oneline = fin.readline()
    while oneline != "":
        if oneline.find("magic0x2014") != -1:
            temp = oneline.strip().split(" ")
            if not thread_log.has_key(temp[1]):
                thread_log[temp[1]] = []
            thread_log[temp[1]].append(oneline)
        else:
            fout.write(oneline)
        oneline = fin.readline()
    for k in thread_log.keys():
        for v in thread_log[k]:
            fout.write(v)
    fin.close()
    fout.close()


if __name__ == '__main__':
    process()
