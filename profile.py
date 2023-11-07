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

# Node source1
node_source1 = request.XenVM('source1')
node_source1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_source1.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_source1.addService(pg.Execute('/bin/sh','sudo apt update; sudo apt -y install vlc'))
iface0 = node_source1.addInterface('interface-0', pg.IPv4Address('10.10.101.2','255.255.255.0'))

# Node rp
node_rp = request.XenVM('rp')
node_rp.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_rp.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_rp.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JYhs5 | bash'))
iface1 = node_rp.addInterface('interface-7', pg.IPv4Address('10.10.1.100','255.255.255.0'))

# Node fhr1
node_fhr1 = request.XenVM('fhr1')
node_fhr1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_fhr1.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_fhr1.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JYhs5 | bash'))
iface2 = node_fhr1.addInterface('interface-1', pg.IPv4Address('10.10.101.1','255.255.255.0'))
iface3 = node_fhr1.addInterface('interface-33', pg.IPv4Address('10.10.11.2','255.255.255.0'))

# Node fhr2
node_fhr2 = request.XenVM('fhr2')
node_fhr2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_fhr2.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_fhr2.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JYhs5 | bash'))
iface4 = node_fhr2.addInterface('interface-9', pg.IPv4Address('10.10.102.1','255.255.255.0'))
iface5 = node_fhr2.addInterface('interface-35', pg.IPv4Address('10.10.12.2','255.255.255.0'))

# Node cr1
node_cr1 = request.XenVM('cr1')
node_cr1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_cr1.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_cr1.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JYhs5 | bash'))
iface6 = node_cr1.addInterface('interface-6', pg.IPv4Address('10.10.1.1','255.255.255.0'))
iface7 = node_cr1.addInterface('interface-34', pg.IPv4Address('10.10.11.1','255.255.255.0'))
iface8 = node_cr1.addInterface('interface-36', pg.IPv4Address('10.10.12.1','255.255.255.0'))

# Node source2
node_source2 = request.XenVM('source2')
node_source2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_source2.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_source2.addService(pg.Execute('/bin/sh','sudo apt update; sudo apt -y install vlc'))
iface9 = node_source2.addInterface('interface-8', pg.IPv4Address('10.10.102.2','255.255.255.0'))

# Node romeo
node_romeo = request.XenVM('romeo')
node_romeo.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_romeo.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_romeo.addService(pg.Execute('/bin/sh','sudo apt update; sudo apt -y install vlc'))
iface10 = node_romeo.addInterface('interface-21', pg.IPv4Address('10.10.103.2','255.255.255.0'))

# Node juliet
node_juliet = request.XenVM('juliet')
node_juliet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_juliet.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_juliet.addService(pg.Execute('/bin/sh','sudo apt update; sudo apt -y install vlc'))
iface11 = node_juliet.addInterface('interface-23', pg.IPv4Address('10.10.103.3','255.255.255.0'))

# Node hamlet
node_hamlet = request.XenVM('hamlet')
node_hamlet.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_hamlet.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_hamlet.addService(pg.Execute('/bin/sh','sudo apt update; sudo apt -y install vlc'))
iface12 = node_hamlet.addInterface('interface-24', pg.IPv4Address('10.10.104.2','255.255.255.0'))

# Node ophelia
node_ophelia = request.XenVM('ophelia')
node_ophelia.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_ophelia.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_ophelia.addService(pg.Execute('/bin/sh','sudo apt update; sudo apt -y install vlc'))
iface13 = node_ophelia.addInterface('interface-38', pg.IPv4Address('10.10.104.3','255.255.255.0'))

# Node lhr1
node_lhr1 = request.XenVM('lhr1')
node_lhr1.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_lhr1.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_lhr1.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JYhs5 | bash'))
iface14 = node_lhr1.addInterface('interface-22', pg.IPv4Address('10.10.103.1','255.255.255.0'))
iface15 = node_lhr1.addInterface('interface-30', pg.IPv4Address('10.10.21.2','255.255.255.0'))

# Node lhr2
node_lhr2 = request.XenVM('lhr2')
node_lhr2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_lhr2.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_lhr2.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JYhs5 | bash'))
iface16 = node_lhr2.addInterface('interface-25', pg.IPv4Address('10.10.104.1','255.255.255.0'))
iface17 = node_lhr2.addInterface('interface-31', pg.IPv4Address('10.10.22.2','255.255.255.0'))

# Node cr2
node_cr2 = request.XenVM('cr2')
node_cr2.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU20-64-STD'
node_cr2.addService(pg.Execute('/bin/sh','wget -O - https://git.io/vSLc2 | bash'))
node_cr2.addService(pg.Execute('/bin/sh','wget -O - https://git.io/JYhs5 | bash'))
iface18 = node_cr2.addInterface('interface-28', pg.IPv4Address('10.10.1.2','255.255.255.0'))
iface19 = node_cr2.addInterface('interface-29', pg.IPv4Address('10.10.21.1','255.255.255.0'))
iface20 = node_cr2.addInterface('interface-32', pg.IPv4Address('10.10.22.1','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.addInterface(iface0)
link_0.addInterface(iface2)

# Link link-3
link_3 = request.Link('link-3')
link_3.addInterface(iface6)
link_3.addInterface(iface1)
link_3.addInterface(iface18)

# Link link-4
link_4 = request.Link('link-4')
link_4.addInterface(iface9)
link_4.addInterface(iface4)

# Link link-5
link_5 = request.Link('link-5')
link_5.addInterface(iface10)
link_5.addInterface(iface14)
link_5.addInterface(iface11)

# Link link-6
link_6 = request.Link('link-6')
link_6.addInterface(iface12)
link_6.addInterface(iface16)
link_6.addInterface(iface13)

# Link link-9
link_9 = request.Link('link-9')
link_9.addInterface(iface19)
link_9.addInterface(iface15)

# Link link-10
link_10 = request.Link('link-10')
link_10.addInterface(iface17)
link_10.addInterface(iface20)

# Link link-11
link_11 = request.Link('link-11')
link_11.addInterface(iface3)
link_11.addInterface(iface7)

# Link link-12
link_12 = request.Link('link-12')
link_12.addInterface(iface5)
link_12.addInterface(iface8)


# Print the generated rspec
pc.printRequestRSpec(request)
