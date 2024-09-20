"""This profile is for an experiment on digital experiments.
Instructions:
To run this experiment, follow the instructions at: https://witestlab.poly.edu/blog/p/digital-certificates 
"""

# Import the Portal object.
import geni.portal as portal
# Import the ProtoGENI library.
import geni.rspec.pg as pg

# Create a portal context.
pc = portal.Context()

# Create a Request object to start building the RSpec.
request = pc.makeRequestRSpec()
 
# Add a raw PC to the request.
node = request.RawPC("node")

node_alice = request.XenVM('alice')
node_alice.disk_image = 'urn:publicid:IDN+emulab.net+image+emulab-ops:UBUNTU22-64-STD'
node_alice.addService(rspec.Execute(shell="bash", command="/usr/bin/sudo /usr/bin/apt purge firefox; /usr/bin/sudo /usr/bin/snap remove firefox; /usr/bin/sudo /usr/bin/add-apt-repository ppa:mozillateam/ppa -y ; /usr/bin/sudo /usr/bin/apt -y install firefox-esr; /usr/bin/sudo /usr/bin/ln -s /usr/bin/firefox-esr /usr/local/bin/firefox"))
node_alice.routable_control_ip = True # required for VNC
node_alice.startVNC()

node_ca = request.XenVM('ca')

node_website = request.XenVM('website')

node_ca = request.XenVM('mallory')

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
