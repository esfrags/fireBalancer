#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import setLogLevel

class FireTopo(Topo):
    def build(self):
        # Añadir switch
        s1 = self.addSwitch('s1')

        # Añadir hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')

        # Enlazar hosts al switch
        self.addLink(h1, s1)
        self.addLink(h2, s1)

def run():
    topo = FireTopo()
    controller = RemoteController('c0', ip='127.0.0.1', port=6653)

    net = Mininet(topo=topo, controller=controller, switch=OVSSwitch, autoSetMacs=True)

    net.start()
    print("Red levantada. Puedes probar con 'pingall'")
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
