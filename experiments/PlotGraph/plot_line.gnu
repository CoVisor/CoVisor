in = 'resline'
out = 'Eval_line.pdf'

set terminal pdf dashed font "Helvetica, 20" size 5,4 # monochrome
set output out
set datafile separator '\t'

plot in using 1:3:2:4 with errorbars title "Strawman",\
	in using 1:3 with line notitle,\
	in using 1:6:5:7 with errorbars title "CoVisor",\
	in using 1:6 with line notitle

