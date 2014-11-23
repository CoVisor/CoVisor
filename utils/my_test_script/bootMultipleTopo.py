import subprocess

#CONTROLLER_IP = "192.168.56.101"
CONTROLLER_IP = "128.112.92.74"
SWITCH_NUM = 2


def bootMonitorController():
    print "*****************************"
    print "***** Monitor Controller ****"
    print "*****************************"
    subprocess.call(["./ovxctl.py", "-n", "createNetwork",
        "tcp:%s:10000" % CONTROLLER_IP, "10.0.0.0", "16"])
    for i in xrange(1, SWITCH_NUM + 1):
        subprocess.call(["./ovxctl.py", "-n", "createSwitch",
            "1", "00:00:00:00:00:00:0%d:00" % i])
        subprocess.call(["./ovxctl.py", "-n", "createPort",
            "1", "00:00:00:00:00:00:0%d:00" % i, "1"])
        subprocess.call(["./ovxctl.py", "-n", "connectHost",
            "1", "00:a4:23:05:00:00:00:0%d" % i, "1",
            "00:00:00:00:0%d:01" % i])
    subprocess.call(["./ovxctl.py", "-n", "startNetwork", "1"])

def bootRouteController():
    print "*****************************"
    print "***** Route Controller *******"
    print "*****************************"
    subprocess.call(["./ovxctl.py", "-n", "createNetwork",
        "tcp:%s:20000" % CONTROLLER_IP, "10.0.0.0", "16"])
    for i in xrange(1, SWITCH_NUM + 1):
        subprocess.call(["./ovxctl.py", "-n", "createSwitch",
            "2", "00:00:00:00:00:00:0%d:00" % i])
        subprocess.call(["./ovxctl.py", "-n", "createPort",
            "2", "00:00:00:00:00:00:0%d:00" % i, "2"])
        subprocess.call(["./ovxctl.py", "-n", "connectHost",
            "2", "00:a4:23:05:00:00:00:0%d" % i, "1",
            "00:00:00:00:0%d:02" % i])
    subprocess.call(["./ovxctl.py", "-n", "startNetwork", "2"])

def installPolicy():
    subprocess.call(["./ovxctl.py", "-n", "createPolicy", "1+2"])

if __name__ == '__main__':
    bootMonitorController()
    bootRouteController()
    installPolicy()


