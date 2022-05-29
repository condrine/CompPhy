set xlabel "x"
set ylabel "Prob. Density"
set title "Gaussian Distribution"

# Gnuplot Script For Histogram
stats "Results/expo_sample.dat" using 1 name "A"
Min = A_min  #max value of your dataset write here
Max = A_max  #min value of your dataset write here
n = 50       # choose accordingly

width = (Max - Min)/n

hist(x,width) = width/2.0 + width*floor(x/width)

set size sq
set style fill solid
plot 'Results/expo_sample.dat' u (hist($1,width)):(1.0/(width*10000)) smooth freq w boxes lc rgb "blue" notitle,\
"Results/expo_exact.dat" u 1:2 w lp lc rgb "red"