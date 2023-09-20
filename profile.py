"""

## Network layer security


The exercises in this experiment will focus on security services offered at the **network layer** of the TCP/IP protocol stack. You will configure a network with a VPN tunnel, and then you will examine the extent to which you are protected from unauthorized eavesdroppers on network traffic, when you use a file transfer application (with and without [application layer confidentiality](https://witestlab.poly.edu/blog/secure-networked-applications/)).

It should take about 60-120 minutes to run this experiment.

Instructions for running the experiment are at: https://witestlab.poly.edu/blog/network-layer-security """

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

# Node romeo
node_romeo = request.XenVM('romeo')
node_romeo.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface0 = node_romeo.addInterface('interface-1', pg.IPv4Address('10.10.1.100','255.255.255.0'))

# Node router-int
node_router_int = request.XenVM('router-int')
node_router_int.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_router_int.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface1 = node_router_int.addInterface('interface-0', pg.IPv4Address('10.10.1.1','255.255.255.0'))
iface2 = node_router_int.addInterface('interface-3', pg.IPv4Address('10.10.2.1','255.255.255.0'))
iface3 = node_router_int.addInterface('interface-6', pg.IPv4Address('10.10.3.1','255.255.255.0'))

# Node server
node_server = request.XenVM('server')
node_server.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_server.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface4 = node_server.addInterface('interface-4', pg.IPv4Address('10.10.2.100','255.255.255.0'))

# Node vpn
node_vpn = request.XenVM('vpn')
node_vpn.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_vpn.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface5 = node_vpn.addInterface('interface-5', pg.IPv4Address('10.10.3.100','255.255.255.0'))
iface6 = node_vpn.addInterface('interface-8', pg.IPv4Address('10.10.4.100','255.255.255.0'))

# Node router-ext
node_router_ext = request.XenVM('router-ext')
node_router_ext.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_router_ext.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface7 = node_router_ext.addInterface('interface-7', pg.IPv4Address('10.10.4.1','255.255.255.0'))
iface8 = node_router_ext.addInterface('interface-10', pg.IPv4Address('10.10.5.1','255.255.255.0'))

# Node juliet
node_juliet = request.XenVM('juliet')
node_juliet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_juliet.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface9 = node_juliet.addInterface('interface-9', pg.IPv4Address('10.10.5.100','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.disableMACLearning()
link_0.addInterface(iface1)
link_0.addInterface(iface0)

# Link link-1
link_1 = request.Link('link-1')
link_1.disableMACLearning()
link_1.addInterface(iface2)
link_1.addInterface(iface4)

# Link link-2
link_2 = request.Link('link-2')
link_2.disableMACLearning()
link_2.addInterface(iface5)
link_2.addInterface(iface3)

# Link link-3
link_3 = request.Link('link-3')
link_3.disableMACLearning()
link_3.addInterface(iface7)
link_3.addInterface(iface6)

# Link link-4
link_4 = request.Link('link-4')
link_4.disableMACLearning()
link_4.addInterface(iface9)
link_4.addInterface(iface8)


# Print the generated rspec
pc.printRequestRSpec(request)

