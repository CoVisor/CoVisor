echo "*****************************"
echo "***** VIRTUAL NETWORK *******"
echo "*****************************"
echo ""
echo ""

./ovxctl.py -n createNetwork tcp:192.168.56.101:30000 10.0.0.0 16
./ovxctl.py -n createSwitch 3 00:00:00:00:00:00:05:00,00:00:00:00:00:00:06:00,00:00:00:00:00:00:0A:00
./ovxctl.py -n createPort 3 00:00:00:00:00:00:05:00 1
./ovxctl.py -n createPort 3 00:00:00:00:00:00:06:00 2
./ovxctl.py -n createPort 3 00:00:00:00:00:00:0A:00 3
./ovxctl.py -n connectHost 3 00:a4:23:05:00:00:00:01 1 00:00:00:00:05:01
./ovxctl.py -n connectHost 3 00:a4:23:05:00:00:00:01 2 00:00:00:00:06:02
./ovxctl.py -n connectHost 3 00:a4:23:05:00:00:00:01 3 00:00:00:00:0A:03
./ovxctl.py -n startNetwork 3

