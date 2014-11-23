from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import lg, setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

FANOUT = 2
SWITCH_NUM = 2
CORES = {}
for i in range(1, SWITCH_NUM + 1):
    CORES['s%d' % i] = {}
    if i < 10:
        CORES['s%d' % i]['dpid'] = '0000000000000%d00' % i
    else:
        CORES['s%d' % i]['dpid'] = '000000000000%d00' % i

class MultipleTopo(Topo):

    def __init__(self, enable_all = True):
        "Create Multiple topology."

        # Add default members to class.
        super(MultipleTopo, self).__init__()


        # Add core switches
        self.cores = {}
        for switch in CORES:
            self.cores[switch] = self.addSwitch(switch, dpid=(CORES[switch]['dpid']))

        # Add hosts and connect them to their core switch
        for switch in CORES:
            for count in xrange(1, FANOUT + 1):
                # Add hosts
                host = 'h_%s_%s' % (switch, count)
                ip = '10.0.0.%s' % count
                mac = CORES[switch]['dpid'][4:-1] + str(count)
                h = self.addHost(host, ip=ip, mac=mac)
                # Connect hosts to core switches
                self.addLink(h, self.cores[switch])

if __name__ == '__main__':
    topo = MultipleTopo()
    net = Mininet(topo, autoSetMacs=True, xterms=False, controller=RemoteController)
    net.addController('c', ip='128.112.93.28') # localhost:127.0.0.1 vm-to-mac:10.0.2.2 server-to-mac:128.112.93.28
    print "\nHosts configured with IPs, switches pointing to OpenVirteX at 128.112.93.28 port 6633\n"
    net.start()
    raw_input("started, press...")
    #CLI(net)
    #net.stop()
    
