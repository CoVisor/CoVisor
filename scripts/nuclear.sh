#!/bin/sh

# This script always recompiles all CoVisor source files.
# ovx.sh does not recompile if the jar file already exists.

OVXHOME=`dirname $0`/..
#echo $OVXHOME
OVX_JAR="${OVXHOME}/target/OpenVirteX.jar"
OVX_TARGET="${OVXHOME}/target"

JVM_OPTS="-Xms512m -Xmx2g"
## If you want JaCoCo Code Coverage reports... uncomment line below
#JVM_OPTS="$JVM_OPTS -javaagent:${OVXHOME}/lib/jacocoagent.jar=dumponexit=true,output=file,destfile=${OVXHOME}/target/jacoco.exec"
JVM_OPTS="$JVM_OPTS -XX:+TieredCompilation"
JVM_OPTS="$JVM_OPTS -XX:+UseCompressedOops"
JVM_OPTS="$JVM_OPTS -XX:+UseConcMarkSweepGC -XX:+AggressiveOpts -XX:+UseFastAccessorMethods"
JVM_OPTS="$JVM_OPTS -XX:MaxInlineSize=8192 -XX:FreqInlineSize=8192" 
JVM_OPTS="$JVM_OPTS -XX:CompileThreshold=1500 -XX:PreBlockSpin=8" 

rm -rf ${OVX_TARGET}

if [ ! -e ${OVX_TARGET} ]; then
  echo "target successfully removed"
fi
cd ${OVXHOME}
echo "Packaging CoVisor for you..."
mvn package -Dmaven.test.skip > scripts/errors.txt
cd -

if [ ! -e ${OVX_JAR} ]; then
  echo "jar still does not exist."
fi

# echo "Starting OpenVirteX..."
# java ${JVM_OPTS} -Dlog4j.configurationFile=../config/log4j2.xml -Djavax.net.ssl.keyStore=../config/sslStore -jar ${OVX_JAR}
  
