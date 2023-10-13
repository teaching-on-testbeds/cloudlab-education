"""This is a basic profile with two hosts connected by a router.
Instructions:
Wait for the profile instance to start, then log in to each node by clicking on it in the topology and choosing the `shell` menu item. 
"""

"""This is a basic profile with two hosts connected by a router.
Instructions:
Wait for the profile instance to start, then log in to each node by clicking on it in the topology and choosing the `shell` menu item.
"""


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
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/cloudlab/scripts/no-offload.sh | bash'))
iface0 = node_romeo.addInterface('interface-1', pg.IPv4Address('10.0.1.100','255.255.255.0'))
node_romeo.exclusive = False

# Node juliet
node_juliet = request.XenVM('juliet')
node_juliet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_juliet.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/cloudlab/scripts/no-offload.sh | bash'))
iface1 = node_juliet.addInterface('interface-3', pg.IPv4Address('10.0.2.100','255.255.255.0'))
node_juliet.exclusive = False

# Node router
node_router = request.XenVM('router')
node_router.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_router.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/cloudlab/scripts/no-offload.sh | bash'))
iface2 = node_router.addInterface('interface-0', pg.IPv4Address('10.0.1.10','255.255.255.0'))
iface3 = node_router.addInterface('interface-2', pg.IPv4Address('10.0.2.10','255.255.255.0'))
node_router.exclusive = False

# Link link-0
link_0 = request.Link('link-0')
link_0.addInterface(iface2)
link_0.addInterface(iface0)

# Link link-1
link_1 = request.Link('link-1')
link_1.addInterface(iface3)
link_1.addInterface(iface1)


# Print the generated rspec
pc.printRequestRSpec(request)

