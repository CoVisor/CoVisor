#!/usr/bin/python
import sys
import time
import subprocess
import random
from ExprTopo.mtopo import *
from apps import *

WorkDir = "/home/xinjin/xin-flowmaster"
CONTROLLER_IP = "localhost"
ovxctlPy = "%s/OpenVirteX/utils/ovxctl.py" % WorkDir
swNumber = 1

#********************************************************************
# mininet: start, kill
#********************************************************************
def startMininet():
    topo = MNTopo(sw_number = swNumber)
    net = Mininet(topo, autoSetMacs=True, xterms=False,
        controller=RemoteController)
    net.addController('c', ip='127.0.0.1')
    print "\nHosts configured with IPs, " + \
        "switches pointing to OpenVirteX at 127.0.0.1 port 6633\n"
    net.start()
    return (topo, net)

def killMininet():
    print "kill mininet"
    subprocess.call("mn -c > /dev/null 2>&1", shell=True)

#********************************************************************
# ovx: start, show, kill, add controller
#********************************************************************
def startOVX():
    with open("ovx.log", "w") as logfile:
        subprocess.call("sh %s/OpenVirteX/scripts/ovx.sh &" % WorkDir,
            shell=True, stdout=logfile, stderr=subprocess.STDOUT)

def showOVX():
    subprocess.call("ps ax | grep ovx.sh | grep -v grep", shell=True)
    subprocess.call("ps ax | grep java | grep -v grep", shell=True)

def killOVX():
    print "kill ovx"
    subprocess.call("ps ax | grep ovx.sh | grep -v grep | awk '{print $1}' " +
        #"| xargs kill > /dev/null 2>&1", shell=True)
        "| xargs kill -9 > /dev/null 2>&1", shell=True)
        #"| xargs pkill -TERM -P > /dev/null 2>&1", shell=True)
    subprocess.call("ps ax | grep OpenVirteX | grep -v grep | awk '{print $1}' " +
        "| xargs kill -9 > /dev/null 2>&1", shell=True)

def createPlumbingGraph():
    cmd = "%s -n createPlumbingSwitch 00:00:00:00:00:00:01:00 1" % ovxctlPy
    subprocess.call(cmd, shell=True)

def addController1(topo):
    print "*****************************"
    print "******** Controller 1 *******"
    print "*****************************"
    cmd = "%s -n createNetwork tcp:%s:10000 10.0.0.0 16" % (ovxctlPy,
        CONTROLLER_IP)
    subprocess.call(cmd, shell=True)

    cmd = "%s -n createSwitch 1 00:00:00:00:00:00:01:00 0" % ovxctlPy
    subprocess.call(cmd, shell=True)

    cmd = "%s -n startNetwork 1" % ovxctlPy
    subprocess.call(cmd, shell=True)

def addController2(topo):
    print "*****************************"
    print "******** Controller 2 *******"
    print "*****************************"
    cmd = "%s -n createNetwork tcp:%s:20000 10.0.0.0 16" % (ovxctlPy,
        CONTROLLER_IP)
    subprocess.call(cmd, shell=True)

    cmd = "%s -n createSwitch 2 00:00:00:00:00:00:01:00 0" % ovxctlPy
    subprocess.call(cmd, shell=True)

    cmd = "%s -n startNetwork 2" % ovxctlPy
    subprocess.call(cmd, shell=True)

def createPolicy(policy):
    cmd = "%s -n createPolicy 00:00:00:00:00:00:01:00 0 %s" % (ovxctlPy, policy)
    subprocess.call(cmd, shell=True)

def createACL(acl):
    cmd = "%s -n createACL %s" % (ovxctlPy, acl)
    subprocess.call(cmd, shell=True)

#********************************************************************
# floodlight: start, show, kill
#********************************************************************
def startOneFloodlight(index):
    with open("ctrl%d.log" % index, "w") as logfile:
        subprocess.call("java -jar " +
            "%s/floodlight-0.90/target/floodlight.jar -cf " % WorkDir +
            "%s/OpenVirteX/experiments/" % WorkDir +
            "ctrl/ctrl%d.floodlight &" % index,
            shell=True, stdout=logfile, stderr=subprocess.STDOUT)

def startFloodlight(count):
    if count > 3:
        print "warning: bigger than 3 controllers, only start 3 controllers"
        count = 3
    for i in range(count):
        startOneFloodlight(i+1)

def showFloodlight():
    subprocess.call("ps ax | grep floodlight | grep -v grep", shell=True)

def killFloodlight():
    print "kill floodlight"
    subprocess.call("ps ax | grep floodlight | grep -v grep | awk '{print $1}' " +
        "| xargs kill -9 > /dev/null 2>&1", shell=True)

#********************************************************************
# utils
#********************************************************************
def cleanAll():
    killMininet()
    killFloodlight()
    killOVX()
    showOVX()
    showFloodlight()

#********************************************************************
# expr: parallel
#********************************************************************
def exprParallel():
    cleanAll()
    startFloodlight(2)
    startOVX()
    (topo, net) = startMininet()
    time.sleep(5)
    createPlumbingGraph()
    addController1(topo)
    addController2(topo)
    createACL('1 dltype:exact,srcip:prefix,dstip:prefix output')
    createACL('2 dltype:exact,dstip:prefix output')
    createPolicy('"1+2"')
    app1 = DemoMonitorApp(topo)
    app1.installRules()
    app2 = DemoRouterApp(topo)
    app2.installRules()
    CLI(net)

#********************************************************************
# expr: sequential
#********************************************************************
def exprSequential():
    cleanAll()
    startFloodlight(2)
    startOVX()
    (topo, net) = startMininet()
    time.sleep(5)
    createPlumbingGraph()
    addController1(topo)
    addController2(topo)
    createACL('1 dltype:exact,srcip:prefix,dstip:exact mod:dstip')
    createACL('2 dltype:exact,dstip:prefix output')
    createPolicy('"1>2"')
    app1 = DemoLoadBalancerApp(topo)
    app1.installRules()
    app2 = DemoRouterApp(topo)
    app2.installRules()
    CLI(net)

#********************************************************************
# expr: virtual topology
#********************************************************************
def virtCreatePlumbingGraph():
    cmd = "%s -n createPlumbingSwitch 00:00:00:00:00:00:01:00 3" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingPort 00:00:00:00:00:00:01:00 0 1" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingPort 00:00:00:00:00:00:01:00 0 2" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingPort 00:00:00:00:00:00:01:00 0 0" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingPort 00:00:00:00:00:00:01:00 1 0" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingPort 00:00:00:00:00:00:01:00 1 3" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingPort 00:00:00:00:00:00:01:00 1 0" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingPort 00:00:00:00:00:00:01:00 2 0" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingPort 00:00:00:00:00:00:01:00 2 4" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingPort 00:00:00:00:00:00:01:00 2 5" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingLink 00:00:00:00:00:00:01:00 0 3 1 1" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPlumbingLink 00:00:00:00:00:00:01:00 1 3 2 1" % ovxctlPy
    subprocess.call(cmd, shell=True)

def virtAddController1(topo):
    print "*****************************"
    print "******** Controller 1 *******"
    print "*****************************"
    cmd = "%s -n createNetwork tcp:%s:10000 10.0.0.0 16" % (ovxctlPy,
        CONTROLLER_IP)
    subprocess.call(cmd, shell=True)

    cmd = "%s -n createSwitch 1 00:00:00:00:00:00:01:00 0" % ovxctlPy
    subprocess.call(cmd, shell=True)

    cmd = "%s -n startNetwork 1" % ovxctlPy
    subprocess.call(cmd, shell=True)

def virtAddController2(topo):
    print "*****************************"
    print "******** Controller 2 *******"
    print "*****************************"
    cmd = "%s -n createNetwork tcp:%s:20000 10.0.0.0 16" % (ovxctlPy,
        CONTROLLER_IP)
    subprocess.call(cmd, shell=True)

    cmd = "%s -n createSwitch 2 00:00:00:00:00:00:01:00 1" % ovxctlPy
    subprocess.call(cmd, shell=True)

    cmd = "%s -n startNetwork 2" % ovxctlPy
    subprocess.call(cmd, shell=True)

def virtAddController3(topo):
    print "*****************************"
    print "******** Controller 3 *******"
    print "*****************************"
    cmd = "%s -n createNetwork tcp:%s:30000 10.0.0.0 16" % (ovxctlPy,
        CONTROLLER_IP)
    subprocess.call(cmd, shell=True)

    cmd = "%s -n createSwitch 3 00:00:00:00:00:00:01:00 2" % ovxctlPy
    subprocess.call(cmd, shell=True)

    cmd = "%s -n startNetwork 3" % ovxctlPy
    subprocess.call(cmd, shell=True)

def virtCreatePolicy():
    cmd = "%s -n createPolicy 00:00:00:00:00:00:01:00 0 1" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPolicy 00:00:00:00:00:00:01:00 1 2" % ovxctlPy
    subprocess.call(cmd, shell=True)
    cmd = "%s -n createPolicy 00:00:00:00:00:00:01:00 2 3" % ovxctlPy
    subprocess.call(cmd, shell=True)

def exprVirt():
    cleanAll()
    startFloodlight(3)
    startOVX()
    (topo, net) = startMininet()
    time.sleep(5)
    virtCreatePlumbingGraph()
    virtAddController1(topo)
    virtAddController2(topo)
    virtAddController3(topo)
    createACL('1 dltype:exact,dstip:prefix output')
    createACL('2 dltype:exact,dstip:prefix output,mod:dstip')
    createACL('3 dltype:exact,dstip:prefix output')
    virtCreatePolicy()
    app = DemoVirtApp(topo)
    app.installRules()
    CLI(net)

#********************************************************************
# main
#********************************************************************
   
def printHelp():
    print "\tUsage: ctrl.py"
    print "\t\tstart-mn kill-mn"
    print "\t\tstart-ovx show-ovx kill-ovx"
    print "\t\tstart-fl show-fl kill-fl"
    print "\t\texpr-parallel expr-sequential expr-virt"
    print "\t\tclean"

if __name__ == '__main__':
    if len(sys.argv) < 2:
        printHelp()
        sys.exit()

    if sys.argv[1] == "start-mn":
        startMininet()
    elif sys.argv[1] == "kill-mn":
        killMininet()
    elif sys.argv[1] == "start-ovx":
        startOVX()
    elif sys.argv[1] == "show-ovx":
        showOVX()
    elif sys.argv[1] == "kill-ovx":
        killOVX()
    elif sys.argv[1] == "start-fl":
        startFloodlight()
    elif sys.argv[1] == "show-fl":
        showFloodlight()
    elif sys.argv[1] == "kill-fl":
        killFloodlight()
    elif sys.argv[1] == "expr-parallel":
        exprParallel()
    elif sys.argv[1] == "expr-sequential":
        exprSequential()
    elif sys.argv[1] == "expr-virt":
        exprVirt()
    elif sys.argv[1] == "clean":
        cleanAll()
    else:
        printHelp()



