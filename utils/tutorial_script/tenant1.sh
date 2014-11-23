echo "*****************************"
echo "***** VIRTUAL NETWORK *******"
echo "*****************************"
echo ""
echo ""

./ovxctl.py -n createNetwork tcp:192.168.56.101:10000 10.0.0.0 16

./ovxctl.py -n createSwitch 1  00:00:00:00:00:00:01:00
./ovxctl.py -n createSwitch 1  00:00:00:00:00:00:02:00
./ovxctl.py -n createSwitch 1  00:00:00:00:00:00:03:00

./ovxctl.py -n createPort 1 00:00:00:00:00:00:01:00 1
./ovxctl.py -n createPort 1 00:00:00:00:00:00:01:00 5
./ovxctl.py -n createPort 1 00:00:00:00:00:00:02:00 5
./ovxctl.py -n createPort 1 00:00:00:00:00:00:02:00 6
./ovxctl.py -n createPort 1 00:00:00:00:00:00:03:00 5
./ovxctl.py -n createPort 1 00:00:00:00:00:00:03:00 2

./ovxctl.py -n connectLink 1 00:a4:23:05:00:00:00:01 2 00:a4:23:05:00:00:00:02 1 spf 1
./ovxctl.py -n connectLink 1 00:a4:23:05:00:00:00:02 2 00:a4:23:05:00:00:00:03 1 spf 1

./ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:01 1 00:00:00:00:01:01
./ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:03 2 00:00:00:00:03:02

./ovxctl.py -n startNetwork 1

