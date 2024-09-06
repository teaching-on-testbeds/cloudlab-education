sudo apt update
sudo apt -y install nmap 
sudo apt install -y ca-certificates curl gnupg

sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update

sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

for username in $(ls /users); do sudo usermod -aG docker $username; done

export DOWNLOAD_DIR=/opt/greenbone-community-container 
sudo mkdir -p $DOWNLOAD_DIR
sudo chown $USER $DOWNLOAD_DIR
cd $DOWNLOAD_DIR 
curl -f -L https://greenbone.github.io/docs/latest/_static/docker-compose-22.4.yml -o $DOWNLOAD_DIR/docker-compose.yml


sed -i "s/127.0.0.1/0.0.0.0/g" $DOWNLOAD_DIR/docker-compose.yml

#sed -i "s/# ports/ports/g" $DOWNLOAD_DIR/docker-compose.yml
#sed -i "s/#   - 0.0.0.0/  - 0.0.0.0/g" $DOWNLOAD_DIR/docker-compose.yml

sudo docker compose -f /opt/greenbone-community-container/docker-compose.yml -p greenbone-community-edition pull
