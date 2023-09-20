"""Topology for slowloris demo. To run this experiment, refer to the instructions at https://witestlab.poly.edu/blog/slowloris/ """

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
node_client = request.XenVM('client')
node_client.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_client.exclusive = False
iface0 = node_client.addInterface('interface-r', pg.IPv4Address('10.10.1.1','255.255.255.0'))

# Node juliet
node_server = request.XenVM('server')
node_server.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_server.exclusive = False
iface1 = node_server.addInterface('interface-j', pg.IPv4Address('10.10.1.2','255.255.255.0'))

# Node hamlet
node_attacker = request.XenVM('attacker')
node_attacker.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU18-64-STD'
node_attacker.exclusive = False
iface2 = node_attacker.addInterface('interface-h', pg.IPv4Address('10.10.1.3','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.disableMACLearning()
link_0.addInterface(iface1)
link_0.addInterface(iface0)
link_0.addInterface(iface2)


# Print the generated rspec
pc.printRequestRSpec(request)
