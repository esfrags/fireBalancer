#!/usr/bin/env python3

from mininet.net import Containernet
from mininet.node import Controller, RemoteController, Docker
from mininet.link import TCLink
from mininet.log import setLogLevel, info

def topology():
    net = Containernet(controller=RemoteController)

    info('*** Adding controller\n')
    net.addController('c0', controller=RemoteController, ip='127.0.0.1', port=6653)

    info('*** Adding switch\n')
    s1 = net.addSwitch('s1')

    info('*** Adding Docker containers as hosts\n')
    h1 = net.addDocker('h1', ip='10.0.0.1', dimage="alpine", defaultRoute=None)
    h2 = net.addDocker('h2', ip='10.0.0.2', dimage="alpine", defaultRoute=None)

    info('*** Creating links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s1)

    info('*** Starting network\n')
    net.start()

    info('*** Running CLI\n')
    from mininet.cli import CLI
    CLI(net)

    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    topology()
