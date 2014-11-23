#!/bin/bash

WORKDIR=~/xin-flowmaster

java -jar ${WORKDIR}/floodlight-0.90/target/floodlight.jar -cf ${WORKDIR}/ctrl/ctrl3.floodlight > ${WORKDIR}/ctrl/ctrl3.log 2>&1 &
