"""

## Operation of a basic Ethernet switch or bridge


In this experimental demonstration of the basic operation of a layer 2 switch/bridge, we will see:

* how to set up a layer 2 bridge on Linux,
* how a bridge or switch learns MAC addresses and updates its forwarding table, and how it forwards, filters, or floods a frame depending on the forwarding table,
* how a bridge or switch reduces collisions by separating each port into a separate collision domain.

It should take about 60-120 minutes to run this experiment.

Instructions for running the experiment are at: https://witestlab.poly.edu/blog/basic-ethernet-switch-operation """

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

# Node bridge
node_bridge = request.XenVM('bridge')
node_bridge.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
iface0 = node_bridge.addInterface('interface-1', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface1 = node_bridge.addInterface('interface-3', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface2 = node_bridge.addInterface('interface-5', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface3 = node_bridge.addInterface('interface-6', pg.IPv4Address('0.0.0.0','255.255.255.0'))

# Node node-1
node_1 = request.XenVM('node-1')
node_1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
iface4 = node_1.addInterface('interface-0', pg.IPv4Address('10.0.0.1','255.255.255.0'))

# Node node-2
node_2 = request.XenVM('node-2')
node_2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
iface5 = node_2.addInterface('interface-2', pg.IPv4Address('10.0.0.2','255.255.255.0'))

# Node node-3
node_3 = request.XenVM('node-3')
node_3.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
iface6 = node_3.addInterface('interface-4', pg.IPv4Address('10.0.0.3','255.255.255.0'))

# Node node-4
node_4 = request.XenVM('node-4')
node_4.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
iface7 = node_4.addInterface('interface-7', pg.IPv4Address('10.0.0.4','255.255.255.0'))

# Link link-1
link_1 = request.Link('link-1')
link_1.disableMACLearning()
iface4.bandwidth = 1000
link_1.addInterface(iface4)
iface0.bandwidth = 1000
link_1.addInterface(iface0)

# Link link-2
link_2 = request.Link('link-2')
link_2.disableMACLearning()
iface5.bandwidth = 1000
link_2.addInterface(iface5)
iface1.bandwidth = 1000
link_2.addInterface(iface1)

# Link link-3
link_3 = request.Link('link-3')
link_3.disableMACLearning()
iface6.bandwidth = 1000
link_3.addInterface(iface6)
iface2.bandwidth = 1000
link_3.addInterface(iface2)

# Link link-4
link_4 = request.Link('link-4')
link_4.disableMACLearning()
iface3.bandwidth = 1000
link_4.addInterface(iface3)
iface7.bandwidth = 1000
link_4.addInterface(iface7)


# Print the generated rspec
pc.printRequestRSpec(request)

