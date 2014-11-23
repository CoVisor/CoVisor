#!/usr/bin/python
import sys
import subprocess
import time
import random
from ExprTopo.mtopo import *

#********************************************************************
# Demo App
#********************************************************************
class DemoMonitorApp():

    def __init__(self, topo):
        self.graph = topo.graph
        switch = self.graph.nodes()[0]
        dpid = self.graph.node[switch]['vdpid']
        self.rules = []

        rule = '{"switch":"%s", ' % dpid + \
                '"name":"DemoMinitor0", ' + \
                '"priority":"0", ' + \
                '"active":"true", "actions":""}'
        self.rules.append(rule)

        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoMonitor1", ' + \
            '"priority":"1", ' + \
            '"ether-type":"2048", ' + \
            '"src-ip":"1.0.0.0/24", ' + \
            '"active":"true", "actions":""}'
        self.rules.append(rule)

    def installRules(self):
        for rule in self.rules:
            print rule
            cmd = "curl -d '%s' http://localhost:10001/wm/staticflowentrypusher/json" % rule
            subprocess.call(cmd, shell=True)
            print ""

class DemoRouterApp():

    def __init__(self, topo):
        self.graph = topo.graph
        switch = self.graph.nodes()[0]
        dpid = self.graph.node[switch]['vdpid']
        self.rules = []

        rule = '{"switch":"%s", ' % dpid + \
                '"name":"DemoRouter0", ' + \
                '"priority":"0", ' + \
                '"active":"true", "actions":""}'
        self.rules.append(rule)

        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoRouter1", ' + \
            '"priority":"1", ' + \
            '"ether-type":"2048", ' + \
            '"dst-ip":"2.0.0.1", ' + \
            '"active":"true", "actions":"output=1"}'
        self.rules.append(rule)

        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoRouter2", ' + \
            '"priority":"1", ' + \
            '"ether-type":"2048", ' + \
            '"dst-ip":"2.0.0.2", ' + \
            '"active":"true", "actions":"output=2"}'
        self.rules.append(rule)

    def installRules(self):
        for rule in self.rules:
            print rule
            cmd = "curl -d '%s' http://localhost:20001/wm/staticflowentrypusher/json" % rule
            subprocess.call(cmd, shell=True)
            print ""

class DemoLoadBalancerApp():

    def __init__(self, topo):
        self.graph = topo.graph
        switch = self.graph.nodes()[0]
        dpid = self.graph.node[switch]['vdpid']
        self.rules = []

        rule = '{"switch":"%s", ' % dpid + \
                '"name":"DemoLB0", ' + \
                '"priority":"0", ' + \
                '"active":"true", "actions":""}'
        self.rules.append(rule)

        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoLB1", ' + \
            '"priority":"3", ' + \
            '"ether-type":"2048", ' + \
            '"src-ip":"0.0.0.0/2", ' + \
            '"dst-ip":"3.0.0.0", ' + \
            '"active":"true", "actions":"set-dst-ip=2.0.0.1"}'
        self.rules.append(rule)

        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoLB2", ' + \
            '"priority":"1", ' + \
            '"ether-type":"2048", ' + \
            '"dst-ip":"3.0.0.0", ' + \
            '"active":"true", "actions":"set-dst-ip=2.0.0.2"}'
        self.rules.append(rule)

    def installRules(self):
        for rule in self.rules:
            print rule
            cmd = "curl -d '%s' http://localhost:10001/wm/staticflowentrypusher/json" % rule
            subprocess.call(cmd, shell=True)
            print ""

class DemoVirtApp():

    def __init__(self, topo):
        self.graph = topo.graph

        dpid = "00:a4:23:05:00:00:00:01"
        self.rules1 = []
        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoVirt1R1", ' + \
            '"priority":"1", ' + \
            '"ether-type":"2048", ' + \
            '"dst-ip":"1.0.0.0/8", ' + \
            '"active":"true", "actions":"output=3"}'
        self.rules1.append(rule)
        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoVirt1R2", ' + \
            '"priority":"4", ' + \
            '"ether-type":"2048", ' + \
            '"dst-ip":"2.0.0.0/16", ' + \
            '"active":"true", "actions":"output=2"}'
        self.rules1.append(rule)

        dpid = "00:a4:23:05:00:00:00:01"
        self.rules2 = []
        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoVirt2R1", ' + \
            '"priority":"1", ' + \
            '"ether-type":"2048", ' + \
            '"dst-ip":"1.0.0.0/4", ' + \
            '"active":"true", "actions":"set-dst-ip=2.0.0.0,output=3"}'
        self.rules2.append(rule)
        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoVirt2R2", ' + \
            '"priority":"6", ' + \
            '"ether-type":"2048", ' + \
            '"dst-ip":"1.0.0.0/24", ' + \
            '"active":"true", "actions":"output=2"}'
        self.rules2.append(rule)

        dpid = "00:a4:23:05:00:00:00:01"
        self.rules3 = []
        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoVirt3R1", ' + \
            '"priority":"1", ' + \
            '"ether-type":"2048", ' + \
            '"dst-ip":"1.0.0.0/8", ' + \
            '"active":"true", "actions":"output=3"}'
        self.rules3.append(rule)
        rule = '{"switch":"%s", ' % dpid + \
            '"name":"DemoVirt3R2", ' + \
            '"priority":"4", ' + \
            '"ether-type":"2048", ' + \
            '"dst-ip":"2.0.0.0/16", ' + \
            '"active":"true", "actions":"output=2"}'
        self.rules3.append(rule)

    def installRules(self):
        for rule in self.rules1:
            print rule
            cmd = "curl -d '%s' http://localhost:10001/wm/staticflowentrypusher/json" % rule
            subprocess.call(cmd, shell=True)
            print ""
        for rule in self.rules2:
            print rule
            cmd = "curl -d '%s' http://localhost:20001/wm/staticflowentrypusher/json" % rule
            subprocess.call(cmd, shell=True)
            print ""
        for rule in self.rules3:
            print rule
            cmd = "curl -d '%s' http://localhost:30001/wm/staticflowentrypusher/json" % rule
            subprocess.call(cmd, shell=True)
            print ""

