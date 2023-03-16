"""The exercises in this experiment will focus on the confidentiality of network services - to what extent are services that offer remote login, file transfer, or web access, protected from disclosure to unauthorized individuals? In particular, we will consider confidentiality with respect to malicious users who might be eavesdropping on network traffic.

Instructions for running the experiment are at: https://witestlab.poly.edu/blog/secure-applications/"""

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
node_romeo.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_romeo.Site('Site 1')
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface0 = node_romeo.addInterface('interface-1', pg.IPv4Address('10.10.1.100','255.255.255.0'))

# Node router
node_router = request.XenVM('router')
node_router.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_router.Site('Site 1')
node_router.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface1 = node_router.addInterface('interface-0', pg.IPv4Address('10.10.1.1','255.255.255.0'))
iface2 = node_router.addInterface('interface-3', pg.IPv4Address('10.10.2.1','255.255.255.0'))

# Node server
node_server = request.XenVM('server')
node_server.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_server.Site('Site 1')
node_server.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JTQIx | bash'))
iface3 = node_server.addInterface('interface-4', pg.IPv4Address('10.10.2.100','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.disableMACLearning()
link_0.Site('undefined')
link_0.addInterface(iface1)
link_0.addInterface(iface0)

# Link link-1
link_1 = request.Link('link-1')
link_1.disableMACLearning()
link_1.Site('undefined')
link_1.addInterface(iface2)
link_1.addInterface(iface3)


# Print the generated rspec
pc.printRequestRSpec(request)
