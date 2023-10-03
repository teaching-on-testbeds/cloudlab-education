""" 

## Designing subnets

Your task in this experiment is to set up subnets in a few small LANs to meet given design requirements.

It should take about 60-120 minutes to run this experiment, *after* you work out what part of the address space to assign to each LAN.

"""

#
# NOTE: This code was machine converted. An actual human would not
#       write code like this!
#

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node router-a
node_router_a = request.XenVM('router-a')
node_router_a.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_router_a.Site('Site 1')
node_router_a.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_router_a.addService(pg.Execute('/bin/sh','sudo sysctl -w net.ipv4.ip_forward=1'))
iface0 = node_router_a.addInterface('interface-5', pg.IPv4Address('0.0.0.0','0.0.0.0'))
iface1 = node_router_a.addInterface('interface-0', pg.IPv4Address('10.1.10.1','255.255.255.0'))

# Node router-b
node_router_b = request.XenVM('router-b')
node_router_b.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_router_b.Site('Site 1')
node_router_b.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_router_b.addService(pg.Execute('/bin/sh','sudo sysctl -w net.ipv4.ip_forward=1'))
iface2 = node_router_b.addInterface('interface-2', pg.IPv4Address('10.1.10.2','255.255.255.0'))
iface3 = node_router_b.addInterface('interface-9', pg.IPv4Address('0.0.0.0','0.0.0.0'))

# Node router-c
node_router_c = request.XenVM('router-c')
node_router_c.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_router_c.Site('Site 1')
node_router_c.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_router_c.addService(pg.Execute('/bin/sh','sudo sysctl -w net.ipv4.ip_forward=1'))
iface4 = node_router_c.addInterface('interface-3', pg.IPv4Address('10.1.10.3','255.255.255.0'))
iface5 = node_router_c.addInterface('interface-13', pg.IPv4Address('0.0.0.0','0.0.0.0'))

# Node juliet
node_juliet = request.XenVM('juliet')
node_juliet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_juliet.Site('Site 1')
node_juliet.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_juliet.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSWTX | bash'))
iface6 = node_juliet.addInterface('interface-6', pg.IPv4Address('0.0.0.0','0.0.0.0'))

# Node romeo
node_romeo = request.XenVM('romeo')
node_romeo.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_romeo.Site('Site 1')
node_romeo.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSWTX | bash'))
iface7 = node_romeo.addInterface('interface-4', pg.IPv4Address('0.0.0.0','0.0.0.0'))

# Node othello
node_othello = request.XenVM('othello')
node_othello.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_othello.Site('Site 1')
node_othello.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_othello.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSWTX | bash'))
iface8 = node_othello.addInterface('interface-8', pg.IPv4Address('0.0.0.0','0.0.0.0'))

# Node desdemona
node_desdemona = request.XenVM('desdemona')
node_desdemona.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_desdemona.Site('Site 1')
node_desdemona.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_desdemona.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSWTX | bash'))
iface9 = node_desdemona.addInterface('interface-10', pg.IPv4Address('0.0.0.0','0.0.0.0'))

# Node ophelia
node_ophelia = request.XenVM('ophelia')
node_ophelia.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_ophelia.Site('Site 1')
node_ophelia.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_ophelia.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSWTX | bash'))
iface10 = node_ophelia.addInterface('interface-14', pg.IPv4Address('0.0.0.0','0.0.0.0'))

# Node hamlet
node_hamlet = request.XenVM('hamlet')
node_hamlet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_hamlet.Site('Site 1')
node_hamlet.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_hamlet.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSWTX | bash'))
iface11 = node_hamlet.addInterface('interface-12', pg.IPv4Address('0.0.0.0','0.0.0.0'))

# Link link-1 between routers
link_1 = request.Link('link-1')
link_1.disableMACLearning()
iface2.bandwidth = 1000
link_1.addInterface(iface2)
iface4.bandwidth = 1000
link_1.addInterface(iface4)
iface1.bandwidth = 1000
link_1.addInterface(iface1)

# Link link-2 LAN A
link_2 = request.Link('link-2')
link_2.disableMACLearning()
iface7.bandwidth = 1000
link_2.addInterface(iface7)
iface0.bandwidth = 1000
link_2.addInterface(iface0)
iface6.bandwidth = 1000
link_2.addInterface(iface6)

# Link link-3 LAN B
link_3 = request.Link('link-3')
link_3.disableMACLearning()
iface3.bandwidth = 1000
link_3.addInterface(iface3)
iface10.bandwidth = 1000
link_3.addInterface(iface10)
iface11.bandwidth = 1000
link_3.addInterface(iface11)

# Link link-4 LAN C
link_4 = request.Link('link-4')
link_4.disableMACLearning()
iface5.bandwidth = 1000
link_4.addInterface(iface5)
iface8.bandwidth = 1000
link_4.addInterface(iface8)
iface9.bandwidth = 1000
link_4.addInterface(iface9)

# Print the generated rspec
pc.printRequestRSpec(request)

