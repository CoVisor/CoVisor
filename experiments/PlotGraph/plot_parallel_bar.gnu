in = 'res_parallel_all'

set terminal pdf dashed font "Helvetica, 16" size 5,4 # monochrome
set datafile separator '\t'
set border lw 3

set xlabel 'Size of L2 Router Policy (# of Rules)'
set xtics nomirror

set style data histogram
set style histogram errorbars lw 3
set style fill solid border -1

set tmargin at screen 0.77
set key outside c t
set key width -6

# plot compile time
set output 'Eval_parallel_compile.pdf'

set ylabel 'Time (ms)' offset 2
set logscale y
set yrange [0.001:10000]
set ytics (0.001,0.01,0.1,1,10,100,1000,10000)
set ytics nomirror

plot in u 3:2:4:xtic(1) title 'Strawman [10, 50, 90 perc.]' lw 3 lt 1 lc rgb 'black' fs pattern 4,\
    in u 15:14:16:xtic(1) title 'Incremental [10, 50, 90 perc.]' lw 3 lt 1 lc rgb 'blue' fs pattern 2,\
    in u 27:26:28:xtic(1) title 'IncreOpt [10, 50, 90 perc.]' lw 3 lt 1 lc rgb 'red' fs pattern 1

# plot rule-update
set output 'Eval_parallel_rule.pdf'

set ylabel '# of Flowmods' offset 2
set logscale y
set yrange [0.1:10000]
set ytics (0.1,1,10,100,1000,10000)
set ytics nomirror

plot in u 6:5:7:xtic(1) title 'Strawman [10, 50, 90 perc.]' lw 3 lt 1 lc rgb 'black' fs pattern 4,\
    in u 18:17:19:xtic(1) title 'Incremental [10, 50, 90 perc.]' lw 3 lt 1 lc rgb 'blue' fs pattern 2,\
    in u 30:29:31:xtic(1) title 'IncreOpt [10, 50, 90 perc.]' lw 3 lt 1 lc rgb 'red' fs pattern 1

# plot total time
set output 'Eval_parallel_total.pdf'

set ylabel 'Time (s)' offset 2
set logscale y
set yrange [0.001:100]
set ytics (0.001,0.01,0.1,1,10,100)
set ytics nomirror

plot in u 12:11:13:xtic(1) title 'Strawman [10, 50, 90 perc.]' lw 3 lt 1 lc rgb 'black' fs pattern 4,\
    in u 24:23:25:xtic(1) title 'Incremental [10, 50, 90 perc.]' lw 3 lt 1 lc rgb 'blue' fs pattern 2,\
    in u 36:35:37:xtic(1) title 'IncreOpt [10, 50, 90 perc.]' lw 3 lt 1 lc rgb 'red' fs pattern 1

