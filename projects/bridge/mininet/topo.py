#!/usr/bin/python

#  Copyright 2019-present Open Networking Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import argparse

from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.net import Mininet
from mininet.topo import Topo
from stratum import StratumBmv2Switch


class SingleSwitchTopo(Topo):
    """Single Switch topology"""

    def __init__(self, *args, **kwargs):
        Topo.__init__(self, *args, **kwargs)

        s1 = self.addSwitch('s1')  # gRPC 50001

        h1 = self.addHost('h1', mac="00:00:00:00:00:1A", ip="10.0.0.1/24")
        h2 = self.addHost('h2', mac="00:00:00:00:00:1B", ip="10.0.0.2/24")
        self.addLink(h1, s1)  # port 1
        self.addLink(h2, s1)  # port 2


topos = {'singleswitch': (lambda: SingleSwitchTopo())}


def main():
    net = Mininet(
        topo=TutorialTopo(),
        switch=StratumBmv2Switch,
        controller=None)
    net.start()
    CLI(net)
    net.stop()


if __name__ == "__main__":
    setLogLevel('info')
    main()

