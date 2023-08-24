# install and enable Docker & Docker Compose
sudo apt update
sudo apt install -y python3 docker.io docker-compose 
sudo systemctl enable docker --now

# docker needs to be run with SUDO until we add user to group
# will need to either restart or log out / log in for permissions to be read again
sudo usermod -aG docker $USER


# install unzip to extract the vanity address generator... if not already installed
sudo apt-get install unzip

# unzip the generator
unzip mkp224o-master.zip

# prepare project for building
sudo apt install gcc libsodium-dev make autoconf -y
cd ./mkp224o-master
./autogen.sh
# additional option helps it generate addresses faster, otherwise just ./configure
./configure --enable-amd65-51-30k   
# now make it
make


# install the TOR browser... will need restarts between steps.
#sudo apt install flatpak
#flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
#flatpak run com.github.micahflee.torbrowser-launcher

# this version might be outdated.. BUT it doesn't require reboots so automation is easier. 
sudo add-apt-repository ppa:micahflee/ppa
sudo apt install -y torbrowser-launcher

# setup the requirements for hosting a Python Flask website
sudo apt install python3-pip
pip3 install Flask