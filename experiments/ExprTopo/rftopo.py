from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import lg, setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
import networkx as nx

class MNTopo(Topo):

    def __init__(self, enable_all = True,
        topoFile = "/home/xinjin/xin-flowmaster/" + \
        "OpenVirteX/experiments/ExprTopo/Rocketfuel/test/weights.intra"):

        "Create Rocketfuel topology for mininet."

        # Add default members to class.
        super(MNTopo, self).__init__()

        # init rocketfuel topo
        self.graph = nx.Graph()
        f = open(topoFile, 'r')
        oneline = f.readline()
        while oneline != '':
            temp = oneline.strip().split()
            if not self.graph.has_edge(temp[0], temp[1]):
                self.graph.add_edge(temp[0], temp[1], weight = float(temp[2]))
                if not 'ports' in self.graph.node[temp[0]]:
                    self.graph.node[temp[0]]['ports'] = 1
                self.graph.node[temp[0]]['ports'] += 1
                if not 'ports' in self.graph.node[temp[1]]:
                    self.graph.node[temp[1]]['ports'] = 1
                self.graph.node[temp[1]]['ports'] += 1
                p0 = self.graph.node[temp[0]]['ports']
                self.graph.edge[temp[0]][temp[1]][temp[0]] = p0
                p1 = self.graph.node[temp[1]]['ports']
                self.graph.edge[temp[0]][temp[1]][temp[1]] = p1
            oneline = f.readline()
        f.close()

        # Add core switches
        for idx, switch in enumerate(self.graph.nodes()):
            index = idx + 1
            self.graph.node[switch]['ridx'] = index
            if index < 16:
                self.graph.node[switch]['dpid'] = '0000000000000%s00' % format(index, 'x')
            elif index < 16*16:
                self.graph.node[switch]['dpid'] = '000000000000%s00' % format(index, 'x')
            elif index < 16*16*16:
                self.graph.node[switch]['dpid'] = '00000000000%s00' % format(index, 'x')
            self.graph.node[switch]['vdpid'] = "00a42305" + self.graph.node[switch]['dpid'][-10:-2]
            self.addSwitch(switch, dpid=self.graph.node[switch]['dpid'])

        # Add hosts and connect them to their core switch
        for switch in self.graph.nodes():
            # Add host
            host = 'h_%s_1' % switch
            ip = '10.0.0.1'
            mac = self.graph.node[switch]['dpid'][4:-1] + '1'
            h = self.addHost(host, ip=ip, mac=mac)
            # Connect hosts to core switches
            self.addLink(h, switch)

        # Connect core switches
        for (u, v) in self.graph.edges():
            self.addLink(u, v)

if __name__ == '__main__':
    topo = MNTopo()
    raw_input("pause")
    net = Mininet(topo, autoSetMacs=True, xterms=False, controller=RemoteController)
    net.addController('c', ip='127.0.0.1') # localhost:127.0.0.1 vm-to-mac:10.0.2.2 server-to-mac:128.112.93.28
    print "\nHosts configured with IPs, switches pointing to OpenVirteX at 127.0.0.1 port 6633\n"
    net.start()
    CLI(net)
    net.stop()
    
