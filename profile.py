"""Topology for Dynamic Routing RIP and ICMP experiments"""

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
node_romeo.Site('Site 1')
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
iface0 = node_romeo.addInterface('interface-14', pg.IPv4Address('10.10.61.100','255.255.255.0'))

# Node hamlet
node_hamlet = request.XenVM('hamlet')
node_hamlet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_hamlet.Site('Site 1')
node_hamlet.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
iface1 = node_hamlet.addInterface('interface-2', pg.IPv4Address('10.10.62.100','255.255.255.0'))

# Node othello
node_othello = request.XenVM('othello')
node_othello.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_othello.Site('Site 1')
node_othello.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
iface2 = node_othello.addInterface('interface-4', pg.IPv4Address('10.10.63.100','255.255.255.0'))

# Node petruchio
node_petruchio = request.XenVM('petruchio')
node_petruchio.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_petruchio.Site('Site 1')
node_petruchio.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
iface3 = node_petruchio.addInterface('interface-11', pg.IPv4Address('10.10.64.100','255.255.255.0'))

# Node router-3
node_router_3 = request.XenVM('router-3')
node_router_3.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_router_3.Site('Site 1')
node_router_3.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_router_3.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/rip-router-frr-setup.sh'))
iface4 = node_router_3.addInterface('interface-12', pg.IPv4Address('10.10.64.3','255.255.255.0'))
iface5 = node_router_3.addInterface('interface-8', pg.IPv4Address('10.10.63.3','255.255.255.0'))

# Node router-2
node_router_2 = request.XenVM('router-2')
node_router_2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_router_2.Site('Site 1')
node_router_2.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_router_2.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/rip-router-frr-setup.sh'))
iface6 = node_router_2.addInterface('interface-3', pg.IPv4Address('10.10.63.2','255.255.255.0'))
iface7 = node_router_2.addInterface('interface-16', pg.IPv4Address('10.10.62.2','255.255.255.0'))

# Node router-1
node_router_1 = request.XenVM('router-1')
node_router_1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_router_1.Site('Site 1')
node_router_1.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_router_1.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/rip-router-frr-setup.sh'))
iface8 = node_router_1.addInterface('interface-18', pg.IPv4Address('10.10.61.1','255.255.255.0'))
iface9 = node_router_1.addInterface('interface-1', pg.IPv4Address('10.10.62.1','255.255.255.0'))

# Node router-4
node_router_4 = request.XenVM('router-4')
node_router_4.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops//UBUNTU22-64-STD'
node_router_4.Site('Site 1')
node_router_4.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_router_4.addService(pg.Execute('/bin/sh','bash /local/repository/scripts/rip-router-frr-setup.sh'))
iface10 = node_router_4.addInterface('interface-9', pg.IPv4Address('10.10.64.4','255.255.255.0'))
iface11 = node_router_4.addInterface('interface-13', pg.IPv4Address('10.10.61.4','255.255.255.0'))

# Link link-3-4
link_3_4 = request.Link('link-3-4')
link_3_4.Site('undefined')
link_3_4.addInterface(iface4)
link_3_4.addInterface(iface10)
link_3_4.addInterface(iface3)

# Link link-1
link_1 = request.Link('link-1')
link_1.Site('undefined')
link_1.addInterface(iface11)
link_1.addInterface(iface0)
link_1.addInterface(iface8)

# Link link-2
link_2 = request.Link('link-2')
link_2.Site('undefined')
link_2.addInterface(iface9)
link_2.addInterface(iface1)
link_2.addInterface(iface7)

# Link link-2-3
link_2_3 = request.Link('link-2-3')
link_2_3.Site('undefined')
link_2_3.addInterface(iface6)
link_2_3.addInterface(iface2)
link_2_3.addInterface(iface5)


# Print the generated rspec
pc.printRequestRSpec(request)
