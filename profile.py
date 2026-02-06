""" 
  
## Spanning tree protocol

In this experiment, we will see how broadcast storms can occur in a network with bridge loops (multiple Layer 2 paths between endpoints). Then, we will see how the spanning tree protocol creates a loop-free logical topology in a network with physical loops, so that a broadcast storm cannot occur. We will also see how the spanning tree protocol reacts when the topology changes.

It should take about 1 hour to run this experiment.

Instructions for running the experiment are at:  https://ffund.github.io/tcp-ip-essentials/lab-stp/ """
# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg
# Import the InstaGENI library.
import geni.rspec.igext as ig
# Import the Emulab specific extensions.
import geni.rspec.emulab as emulab

# Create a portal object,
pc = portal.Context()

ALLOWED_VHOST_TYPES = [
    ('any','Any (no restriction)'),
    ('c220g2','c220g2'),
    ('c240g5','c240g5'),
    ('m510','m510'),
]

pc.defineParameter(
    'vhostType',
    'Physical Host Type',
    portal.ParameterType.STRING,
    'c240g5',
    ALLOWED_VHOST_TYPES,
    longDescription='Restrict vhost-0 to a specific node type. Choose a larger type if allocation fails.')

pc.defineParameter(
    'coresPerVM',
    'Cores per VM',
    portal.ParameterType.INTEGER,
    2,
    longDescription='Requested CPU cores for each Xen VM.')

pc.defineParameter(
    'ramPerVM',
    'RAM per VM (MB)',
    portal.ParameterType.INTEGER,
    1024,
    longDescription='Requested RAM in MB for each Xen VM.')

params = pc.bindParameters()
pc.verifyParameters()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Require that all VMs are instantiated on a single physical host.
vhost = pg.RawPC('vhost-0')
vhost.exclusive = True
if params.vhostType and params.vhostType != 'any':
    vhost.hardware_type = params.vhostType
# A Xen-capable host image is required to run XenVMs.
vhost.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//XEN44-64-STD'
request.addResource(vhost)

def mkvm(name):
    node = ig.XenVM(name)
    # Run this VM on the dedicated physical host.
    # NOTE: Leave the VM non-exclusive; exclusivity is provided by vhost-0.
    node.InstantiateOn(vhost)
    node.exclusive = False
    if params.coresPerVM and params.coresPerVM > 0:
        node.cores = params.coresPerVM
    if params.ramPerVM and params.ramPerVM > 0:
        node.ram = params.ramPerVM
    node.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
    node.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JUaUL | bash'))
    request.addResource(node)
    return node

# Node romeo
node_romeo = mkvm('romeo')
iface0 = node_romeo.addInterface('interface-romeo-link3-4', pg.IPv4Address('10.10.0.100','255.255.255.0'))

# Node hamlet
node_hamlet = mkvm('hamlet')
iface1 = node_hamlet.addInterface('interface-hamlet-link1-2', pg.IPv4Address('10.10.0.102','255.255.255.0'))

# Node othello
node_othello = mkvm('othello')
iface2 = node_othello.addInterface('interface-othello-link2-3', pg.IPv4Address('10.10.0.104','255.255.255.0'))

# Node petruchio
node_petruchio = mkvm('petruchio')
iface3 = node_petruchio.addInterface('interface-petruchio-link1-4', pg.IPv4Address('10.10.0.106','255.255.255.0'))

# Node bridge-1
node_bridge_1 = mkvm('bridge-1')
iface4 = node_bridge_1.addInterface('interface-br1-link1-4', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface5 = node_bridge_1.addInterface('interface-br1-link1-2', pg.IPv4Address('0.0.0.0','255.255.255.0'))

# Node bridge-2
node_bridge_2 = mkvm('bridge-2')
iface6 = node_bridge_2.addInterface('interface-br2-link1-2', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface7 = node_bridge_2.addInterface('interface-br2-link2-3', pg.IPv4Address('0.0.0.0','255.255.255.0'))

# Node bridge-3
node_bridge_3 = mkvm('bridge-3')
iface8 = node_bridge_3.addInterface('interface-br3-link2-3', pg.IPv4Address('0.0.0.0','255.255.255.0'))
iface9 = node_bridge_3.addInterface('interface-br3-link3-4', pg.IPv4Address('0.0.0.0','255.255.255.0'))

# Node bridge-4
node_bridge_4 = mkvm('bridge-4')
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
