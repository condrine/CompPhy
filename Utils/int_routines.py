# Script Containing Integration Methods

# Forward difference method
def euler(xn, yn, h, func):
    return yn + h*func(yn, xn)

# Multistep method
def multistep(xn, yn, ynn, h, func):
    return ynn + 2*h*func(yn, xn)

# Trapezoidal Predictor Corrector
def trapezoidal_pc(xn, yn, h, func):
    yp = yn + h*func(yn, xn)
    return yn + (h/2)*(func(yn, xn) + func(yp, xn + h))

# Runge Kutta of order 2
def rk2(xn, yn, h, func):
    k = yn + (h/2)*func(yn, xn)
    return yn + h*func(k, xn + h/2)

# Runge Kutta of order 4
def rk4(xn, yn, h, func):
    k1 = func(yn, xn)
    k2 = func(yn + (h/2)*k1, xn + h/2)
    k3 = func(yn + (h/2)*k2, xn + h/2)
    k4 = func(yn + h*k3, xn + h)
    return yn + (h/6)*(k1 + 2*(k2 + k3) + k4)

# Adams-Bashforth of order 4
def ab4(yn, h, f):
    k1 = (55/24)*f[0]
    k2 = (59/24)*f[1]
    k3 = (37/24)*f[2]
    k4 = (3/8)*f[3]
    return yn + h*(k1 - k2 + k3 - k4)
