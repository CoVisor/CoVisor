echo "*****************************"
echo "***** VIRTUAL NETWORK 1 *****"
echo "*****************************"
echo ""
echo ""
./ovxctl.py -n createNetwork tcp:192.168.56.101:10000 10.0.0.0 16
./ovxctl.py -n createSwitch 1  00:00:00:00:00:00:00:01
./ovxctl.py -n createPort 1 00:00:00:00:00:00:00:01 1
./ovxctl.py -n createPort 1 00:00:00:00:00:00:00:01 2
./ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:01 1 00:00:00:00:00:01
./ovxctl.py -n connectHost 1 00:a4:23:05:00:00:00:01 2 00:00:00:00:00:02
./ovxctl.py -n startNetwork 1

echo "*****************************"
echo "***** VIRTUAL NETWORK 2 *****"
echo "*****************************"
echo ""
echo ""
./ovxctl.py -n createNetwork tcp:192.168.56.101:20000 10.0.0.0 16
./ovxctl.py -n createSwitch 2  00:00:00:00:00:00:00:01
./ovxctl.py -n createPort 2 00:00:00:00:00:00:00:01 1
./ovxctl.py -n createPort 2 00:00:00:00:00:00:00:01 2
./ovxctl.py -n connectHost 2 00:a4:23:05:00:00:00:01 1 00:00:00:00:00:03
./ovxctl.py -n connectHost 2 00:a4:23:05:00:00:00:01 2 00:00:00:00:00:04
./ovxctl.py -n startNetwork 2

./ovxctl.py -n createPolicy 1+2

