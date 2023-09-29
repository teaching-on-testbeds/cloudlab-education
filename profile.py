"""
## Static routing

In this experiment, you will observe how routing principles apply when packets are forwarded by a router from one network segment to the next.

It should take about 60-120 minutes to run this experiment.
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
node_romeo.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/delete-default-route.sh | bash'))
iface0 = node_romeo.addInterface('interface-1', pg.IPv4Address('10.10.0.100','255.255.255.0'))

# Node juliet
node_juliet = request.XenVM('juliet')
node_juliet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_juliet.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_juliet.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/delete-default-route.sh | bash'))
iface1 = node_juliet.addInterface('interface-0', pg.IPv4Address('10.10.0.101','255.255.255.0'))

# Node hamlet
node_hamlet = request.XenVM('hamlet')
node_hamlet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_hamlet.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_hamlet.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/delete-default-route.sh | bash'))
iface2 = node_hamlet.addInterface('interface-2', pg.IPv4Address('10.10.0.102','255.255.255.0'))

# Node ophelia
node_ophelia = request.XenVM('ophelia')
node_ophelia.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_ophelia.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_ophelia.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/delete-default-route.sh | bash'))
iface3 = node_ophelia.addInterface('interface-3', pg.IPv4Address('10.10.0.103','255.255.255.0'))

# Node router-1
node_router_1 = request.XenVM('router-1')
node_router_1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_router_1.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_router_1.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/delete-default-route.sh | bash'))
iface4 = node_router_1.addInterface('interface-4', pg.IPv4Address('10.10.0.1','255.255.255.0'))
iface5 = node_router_1.addInterface('interface-11', pg.IPv4Address('10.10.100.1','255.255.255.0'))

# Node router-2
node_router_2 = request.XenVM('router-2')
node_router_2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_router_2.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_router_2.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/delete-default-route.sh | bash'))
iface6 = node_router_2.addInterface('interface-6', pg.IPv4Address('10.10.1.1','255.255.255.0'))
iface7 = node_router_2.addInterface('interface-9', pg.IPv4Address('10.10.100.2','255.255.255.0'))

# Node router-3
node_router_3 = request.XenVM('router-3')
node_router_3.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_router_3.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_router_3.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/delete-default-route.sh | bash'))
iface8 = node_router_3.addInterface('interface-8', pg.IPv4Address('10.10.2.1','255.255.255.0'))
iface9 = node_router_3.addInterface('interface-10', pg.IPv4Address('10.10.100.3','255.255.255.0'))

# Node othello
node_othello = request.XenVM('othello')
node_othello.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU18-64-STD'
node_othello.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/no-auto-routes.sh | bash'))
node_othello.addService(pg.Execute('/bin/sh','wget -O - https://raw.githubusercontent.com/ffund/tcp-ip-essentials/gh-pages/scripts/delete-default-route.sh | bash'))
iface10 = node_othello.addInterface('interface-5', pg.IPv4Address('10.10.1.104','255.255.255.0'))
iface11 = node_othello.addInterface('interface-7', pg.IPv4Address('10.10.2.104','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.disableMACLearning()
iface1.bandwidth = 1000
iface1.bandwidth = 1000
iface1.bandwidth = 1000
iface1.bandwidth = 1000
link_0.addInterface(iface1)
iface0.bandwidth = 1000
iface0.bandwidth = 1000
iface0.bandwidth = 1000
iface0.bandwidth = 1000
link_0.addInterface(iface0)
iface2.bandwidth = 1000
iface2.bandwidth = 1000
iface2.bandwidth = 1000
iface2.bandwidth = 1000
link_0.addInterface(iface2)
iface3.bandwidth = 1000
iface3.bandwidth = 1000
iface3.bandwidth = 1000
iface3.bandwidth = 1000
link_0.addInterface(iface3)
iface4.bandwidth = 1000
iface4.bandwidth = 1000
iface4.bandwidth = 1000
iface4.bandwidth = 1000
link_0.addInterface(iface4)

# Link link-1
link_1 = request.Link('link-1')
link_1.disableMACLearning()
iface10.bandwidth = 1000
link_1.addInterface(iface10)
iface6.bandwidth = 1000
link_1.addInterface(iface6)

# Link link-2
link_2 = request.Link('link-2')
link_2.disableMACLearning()
iface11.bandwidth = 1000
link_2.addInterface(iface11)
iface8.bandwidth = 1000
link_2.addInterface(iface8)

# Link link-3
link_3 = request.Link('link-3')
link_3.disableMACLearning()
iface7.bandwidth = 1000
iface7.bandwidth = 1000
link_3.addInterface(iface7)
iface9.bandwidth = 1000
iface9.bandwidth = 1000
link_3.addInterface(iface9)
iface5.bandwidth = 1000
iface5.bandwidth = 1000
link_3.addInterface(iface5)


# Print the generated rspec
pc.printRequestRSpec(request)
