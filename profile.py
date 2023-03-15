""" 
## Dijkstra's algorithm
In this experiment, we will use Dijkstra's algorithm to find the shortest path from one node in a six-node topology, to all other nodes. We will then install routing rules at each node to implement the shortest-path tree produced by Dijkstra's algorithm.
It should take about 120 minutes to run this experiment.
Instructions for running the experiment are at: https://witestlab.poly.edu/blog/dijkstras-shortest-path-algorithm/ """


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

# Node dijkstra
node_dijkstra = request.XenVM('dijkstra')
node_dijkstra.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_dijkstra.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_dijkstra.addService(pg.Execute('/bin/sh','sudo wget -O /etc/profile.d/link-status-message.sh https://git.io/JUBmU; sudo chmod a+x /etc/profile.d/link-status-message.sh'))
node_dijkstra.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash; wget -O - https://git.io/vSC5r | bash'))
iface0 = node_dijkstra.addInterface('interface-7', pg.IPv4Address('10.10.4.2','255.255.255.0'))
iface1 = node_dijkstra.addInterface('interface-8', pg.IPv4Address('10.10.5.1','255.255.255.0'))

# Node knuth
node_knuth = request.XenVM('knuth')
node_knuth.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_knuth.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_knuth.addService(pg.Execute('/bin/sh','sudo wget -O /etc/profile.d/link-status-message.sh https://git.io/JUBmU; sudo chmod a+x /etc/profile.d/link-status-message.sh'))
node_knuth.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash; wget -O - https://git.io/vSC5r | bash'))
iface2 = node_knuth.addInterface('interface-11', pg.IPv4Address('10.10.6.2','255.255.255.0'))
iface3 = node_knuth.addInterface('interface-12', pg.IPv4Address('10.10.7.1','255.255.255.0'))
iface4 = node_knuth.addInterface('interface-15', pg.IPv4Address('10.10.8.2','255.255.255.0'))

# Node lovelace
node_lovelace = request.XenVM('lovelace')
node_lovelace.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_lovelace.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_lovelace.addService(pg.Execute('/bin/sh','sudo wget -O /etc/profile.d/link-status-message.sh https://git.io/JUBmU; sudo chmod a+x /etc/profile.d/link-status-message.sh'))
node_lovelace.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash; wget -O - https://git.io/vSC5r | bash'))
iface5 = node_lovelace.addInterface('interface-5', pg.IPv4Address('10.10.3.2','255.255.255.0'))
iface6 = node_lovelace.addInterface('interface-6', pg.IPv4Address('10.10.4.1','255.255.255.0'))
iface7 = node_lovelace.addInterface('interface-14', pg.IPv4Address('10.10.8.1','255.255.255.0'))

# Node baran
node_baran = request.XenVM('baran')
node_baran.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_baran.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_baran.addService(pg.Execute('/bin/sh','sudo wget -O /etc/profile.d/link-status-message.sh https://git.io/JUBmU; sudo chmod a+x /etc/profile.d/link-status-message.sh'))
node_baran.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash; wget -O - https://git.io/vSC5r | bash'))
iface8 = node_baran.addInterface('interface-1', pg.IPv4Address('10.10.1.2','255.255.255.0'))
iface9 = node_baran.addInterface('interface-9', pg.IPv4Address('10.10.5.2','255.255.255.0'))

# Node cerf
node_cerf = request.XenVM('cerf')
node_cerf.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_cerf.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_cerf.addService(pg.Execute('/bin/sh','sudo wget -O /etc/profile.d/link-status-message.sh https://git.io/JUBmU; sudo chmod a+x /etc/profile.d/link-status-message.sh'))
node_cerf.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash; wget -O - https://git.io/vSC5r | bash'))
iface10 = node_cerf.addInterface('interface-0', pg.IPv4Address('10.10.1.1','255.255.255.0'))
iface11 = node_cerf.addInterface('interface-3', pg.IPv4Address('10.10.2.2','255.255.255.0'))
iface12 = node_cerf.addInterface('interface-13', pg.IPv4Address('10.10.7.2','255.255.255.0'))

# Node hopper
node_hopper = request.XenVM('hopper')
node_hopper.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_hopper.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install mtr'))
node_hopper.addService(pg.Execute('/bin/sh','sudo wget -O /etc/profile.d/link-status-message.sh https://git.io/JUBmU; sudo chmod a+x /etc/profile.d/link-status-message.sh'))
node_hopper.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash; wget -O - https://git.io/vSC5r | bash'))
iface13 = node_hopper.addInterface('interface-2', pg.IPv4Address('10.10.2.1','255.255.255.0'))
iface14 = node_hopper.addInterface('interface-4', pg.IPv4Address('10.10.3.1','255.255.255.0'))
iface15 = node_hopper.addInterface('interface-10', pg.IPv4Address('10.10.6.1','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
iface10.bandwidth = 100
link_0.addInterface(iface10)
iface8.bandwidth = 100
link_0.addInterface(iface8)

# Link link-1
link_1 = request.Link('link-1')
iface13.bandwidth = 100
link_1.addInterface(iface13)
iface11.bandwidth = 100
link_1.addInterface(iface11)

# Link link-2
link_2 = request.Link('link-2')
iface14.bandwidth = 100
link_2.addInterface(iface14)
iface5.bandwidth = 100
link_2.addInterface(iface5)

# Link link-3
link_3 = request.Link('link-3')
iface6.bandwidth = 100
link_3.addInterface(iface6)
iface0.bandwidth = 100
link_3.addInterface(iface0)

# Link link-4
link_4 = request.Link('link-4')
iface1.bandwidth = 100
link_4.addInterface(iface1)
iface9.bandwidth = 100
link_4.addInterface(iface9)

# Link link-5
link_5 = request.Link('link-5')
iface15.bandwidth = 100
link_5.addInterface(iface15)
iface2.bandwidth = 100
link_5.addInterface(iface2)

# Link link-6
link_6 = request.Link('link-6')
iface3.bandwidth = 100
link_6.addInterface(iface3)
iface12.bandwidth = 100
link_6.addInterface(iface12)

# Link link-7
link_7 = request.Link('link-7')
iface7.bandwidth = 100
link_7.addInterface(iface7)
iface4.bandwidth = 100
link_7.addInterface(iface4)


# Print the generated rspec
pc.printRequestRSpec(request)