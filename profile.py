"""Topology where two hosts are directly connected"""

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
node_romeo.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/no-offload.sh'))
iface0 = node_romeo.addInterface('interface-1', pg.IPv4Address('10.10.0.100','255.255.255.0'))

# Node juliet
node_juliet = request.XenVM('juliet')
node_juliet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_juliet.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/no-offload.sh'))
iface1 = node_juliet.addInterface('interface-0', pg.IPv4Address('10.10.0.101','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.addInterface(iface1)
link_0.addInterface(iface0)


# Print the generated rspec
pc.printRequestRSpec(request)
