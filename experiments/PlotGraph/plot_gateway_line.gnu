in = 'res_gateway_all'

set terminal pdf dashed font "Helvetica, 16" size 5,4 # monochrome
set datafile separator '\t'
set border lw 3
#set grid ytics lw 2 lt 1 lc rgb 'gray'

set key off

set logscale y
set ytics nomirror
set xtics nomirror
set xlabel '# of IP Prefixes'

set style data histogram
set style histogram errorbars lw 3
set style fill solid border -1

set output 'Eval_gateway_compile.pdf'
set yrange [0.1:1000]
set ylabel 'Time (ms)' offset 2
plot in u 3:2:4:xtic(1) t col lw 3 lt 1 lc rgb 'blue' fs pattern 2

set output 'Eval_gateway_rule.pdf'
set yrange [100:100000]
set ylabel '# of Flowmods' offset 2
plot in u 6:5:7:xtic(1) t col lw 3 lt 1 lc rgb 'blue' fs pattern 2

set output 'Eval_gateway_total.pdf'
set yrange [0.1:1000]
set ylabel 'Time (s)' offset 2
plot in u 12:11:13:xtic(1) t col lw 3 lt 1 lc rgb 'blue' fs pattern 2

