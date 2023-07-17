curl -s https://deb.frrouting.org/frr/keys.asc | sudo apt-key add -
echo deb https://deb.frrouting.org/frr $(lsb_release -s -c) frr-stable | sudo tee -a /etc/apt/sources.list.d/frr.list

sudo apt update
sudo apt -y install frr frr-pythontools nload

sudo sed -i 's/zebrad=no/zebrad=yes/g' /etc/frr/daemons
sudo sed -i 's/ripd=no/ripd=yes/g' /etc/frr/daemons

sudo systemctl restart frr.service