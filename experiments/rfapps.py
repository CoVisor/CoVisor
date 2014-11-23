#!/usr/bin/python
import sys
import subprocess
import time
import random
from ExprTopo.rftopo import *

#********************************************************************
# Routing App
#********************************************************************
class RoutingApp():

    def __init__(self, topo, classbenchFile):
        self.graph = topo.graph
        self.rules = {}
        self.ruleCount = 0

        # assign subnets to switches
        subnets = set()
        f = open(classbenchFile, 'r')
        oneline = f.readline()
        while oneline != "":
            temp = oneline.strip().split()
            subnets.add(temp[0][1:])
            subnets.add(temp[1])
            oneline = f.readline()
        f.close()
        subnets = list(subnets)

        perSwSubnetCount = len(subnets) / len(topo.graph.nodes())
        for index, switch in enumerate(topo.graph.nodes()):
            topo.graph.node[switch]['subnets'] = []
            for snIndex in range(perSwSubnetCount):
                subnet = subnets[index * perSwSubnetCount + snIndex]
                topo.graph.node[switch]['subnets'].append(subnet)

    def genRules(self):
        paths = nx.all_pairs_dijkstra_path(self.graph)
        for dst in self.graph.nodes():
            visited = set()
            for src in self.graph.nodes():
                if src == dst:
                    continue
                path = paths[src][dst]
                if len(path) == 0:
                    continue
                prev = path[0]
                for sw in path[1:]:
                    if prev in visited:
                        prev = sw
                        continue
                    visited.add(prev)
                    vdpid = self.graph.node[prev]['vdpid']
                    output = self.graph.edge[prev][sw][prev]
                    for subnet in self.graph.node[dst]['subnets']:
                        name = "RouteApp%d" % self.ruleCount
                        rule = '{"switch":"%s", ' % vdpid + \
                            '"name":"%s", ' % name + \
                            '"priority":"%s", ' % subnet.split('/')[1] + \
                            '"ether-type":"2048", ' + \
                            '"dst-ip":"%s", ' % subnet + \
                            '"active":"true", "actions":"output=%d"}' % output
                        self.rules[name] = rule
                        self.ruleCount += 1
                    prev = sw
        print len(self.rules)

    def installRules(self):
        for rule in self.rules.values():
            #print rule
            cmd = "curl -d '%s' http://localhost:20001/wm/staticflowentrypusher/json" % rule
            subprocess.call(cmd, shell=True)
            print ""

#********************************************************************
# Firewall App
#********************************************************************
class FirewallApp():

    def __init__(self, topo, classbenchFile):
        self.graph = topo.graph
        self.rules = {}
        self.ruleCount = 0

        self.addRules = {}
        self.addRuleCount = 5

        random.seed(1)
        self.metaRules = []
        f = open(classbenchFile, 'r')
        oneline = f.readline()
        while oneline != "":
            temp = oneline.strip().split('\t')
            rule = '"priority":"%d", ' % random.randint(1, 100) + \
                '"ether-type":"2048", ' + \
                '"src-ip":"%s", ' % temp[0][1:] + \
                '"dst-ip":"%s", ' % temp[1]

            srcports = [int(x) for x in temp[2].split(':')]
            if srcports[0] == srcports[1]:
                rule = rule + '"src-port":"%d", ' % srcports[0]

            dstports = [int(x) for x in temp[3].split(':')]
            if dstports[0] == dstports[1]:
                rule = rule + '"dst-port":"%d", ' % dstports[0]

            protocol = temp[4].split('/')
            if protocol[1] == '0xFF':
                rule = rule + '"protocol":"%s", ' % int(protocol[0], 0)
            
            if random.randint(0, 1) == 0:
                rule = rule + '"active":"true", "actions":""}' 
            else:
                rule = rule + '"active":"true", "actions":"output=1"}' 

            self.metaRules.append(rule)
            self.ruleCount += 1
            oneline = f.readline()
        f.close()

    def genRules(self):
        for switch in self.graph.nodes():
            ridx = self.graph.node[switch]['ridx'] 
            vdpid = self.graph.node[switch]['vdpid']
            for index, metaRule in enumerate(self.metaRules[:-self.addRuleCount]):
                name = "FWAppS%dR%d" % (ridx, index)
                rule = '{"switch":"%s", ' % vdpid + \
                            '"name":"%s", ' % name + \
                            metaRule
                self.rules[name] = rule
            for index, metaRule in enumerate(self.metaRules[-self.addRuleCount:]):
                name = "FWAppS%dR%d" % (ridx, index + len(self.metaRules) - self.addRuleCount)
                rule = '{"switch":"%s", ' % vdpid + \
                            '"name":"%s", ' % name + \
                            metaRule
                self.addRules[name] = rule

    def installRules(self):
        for rule in self.rules.values():
            #print rule
            cmd = "curl -d '%s' http://localhost:10001/wm/staticflowentrypusher/json" % rule
            subprocess.call(cmd, shell=True)
            print ""

    def updateRules(self):
        for rule in self.addRules.values():
            #print rule
            cmd = "curl -d '%s' http://localhost:10001/wm/staticflowentrypusher/json" % rule
            subprocess.call(cmd, shell=True)
            print ""


