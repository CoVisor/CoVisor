echo "*****************************"
echo "***** VIRTUAL NETWORK *******"
echo "*****************************"
echo ""
echo ""

./ovxctl.py -n stopNetwork 3
./ovxctl.py -n createSwitch 3 00:00:00:00:00:00:08:00
./ovxctl.py -n createPort 3 00:00:00:00:00:00:05:00 5
./ovxctl.py -n createPort 3 00:00:00:00:00:00:08:00 6
./ovxctl.py -n connectLink 3 00:a4:23:05:00:00:00:01 4 00:a4:23:05:00:00:00:02 1 spf 1
./ovxctl.py -n createPort 3 00:00:00:00:00:00:08:00 4
./ovxctl.py -n connectHost 3 00:a4:23:05:00:00:00:02 2 00:00:00:00:08:04
./ovxctl.py -n startNetwork 3

