import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Painleve I ode
ttpainleve = np.linspace(0, 1, 200) ##change later to match graphs

# painleve I system
def painleve(t, y):
    x1, x2 = y
    return [x2, 6*x1**2 + t]

#solution with chosen initial consditions x0,y0=0,0 over T=1
sol_P = solve_ivp(painleve, (0,1), [0,0], t_eval = ttpainleve, rtol = 1e-9, atol = 1e-12)


# Pendulum ode
ttpendulum = np.linspace(0, 10, 1000) ##change later to match graphs

g = 9.80 #constant for gravity
L = 1 #length of pendulum

# let th=theta and o=omega
# pendulum system
def pendulum(t, z):
    th, o = z
    dthdt = o
    dodt = -(g/L) * np.sin(th)
    return [dthdt, dodt]

#solution with chosen initial conditions th0,o0=pi/4,0 over T=10
sol_Pend = solve_ivp(pendulum, (0, 10), [np.pi/4, 0], t_eval = ttpendulum, rtol = 1e-9, atol = 1e-12)
print(sol_Pend.t)

# Lorenz ode
sigma = 10
rho = 28
beta = 8/3

# Lorenz system
def lorenz(t, xyz):
    x, y, z = xyz
    dxdt = sigma * (y-x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

ttlorenz = np.linspace(0, 50, 10000)

#solution with choen inital conditions x0,y0,z0=1,1,1, over T=50
sol_L = solve_ivp(lorenz, (0, 50), [1, 1, 1], t_eval = ttlorenz, rtol = 1e-9, atol = 1e-12) 
