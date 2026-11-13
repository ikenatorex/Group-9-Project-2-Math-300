import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

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

# list of initial conditions for pendulum
initial_conditions_Pend = [[np.pi, 0], [np.pi/4, 0], [np.pi/2, 0], [3*np.pi/4, 0], [3*np.pi/2, 0], [5*np.pi/4, 0], [5*np.pi/2, 0], [2*np.pi, 0]]

# empty list to hold sol_Pend info for each initial condition
sol_Pend_info = []

#solution with chosen initial conditions from list over T=10
for th0, o0 in initial_conditions_Pend:
    sol_Pend = solve_ivp(pendulum, (0, 10), [th0, o0], t_eval = ttpendulum, rtol = 1e-9, atol = 1e-12)
    sol_Pend_info.append([sol_Pend.t, sol_Pend.y[0], sol_Pend.y[1]]) # Returns time, theta, and omega for all initial conditions to info list

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

# empty list to hold sol_L info for each initial condition
sol_L_info = []

# list of initial conditions for lorenz
initial_conditions_L = [[1, 1, 1], [1.000001, 1, 1], [0, 1, 0], [-8, 8, 27], [5, -5, 20]]

#solution with chosen initial conditions x0,y0,z0 over T=50
for x0, y0, z0 in initial_conditions_L:
    sol_L = solve_ivp(lorenz, (0, 50), [1, 1, 1], t_eval = ttlorenz, rtol = 1e-9, atol = 1e-12) 
    sol_L_info.append([sol_L.y, sol_L.y[0], sol_L.y[1], sol_L.y[2]]) # Returns time and all initial conditions for each in the list

