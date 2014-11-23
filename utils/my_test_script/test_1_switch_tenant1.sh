#CONTROLLERIP=192.168.56.101
CONTROLLERIP=128.112.92.74

echo "*****************************"
echo "***** VIRTUAL NETWORK *******"
echo "*****************************"
echo ""
echo ""
./ovxctl.py -n createNetwork tcp:${CONTROLLERIP}:10000 10.0.0.0 16
./ovxctl.py -n createSwitch 1  00:00:00:00:00:00:00:01
./ovxctl.py -n createPort 1 00:00:00:00:00:00:00:01 1
./ovxctl.py -n createPort 1 00:00:00:00:00:00:00:01 2
./ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:01 1 00:00:00:00:00:01
./ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:01 2 00:00:00:00:00:02
./ovxctl.py -n startNetwork 1

