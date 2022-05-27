set xlabel "Data points"
set ylabel "Frequency"
set title "Histogram of data"
#Gnuplot Script For Histogram
Min = -3.24  #max value of your dataset write here
Max = 3.682  #min value of your dataset write here
n = 30             #chose accordingly
width = (Max - Min)/n

hist(x,width) = width/2.0 + width*floor(x/width)

set size sq

plot 'Results/gauss.dat' u (hist($1,width)):(1.0) smooth freq w boxes lc rgb "red" notitle