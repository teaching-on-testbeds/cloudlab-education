""" 
  
## Network reconnaissance and vulnerability assessment

In this experiment, we will practice network reconnaissance: gathering information about a network, such as the network structure, applications and services, and vulnerabilities.
It should take about 1 hour to run this experiment.
Instructions for running the experiment are at: https://witestlab.poly.edu/blog/network-reconnaissance-and-vulnerability-assessment/ """
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Node recon
node_recon = request.XenVM('recon')
node_recon.routable_control_ip = True
node_recon.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_recon.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JtNm8 | bash'))
iface0 = node_recon.addInterface('interface-1', pg.IPv4Address('10.10.1.2','255.255.255.0'))

# Node router
node_router = request.XenVM('router')
node_router.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD'
iface1 = node_router.addInterface('interface-0', pg.IPv4Address('10.10.1.1','255.255.255.0'))
iface2 = node_router.addInterface('interface-3', pg.IPv4Address('10.10.2.1','255.255.255.0'))

# Node target1
node_target1 = request.XenVM('target1')
node_target1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD'
node_target1.addService(pg.Execute('/bin/sh','sudo iptables -A INPUT -i eth1 -p ICMP -j DROP'))
node_target1.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install apache2'))
iface3 = node_target1.addInterface('interface-2', pg.IPv4Address('10.10.2.45','255.255.255.0'))

# Node target2
node_target2 = request.XenVM('target2')
node_target2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD'
node_target2.addService(pg.Execute('/bin/sh','wget -O - https://git.io/Jt1D6 | bash'))
iface4 = node_target2.addInterface('interface-8', pg.IPv4Address('10.10.2.97','255.255.255.0'))

# Node target3
node_target3 = request.XenVM('target3')
node_target3.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU16-64-STD'
node_target3.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo DEBIAN_FRONTEND=noninteractive apt-get -y install postfix'))
iface5 = node_target3.addInterface('interface-9', pg.IPv4Address('10.10.2.112','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.addInterface(iface1)
link_0.addInterface(iface0)

# Link link-1
link_1 = request.Link('link-1')
link_1.addInterface(iface3)
link_1.addInterface(iface2)
link_1.addInterface(iface4)
link_1.addInterface(iface5)

