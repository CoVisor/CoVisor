#!/bin/bash

#kill `ps ax|grep floodlight|grep -v grep|awk '{print }'`

WORKDIR=~/xin-flowmaster

java -jar ${WORKDIR}/floodlight-0.90/target/floodlight.jar -cf ${WORKDIR}/ctrl/ctrl1.floodlight > ${WORKDIR}/ctrl/ctrl1.log 2>&1 &
java -jar ${WORKDIR}/floodlight-0.90/target/floodlight.jar -cf ${WORKDIR}/ctrl/ctrl2.floodlight > ${WORKDIR}/ctrl/ctrl2.log 2>&1 &
#java -jar ${WORKDIR}/floodlight-0.90/target/floodlight.jar -cf ${WORKDIR}/ctrl/ctrl3.floodlight > ${WORKDIR}/ctrl/ctrl3.log 2>&1 &
