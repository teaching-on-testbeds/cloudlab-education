""" 
  
## Spanning tree protocol

In this experiment, we will see how broadcast storms can occur in a network with bridge loops (multiple Layer 2 paths between endpoints). Then, we will see how the spanning tree protocol creates a loop-free logical topology in a network with physical loops, so that a broadcast storm cannot occur. We will also see how the spanning tree protocol reacts when the topology changes.

It should take about 1 hour to run this experiment.

Instructions for running the experiment are at: https://witestlab.poly.edu/blog/the-spanning-tree-protocol/ """
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
node_romeo.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JUaUL | bash'))
iface0 = node_romeo.addInterface('interface-romeo-link3-4', pg.IPv4Address('10.10.0.100','255.255.255.0'))

# Node hamlet
node_hamlet = request.XenVM('hamlet')
node_hamlet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_hamlet.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JUaUL | bash'))
iface1 = node_hamlet.addInterface('interface-hamlet-link1-2', pg.IPv4Address('10.10.0.102','255.255.255.0'))

# Node othello
node_othello = request.XenVM('othello')
node_othello.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_othello.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JUaUL | bash'))
iface2 = node_othello.addInterface('interface-othello-link2-3', pg.IPv4Address('10.10.0.104','255.255.255.0'))

# Node petruchio
node_petruchio = request.XenVM('petruchio')
node_petruchio.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_petruchio.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JUaUL | bash'))
iface3 = node_petruchio.addInterface('interface-petruchio-link1-4', pg.IPv4Address('10.10.0.106','255.255.255.0'))

# Node bridge-1
node_bridge_1 = request.XenVM('bridge-1')
node_bridge_1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_bridge_1.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JUaUL | bash'))
iface4 = node_bridge_1.addInterface('interface-br1-link1-4', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface5 = node_bridge_1.addInterface('interface-br1-link1-2', pg.IPv4Address('0.0.0.0','255.255.255.0'))

# Node bridge-2
node_bridge_2 = request.XenVM('bridge-2')
node_bridge_2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_bridge_2.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JUaUL | bash'))
iface6 = node_bridge_2.addInterface('interface-br2-link1-2', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface7 = node_bridge_2.addInterface('interface-br2-link2-3', pg.IPv4Address('0.0.0.0','255.255.255.0'))

# Node bridge-3
node_bridge_3 = request.XenVM('bridge-3')
node_bridge_3.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_bridge_3.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JUaUL | bash'))
iface8 = node_bridge_3.addInterface('interface-br3-link2-3', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface9 = node_bridge_3.addInterface('interface-br3-link3-4', pg.IPv4Address('0.0.0.0','255.255.255.0'))

# Node bridge-4
node_bridge_4 = request.XenVM('bridge-4')
node_bridge_4.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_bridge_4.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JUaUL | bash'))
iface10 = node_bridge_4.addInterface('interface-br4-link1-4', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface11 = node_bridge_4.addInterface('interface-br4-link3-4', pg.IPv4Address('0.0.0.0','255.255.255.0'))

# Link link-1-2
link_1_2 = request.Link('link-1-2')
link_1_2.disableMACLearning()
link_1_2.addInterface(iface5)
link_1_2.addInterface(iface6)
link_1_2.addInterface(iface1)

# Link link-2-3
link_2_3 = request.Link('link-2-3')
link_2_3.disableMACLearning()
link_2_3.addInterface(iface7)
link_2_3.addInterface(iface8)
link_2_3.addInterface(iface2)

# Link link-1-4
link_1_4 = request.Link('link-1-4')
link_1_4.disableMACLearning()
link_1_4.addInterface(iface4)
link_1_4.addInterface(iface10)
link_1_4.addInterface(iface3)

# Link link-3-4
link_3_4 = request.Link('link-3-4')
link_3_4.disableMACLearning()
link_3_4.addInterface(iface11)
link_3_4.addInterface(iface0)
link_3_4.addInterface(iface9)


# Print the generated rspec
pc.printRequestRSpec(request)
