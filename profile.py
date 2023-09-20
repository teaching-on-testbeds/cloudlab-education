"""Topology for "Redirect traffic to a wrong or fake site with DNS spoofing on a LAN". To run this experiment, refer to the instructions at https://witestlab.poly.edu/blog/redirect-traffic-to-a-wrong-or-fake-site-with-dns-spoofing-on-a-lan/ """

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

# Node client
node_client = request.XenVM('client')
node_client.routable_control_ip = True
node_client.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_client.Site('Site 1')
node_client.startVNC()
node_client.exclusive = False
node_client.addService(pg.Execute(shell="bash", command="/usr/bin/sudo /usr/bin/apt purge firefox; /usr/bin/sudo /usr/bin/snap remove firefox; /usr/bin/sudo /usr/bin/add-apt-repository ppa:mozillateam/ppa -y ; /usr/bin/sudo /usr/bin/apt -y install firefox-esr; /usr/bin/sudo /usr/bin/ln -s /usr/bin/firefox-esr /usr/local/bin/firefox"))
#node_client.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install tightvncserver firefox isc-dhcp-client; sudo wget -O /etc/dhcp/dhclient.conf https://bitbucket.org/ffund/run-my-experiment-on-geni-blog/raw/master/files/dns_spoofing_dhclient.conf'))
iface0 = node_client.addInterface('interface-0', pg.IPv4Address('0.0.0.0','255.255.255.0'))

# Node dns-good
node_dns_good = request.XenVM('dns-good')
node_dns_good.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_dns_good.Site('Site 1')
node_dns_good.exclusive = False
node_dns_good.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install dnsmasq'))
iface1 = node_dns_good.addInterface('interface-1', pg.IPv4Address('10.10.1.2','255.255.255.0'))

# Node attacker
node_attacker = request.XenVM('attacker')
node_attacker.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_attacker.Site('Site 1')
node_attacker.exclusive = False
node_attacker.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install dnsmasq dsniff'))
iface2 = node_attacker.addInterface('interface-2', pg.IPv4Address('10.10.1.254','255.255.255.0'))

# Link link-0
link_0 = request.Link('link-0')
link_0.Site('Site 1')
link_0.addInterface(iface0)
link_0.addInterface(iface1)
link_0.addInterface(iface2)

# Node bank
node_bank = request.XenVM('bank_real')
node_bank.routable_control_ip = True
node_bank.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_bank.exclusive = False
node_bank.Site('Site 2')
node_bank.addService(pg.Execute('/bin/sh','sudo hostname bank'))
node_bank.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install apache2 php libapache2-mod-php; sudo /etc/init.d/apache2 restart; sudo rm /var/www/html/index.html'))


# Node bank
node_bank_f = request.XenVM('bank_fake')
node_bank_f.routable_control_ip = True
node_bank_f.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_bank_f.exclusive = False
node_bank_f.Site('Site 3')
node_bank_f.addService(pg.Execute('/bin/sh','sudo hostname bank'))
node_bank_f.addService(pg.Execute('/bin/sh','sudo apt-get update; sudo apt-get -y install apache2 php libapache2-mod-php; sudo /etc/init.d/apache2 restart; sudo rm /var/www/html/index.html'))

# Print the generated rspec
pc.printRequestRSpec(request)

