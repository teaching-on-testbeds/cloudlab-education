"""Topology for simple multicast exercise"""

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

# Node router
node_router = request.XenVM('router')
node_router.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD'
node_router.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/no-offload.sh'))
iface0 = node_router.addInterface('interface-0', pg.IPv4Address('10.10.1.1','255.255.255.0'))
iface1 = node_router.addInterface('interface-3', pg.IPv4Address('10.10.2.1','255.255.255.0'))

# Node romeo
node_romeo = request.XenVM('romeo')
node_romeo.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD'
node_romeo.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/no-offload.sh'))
iface2 = node_romeo.addInterface('interface-1', pg.IPv4Address('10.10.1.100','255.255.255.0'))

# Node juliet
node_juliet = request.XenVM('juliet')
node_juliet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD'
node_juliet.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/no-offload.sh'))
iface3 = node_juliet.addInterface('interface-2', pg.IPv4Address('10.10.1.101','255.255.255.0'))

# Node hamlet
node_hamlet = request.XenVM('hamlet')
node_hamlet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD'
node_hamlet.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/no-offload.sh'))
iface4 = node_hamlet.addInterface('interface-5', pg.IPv4Address('10.10.1.102','255.255.255.0'))

# Node ophelia
node_ophelia = request.XenVM('ophelia')
node_ophelia.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU20-64-STD'
node_ophelia.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/no-offload.sh'))
iface5 = node_ophelia.addInterface('interface-4', pg.IPv4Address('10.10.2.103','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.addInterface(iface0)
link_0.addInterface(iface2)
link_0.addInterface(iface3)
link_0.addInterface(iface4)

# Link link-1
link_1 = request.Link('link-1')
link_1.addInterface(iface1)
link_1.addInterface(iface5)


# Print the generated rspec
pc.printRequestRSpec(request)
