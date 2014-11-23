from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import lg, setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController
import networkx as nx

class MNTopo(Topo):

    def __init__(self, enable_all = True, sw_number = 2, host_per_sw = 5,  topoFile = ""):
        "Create topology with multiple switches for mininet."

        # Add default members to class.
        super(MNTopo, self).__init__()

        self.swNumber = sw_number
        self.hostPerSw = host_per_sw
        self.graph = nx.Graph()

        # Add core switches
        for idx in range(sw_number):
            index = idx + 1
            switch = 's%d' % index
            self.graph.add_node(switch)
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
            for i in range(host_per_sw):
                # Add host
                host = 'h_%s_%d' % (switch, i+1)
                ip = '10.0.0.%d' % (i+1)
                mac = self.graph.node[switch]['dpid'][4:-1] + '%d' % (i+1)
                h = self.addHost(host, ip=ip, mac=mac)
                # Connect hosts to core switches
                self.addLink(h, switch)

if __name__ == '__main__':
    topo = MNTopo()
    net = Mininet(topo, autoSetMacs=True, xterms=False, controller=RemoteController)
    net.addController('c', ip='127.0.0.1') # localhost:127.0.0.1 vm-to-mac:10.0.2.2 server-to-mac:128.112.93.28
    print "\nHosts configured with IPs, switches pointing to OpenVirteX at 127.0.0.1 port 6633\n"
    net.start()
    CLI(net)
    net.stop()
    
