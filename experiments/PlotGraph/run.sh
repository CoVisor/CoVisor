#!/bin/bash

scp server:~/xin-flowmaster/OpenVirteX/experiments/PlotGraph/res_gateway_* ./
python process.py
gnuplot plot_gateway_bar.gnu

