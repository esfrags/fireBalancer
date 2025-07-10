#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.node import RemoteController, OVSSwitch
from mininet.topo import Topo
from mininet.cli import CLI
from mininet.log import setLogLevel
import os
import subprocess

class FireTopo(Topo):
    def build(self):
        # Añadir switch
        s1 = self.addSwitch('s1')

        # Añadir hosts
        h1 = self.addHost('h1', ip='10.0.0.1/24')
        h2 = self.addHost('h2', ip='10.0.0.2/24')
        h3 = self.addHost('h3', ip='10.0.0.3/24')

        # Enlazar hosts al switch
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

def run():
    # start onos controller from script
    os.system('onos-app/start_onos.sh')
    
    # start mininet with custom topology
    topo = FireTopo()
    controller = RemoteController('c0', ip='127.0.0.1', port=6653)

    net = Mininet(topo=topo, controller=controller, switch=OVSSwitch, autoSetMacs=True)
    net.start()

    # Forzar OpenFlow13 en el switch
    print("Forzando OpenFlow13 en el switch s1...")
    subprocess.run("ovs-vsctl set bridge s1 protocols=OpenFlow13", shell=True)

    print("Red levantada. Puedes probar con 'pingall'")
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
