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

CLUSTER_URNS = {
    'wisconsin': 'urn:publicid:IDN+wisc.cloudlab.us+authority+cm',
    'utah': 'urn:publicid:IDN+utah.cloudlab.us+authority+cm',
    'clemson': 'urn:publicid:IDN+clemson.cloudlab.us+authority+cm',
}

ALLOWED_PLACEMENTS = [
    ('wisconsin:c240g5', 'CloudLab Wisconsin: c240g5'),
    ('wisconsin:c220g2', 'CloudLab Wisconsin: c220g2'),
    ('utah:c240g5', 'CloudLab Utah: c240g5'),
    ('utah:c220g2', 'CloudLab Utah: c220g2'),
    ('clemson:c240g5', 'CloudLab Clemson: c240g5'),
    ('clemson:c220g2', 'CloudLab Clemson: c220g2'),
]

pc.defineParameter(
    'placement',
    'Cluster and Node Type',
    portal.ParameterType.STRING,
    ALLOWED_PLACEMENTS[0],
    ALLOWED_PLACEMENTS,
    longDescription='Select a cluster+node-type combination for vhost-0. All Xen VMs are forced onto that host/site.')

params = pc.bindParameters()
pc.verifyParameters()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()

# Require that all VMs are instantiated on a single physical host.
site_key, host_type = params.placement.split(':', 1)
cm_urn = CLUSTER_URNS.get(site_key)
if not cm_urn:
    pc.reportError(
        portal.ParameterError('Unknown placement selected.', ['placement']),
        immediate=True)

vhost = pg.RawPC('vhost-0')
vhost.exclusive = True
vhost.component_manager_id = cm_urn
vhost.hardware_type = host_type
# A Xen-capable host image is required to run XenVMs.
vhost.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//XEN44-64-STD'
request.addResource(vhost)

def mkvm(name):
    node = ig.XenVM(name)
    node.component_manager_id = cm_urn
    # Run this VM on the dedicated physical host.
    # For InstantiateOn to take effect, the VM must be in dedicated mode.
    node.InstantiateOn(vhost)
    node.exclusive = True
    # Fixed VM sizing (not user-configurable via parameters).
    node.cores = 2
    node.ram = 1024
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
