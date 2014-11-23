#!/usr/bin/python
import sys

class RTopo:
    def __init__(self):
        self.switches = []
        self.edges = {}
        self.pDist = {}
        self.pNext = {}
        self.pInfinity = 100000
        self.pNull = "null"

    def parse(self, fileName):
        f = open(fileName, 'r')
        oneline = f.readline()
        while oneline != '':
            temp = oneline.strip().split()

            # add switch
            if not temp[0] in self.switches:
                self.switches.append(temp[0])
            if not temp[1] in self.switches:
                self.switches.append(temp[1])

            # add edge
            if not temp[0] in self.edges:
                self.edges[temp[0]] = {}
            self.edges[temp[0]][temp[1]] = float(temp[2])

            oneline = f.readline()
        f.close()
        #self.FloydWarshallShortestPaths()

    def FloydWarshallShortestPaths(self):
        for src in self.switches:
            self.pDist[src] = {}
            self.pNext[src] = {}
            for dst in self.switches:
                self.pDist[src][dst] = self.pInfinity
                self.pNext[src][dst] = self.pNull

        for u, vs in self.edges.items():
            for v in vs:
                self.pDist[u][v] = self.edges[u][v]
                self.pNext[u][v] = v
        for k in self.switches:
            for i in self.switches:
                for j in self.switches:
                    if self.pDist[i][k] + self.pDist[k][j] < self.pDist[i][j]:
                        self.pDist[i][j] = self.pDist[i][k] + self.pDist[k][j]
                        self.pNext[i][j] = self.pNext[i][k]
                        
    def getPath(self, u, v):
        if self.pNext[u][v] == self.pNull:
            return []
        path = [u]
        while u != v:
            u = self.pNext[u][v]
            path.append(u)
        return path

    def interactive(self):
        print rtopo.switches
        while True:
            u = raw_input('src: ')
            v = raw_input('dst: ')
            path = rtopo.getPath(u, v)
            print path

if __name__ == '__main__':
    rtopo = RTopo()
    rtopo.parse(sys.argv[1])
    print len(rtopo.switches)
    #rtopo.interactive()

