#!/bin/bash
#
# Based on script by Brian O'Connor for ONOS VM
# For more info, see https://bitbucket.org/bocon13/onos-setup/overview
#
# To make a VM
# 1) Download mininet VM
# 2) Copy install-ovx-vm.sh to /home/mininet
# 2) Login with mininet:mininet and run: sh install-ovx-vm.sh
# Or use VBManage
# 3) Login with ovx:ovx

# Unattended Oracle Java install
#echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
#echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
#echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | sudo tee /etc/apt/sources.list.d/webupd8team-java.list
#sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
#sudo apt-get -q update
#sudo apt-get -y -q install oracle-java7-installer maven virtualbox-guest-additions-iso xorg lxde

# Install FloodLight
if [ ! -f floodlight-source-0.90.tar.gz ];
then
    wget http://floodlight-download.projectfloodlight.org/files/floodlight-source-0.90.tar.gz
    tar xzf floodlight-source-0.90.tar.gz
fi
cd floodlight-0.90
ant
cd -

