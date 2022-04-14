# Script Containing Integration Methods

# Forward difference method
def euler(xn, yn, h, func, *args):
    return yn + h*func(yn, xn, *args)

# Multistep method
def multistep(xn, yn, ynn, h, func, *args):
    return ynn + 2*h*func(yn, xn, *args)

# Trapezoidal Predictor Corrector
def trapezoidal_pc(xn, yn, h, func, *args):
    yp = yn + h*func(yn, xn, *args)
    return yn + (h/2)*(func(yn, xn, *args) + func(yp, xn + h, *args))

# Runge Kutta of order 2
def rk2(xn, yn, h, func, *args):
    k = yn + (h/2)*func(yn, xn, *args)
    return yn + h*func(k, xn + h/2, *args)

# Runge Kutta of order 4
def rk4(xn, yn, h, func, *args):
    k1 = func(yn, xn, *args)
    k2 = func(yn + (h/2)*k1, xn + h/2, *args)
    k3 = func(yn + (h/2)*k2, xn + h/2, *args)
    k4 = func(yn + h*k3, xn + h, *args)
    return yn + (h/6)*(k1 + 2*(k2 + k3) + k4)

# Adams-Bashforth of order 4
def ab4(yn, h, f):
    k1 = (55/24)*f[0]
    k2 = (59/24)*f[1]
    k3 = (37/24)*f[2]
    k4 = (3/8)*f[3]
    return yn + h*(k1 - k2 + k3 - k4)
