#!/bin/bash

#kill `ps ax|grep floodlight|grep -v grep|awk '{print }'`

WORKDIR=~/xin-flowmaster

java -jar ${WORKDIR}/topo-mininet/multiple.py > ${WORKDIR}/topo-mininet/mn.log 2>&1 &
