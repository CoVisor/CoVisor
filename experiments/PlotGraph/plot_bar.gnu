in = 'res'
out = 'Eval_time.pdf'

set terminal pdf dashed font "Helvetica, 20" size 5,4 # monochrome
set output out
set datafile separator '\t'

#set boxwidth 10 absolute
#set size ratio 0.75 # 0.8,0.8 #ratio 1 1,1
set border lw 1

set grid ytics lw 2 lt 1 lc rgb 'black'

set tmargin at screen 0.75

#set key box
set key samplen 2
set key outside c t horizontal #l t #c tm horizontal #outside center top horizontal #right bottom
set key width -4.5

#set yrange [0:6]
#set ytics 0,0.5,3
set ylabel 'Time (second)' offset 2

#set xrange [0:2.5]
#set xtics 0,0.3,1.8
set xtics nomirror
#set xlabel

set style data histogram
set style histogram errorbars lw 3
#set style histogram gap 0
#set style histogram cluster gap 1
set style fill solid border -1

plot in u 3:2:4:xtic(1) t col lt 1 lc rgb 'black' fs pattern 4
#	in u ($6/1000):($5/1000):($7/1000):xtic(1) t col lt 1 lc rgb 'blue' fs pattern 2,\
#	in u ($9/1000):($8/1000):($10/1000):xtic(1) t col lt 1 lc rgb 'red' fs pattern 1

