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
echo debconf shared/accepted-oracle-license-v1-1 select true | sudo debconf-set-selections
echo debconf shared/accepted-oracle-license-v1-1 seen true | sudo debconf-set-selections
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu precise main" | sudo tee /etc/apt/sources.list.d/webupd8team-java.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys EEA14886
sudo apt-get -q update
sudo apt-get -y -q install oracle-java7-installer maven virtualbox-guest-additions-iso xorg lxde

# Install FloodLight
if [ ! -f ~/floodlight-source-0.90.tar.gz ];
then
    wget http://floodlight-download.projectfloodlight.org/files/floodlight-source-0.90.tar.gz
    tar xzf floodlight-source-0.90.tar.gz
fi
cd floodlight-0.90
ant
cd -

# Put controllers' configuration in place
CTRL=~/ctrl

mkdir -p ${CTRL}
cat > ${CTRL}/ctrl1.floodlight << EOF
floodlight.modules = net.floodlightcontroller.storage.memory.MemoryStorageSource,\
net.floodlightcontroller.core.FloodlightProvider,\
net.floodlightcontroller.threadpool.ThreadPool,\
net.floodlightcontroller.devicemanager.internal.DeviceManagerImpl,\
net.floodlightcontroller.staticflowentry.StaticFlowEntryPusher,\
net.floodlightcontroller.firewall.Firewall,\
net.floodlightcontroller.forwarding.Forwarding,\
net.floodlightcontroller.jython.JythonDebugInterface,\
net.floodlightcontroller.counter.CounterStore,\
net.floodlightcontroller.perfmon.PktInProcessingTime,\
net.floodlightcontroller.ui.web.StaticWebRoutable
net.floodlightcontroller.restserver.RestApiServer.port = 10001
net.floodlightcontroller.core.FloodlightProvider.openflowport = 10000
net.floodlightcontroller.jython.JythonDebugInterface.port = 6655
net.floodlightcontroller.forwarding.Forwarding.idletimeout = 5
net.floodlightcontroller.forwarding.Forwarding.hardtimeout = 0
EOF

cat > ${CTRL}/ctrl2.floodlight << EOF
floodlight.modules = net.floodlightcontroller.storage.memory.MemoryStorageSource,\
net.floodlightcontroller.core.FloodlightProvider,\
net.floodlightcontroller.threadpool.ThreadPool,\
net.floodlightcontroller.devicemanager.internal.DeviceManagerImpl,\
net.floodlightcontroller.staticflowentry.StaticFlowEntryPusher,\
net.floodlightcontroller.firewall.Firewall,\
net.floodlightcontroller.forwarding.Forwarding,\
net.floodlightcontroller.jython.JythonDebugInterface,\
net.floodlightcontroller.counter.CounterStore,\
net.floodlightcontroller.perfmon.PktInProcessingTime,\
net.floodlightcontroller.ui.web.StaticWebRoutable
net.floodlightcontroller.restserver.RestApiServer.port = 20001
net.floodlightcontroller.core.FloodlightProvider.openflowport = 20000
net.floodlightcontroller.jython.JythonDebugInterface.port = 6656
net.floodlightcontroller.forwarding.Forwarding.idletimeout = 5
net.floodlightcontroller.forwarding.Forwarding.hardtimeout = 0
EOF

cat > ${CTRL}/ctrl3.floodlight << EOF
floodlight.modules = net.floodlightcontroller.storage.memory.MemoryStorageSource,\
net.floodlightcontroller.core.FloodlightProvider,\
net.floodlightcontroller.threadpool.ThreadPool,\
net.floodlightcontroller.devicemanager.internal.DeviceManagerImpl,\
net.floodlightcontroller.staticflowentry.StaticFlowEntryPusher,\
net.floodlightcontroller.firewall.Firewall,\
net.floodlightcontroller.forwarding.Forwarding,\
net.floodlightcontroller.jython.JythonDebugInterface,\
net.floodlightcontroller.counter.CounterStore,\
net.floodlightcontroller.perfmon.PktInProcessingTime,\
net.floodlightcontroller.ui.web.StaticWebRoutable
net.floodlightcontroller.restserver.RestApiServer.port = 30001
net.floodlightcontroller.core.FloodlightProvider.openflowport = 30000
net.floodlightcontroller.jython.JythonDebugInterface.port = 6657
net.floodlightcontroller.forwarding.Forwarding.idletimeout = 5
net.floodlightcontroller.forwarding.Forwarding.hardtimeout = 0
EOF

# Create start-controllers.sh script
cat > ${CTRL}/start-controllers.sh << EOF
#!/bin/bash

kill \`ps ax|grep floodlight|grep -v grep|awk '{print $1}'\`

java -jar ~/floodlight-0.90/target/floodlight.jar -cf ~/ctrl/ctrl1.floodlight > ~/ctrl/ctrl1.log 2>&1 &
java -jar ~/floodlight-0.90/target/floodlight.jar -cf ~/ctrl/ctrl2.floodlight > ~/ctrl/ctrl2.log 2>&1 &
java -jar ~/floodlight-0.90/target/floodlight.jar -cf ~/ctrl/ctrl3.floodlight > ~/ctrl/ctrl3.log 2>&1 &
EOF

# Make sure controllers are started on boot
cat > ~/.profile << EOF
sh ~/ctrl/start-controllers.sh

if [[ -z "$DISPLAY" ]] && [[ $(tty) = /dev/tty1 ]];
then
 . startx
 logout
fi
EOF

# Install OVX source tree
if [ ! -d OpenVirteX ];
then
    git clone https://github.com/OPENNETWORKINGLAB/OpenVirteX.git
else
    cd OpenVirteX
    git pull
    cd -
fi

# Set desktop icons, remove wallpaper, change background color, and disable screensaver
DESKTOP=~/Desktop

mkdir -p ${DESKTOP}

cat > ${DESKTOP}/Eclipse << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Eclipse
Name[en_US]=Eclipse
Icon=/opt/eclipse/icon.xpm
Exec=/usr/bin/eclipse
Comment[en_US]=
EOF

cat > ${DESKTOP}/Terminal << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Terminal
Name[en_US]=Terminal
Icon=konsole
Exec=/usr/bin/x-terminal-emulator
Comment[en_US]=
EOF

cat > ${DESKTOP}/Tutorial << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=OVX Tutorial
Name[en_US]=OVX Tutorial
Icon=internet-web-browser
Exec=/usr/bin/chromium-browser https://github.com/OPENNETWORKINGLAB/OpenVirteX/wiki/Tutorial
Comment[en_US]=
EOF

cat > ${DESKTOP}/Wireshark << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=Wireshark
Name[en_US]=Wireshark
Icon=wireshark
Exec=/usr/bin/wireshark
Comment[en_US]=
EOF

#sudo sed -i 's/wallpaper_mode=1/wallpaper_mode=0/g' /usr/share/lxde/pcmanfm/LXDE.conf
#sudo sed -i 's/desktop_bg=#000000/desktop_bg=#104187/g' /usr/share/lxde/pcmanfm/LXDE.conf
sudo sed -i '/screensaver/d' /etc/xdg/lxsession/LXDE/autostart

# change username, hostname, home dir, etc.
# make sure Ubuntu accepts passwords of length 3
sudo sed -i 's/^password.*pam_unix.*/& minlen=3/' /etc/pam.d/common-password
echo 'ovx:ovx' | sudo chpasswd
sudo mv /home/mininet /home/ovx
sudo sed -i 's/mininet/ovx/g' /etc/group /etc/gshadow /etc/hosts /etc/hostname /etc/passwd /etc/shadow /etc/sudoers


