import sys
import subprocess
import random

SWITCH_NUM = 2
swDPIDs = []
for i in range(SWITCH_NUM):
    swDPIDs.append("00:a4:23:05:00:00:00:0%d" % (i+1))
DefaultRuleNum = 20
UpdateRuleNum = 5


def generateDefaultRule(swDPID):
    rule = '{"switch":"%s", ' % swDPID
    rule = rule + '"name":"default0", "priority":"0", ' + \
        '"active":"true", "actions":""}'
    return rule

def generateMonitorRule(swDPID, name):
    rule = '{"switch":"%s", ' % swDPID
    rule = rule + '"name":"%s", ' % name
    rule = rule + '"priority":"%d", ' % random.randint(1, 60000)
    rule = rule + '"ether-type":"2048", '
    rule = rule + '"src-ip":"%d.%d.%d.%d/%d", ' % (
        random.randint(0, 256), random.randint(0, 256),
        random.randint(0, 256), random.randint(0, 256),
        random.randint(0, 32))
    rule = rule + '"active":"true", "actions":""}' 
    return rule

def generateMonitorRuleDelete(swDPID, name):
    #rule = '{"switch":"%s", ' % swDPID
    #rule = rule + '"name":"%s"}' % name
    rule = '{"name":"%s"}' % name
    return rule
 
def generateRouteRule(swDPID, name):
    rule = '{"switch":"%s", ' % swDPID
    rule = rule + '"name":"%s", ' % name
    rule = rule + '"priority":"%d", ' % random.randint(1, 60000)
    rule = rule + '"ether-type":"2048", '
    rule = rule + '"dst-ip":"%d.%d.%d.%d/%d", ' % (
        random.randint(0, 256), random.randint(0, 256),
        random.randint(0, 256), random.randint(0, 256),
        random.randint(0, 32))
    rule = rule + '"active":"true", "actions":"output=1"}' 
    return rule

def deleteRules(rules, app):
    for rule in rules:
        print rule
        if app == "m":
            subprocess.call(["curl", "-X", "DELETE", "-d", rule,
                "http://localhost:10001/wm/staticflowentrypusher/json"])
        else:
            subprocess.call(["curl", "-X", "DELETE", "-d", rule,
                "http://localhost:20001/wm/staticflowentrypusher/json"])
        print ""

def installRules(rules, app):
    for rule in rules:
        print rule
        if app == "m":
            subprocess.call(["curl", "-d", rule,
                "http://localhost:10001/wm/staticflowentrypusher/json"])
        else:
            subprocess.call(["curl", "-d", rule,
                "http://localhost:20001/wm/staticflowentrypusher/json"])
        print ""

def initMonitor():
    defaultRules = []
    for swDPID in swDPIDs:
        defaultRules.append(generateDefaultRule(swDPID))
    installRules(defaultRules, "m")

    monitorRules = []
    for swDPID in swDPIDs:
        for i in range(DefaultRuleNum):
            monitorRules.append(generateMonitorRule(swDPID,
                "%sMonitor%d" % (swDPID[-2:], i)))
    installRules(monitorRules, "m")

    print "init monitor rules"

def initRoute():
    defaultRules = []
    for swDPID in swDPIDs:
        defaultRules.append(generateDefaultRule(swDPID))
    installRules(defaultRules, "r")

    routeRules = []
    for swDPID in swDPIDs:
        for i in range(DefaultRuleNum):
            routeRules.append(generateRouteRule(swDPID,
                "%sRoute%d" % (swDPID[-2:], i)))
    installRules(routeRules, "r")

    print "init route rules"

def updateMonitor():
    monitorRules = []
    for swDPID in swDPIDs:
        for i in range(UpdateRuleNum):
            monitorRules.append(generateMonitorRule(swDPID,
                "%sMonitor%d" % (swDPID[-2:], DefaultRuleNum + i)))
            #monitorRules.append(generateMonitorRuleDelete(swDPID,
            #    "%sMonitor%d" % (swDPID[-2:], i)))
    installRules(monitorRules, "m")
    #deleteRules(monitorRules, "m")

    print "update monitor rules"


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "\tUsage: ctrl_rule.py init_m/init_r/update_m/update_r"
        sys.exit()

    if sys.argv[1] == "init_m":
        initMonitor()
    elif sys.argv[1] == "init_r":
        initRoute()
    elif sys.argv[1] == "update_m":
        updateMonitor()
#    elif sys.argv[1] == "update_r":
#        updateRoute()
    else:
        print "not supported"


