in = 'res_parallel_all'

set terminal pdf dashed font "Helvetica, 16" size 5,4 # monochrome
set datafile separator '\t'
#set grid

set xlabel '# of Existing Rules'
set logscale x
#set xrange [640:20480]
#set xtics (128,256,512,1024,2048)
#set xtics (1280,2560,5120,10240)
set xtics nomirror

# plot compile time
set output 'Eval_parallel_compile.pdf'

set key left top

set ylabel 'Time (ms)' offset 2
set logscale y
set yrange [0.001:100000]
set ytics (0.01,0.1,1,10,100,1000,10000)
set ytics nomirror

plot in using 1:3:2:4 with errorbars notitle lt 1 lc rgb 'blue' lw 3,\
	in using 1:3 with line title 'Strawman' lt 1 lc rgb 'blue' lw 10,\
	in using 1:15:14:16 with errorbars notitle lt 1 lc rgb 'red' lw 3,\
	in using 1:15 with line title 'CoVisor' lt 2 lc rgb 'red' lw 10,\
	in using 1:27:26:28 with errorbars notitle lt 1 lc rgb 'green' lw 3,\
	in using 1:27 with line title 'CoVisorACL' lt 3 lc rgb 'green' lw 10

# plot rule-update
set output 'Eval_parallel_rule.pdf'

set key left top

set ylabel '# of Flowmods' offset 2
set logscale y
set yrange [0.1:100000]
set ytics (0.1,1,10,100,1000,10000)
set ytics nomirror

plot in using 1:6:5:7 with errorbars notitle lt 1 lc rgb 'blue' lw 3,\
	in using 1:6 with line title 'Strawman' lt 1 lc rgb 'blue' lw 10,\
	in using 1:18:17:19 with errorbars notitle lt 1 lc rgb 'red' lw 3,\
	in using 1:18 with line title 'CoVisor' lt 2 lc rgb 'red' lw 10,\
	in using 1:30:29:31 with errorbars notitle lt 1 lc rgb 'green' lw 3,\
	in using 1:30 with line title 'CoVisorACL' lt 3 lc rgb 'green' lw 10

# plot total time
set output 'Eval_parallel_total.pdf'

set key left top

set ylabel 'Time (s)' offset 2
set logscale y
set yrange [0.001:1000]
set ytics (0.001,0.01,0.1,1,10,100)
set ytics nomirror

plot in using 1:12:11:13 with errorbars notitle lt 1 lc rgb 'blue' lw 3,\
	in using 1:12 with line title 'Strawman' lt 1 lc rgb 'blue' lw 10,\
	in using 1:24:23:25 with errorbars notitle lt 1 lc rgb 'red' lw 3,\
	in using 1:24 with line title 'CoVisor' lt 2 lc rgb 'red' lw 10,\
	in using 1:36:35:37 with errorbars notitle lt 1 lc rgb 'green' lw 3,\
	in using 1:36 with line title 'CoVisorACL' lt 3 lc rgb 'green' lw 10


