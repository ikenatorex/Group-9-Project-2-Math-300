import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Pendulum ode
ttpendulum = np.linspace(0, 10, 1000)

g = 9.80 # Constant for gravity
L = 1 # Length of pendulum

# Let th=theta and o=omega
# Pendulum system
def pendulum(t, z):
    th, o = z
    dthdt = o
    dodt = -(g/L) * np.sin(th)
    return [dthdt, dodt]

# List of initial conditions for pendulum
initial_conditions_Pend = [[np.pi, 0], [np.pi/4, 0], [np.pi/2, 0], [3*np.pi/4, 0], [3*np.pi/2, 0], [5*np.pi/4, 0], [5*np.pi/2, 0], [2*np.pi, 0]]

# Empty list to hold sol_Pend info for each initial condition
sol_Pend_info = []

# Solution with chosen initial conditions from list over T=10
for th0, o0 in initial_conditions_Pend:
    sol_Pend = solve_ivp(pendulum, (0, 10), [th0, o0], t_eval = ttpendulum, rtol = 1e-9, atol = 1e-12)
    sol_Pend_info.append([sol_Pend.t, sol_Pend.y[0], sol_Pend.y[1]]) # Returns time, theta, and omega for all initial conditions to sol_Pend_info

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

# Empty list to hold sol_L info for each initial condition
sol_L_info = []

# List of initial conditions for lorenz
initial_conditions_L = [[0, 0, 0], [1, 1, 1], [1.000001, 1, 1], [0, 1, 0], [-8, 8, 27], [5, -5, 20]]

# Solution with chosen initial conditions x0,y0,z0 over T=50
for x0, y0, z0 in initial_conditions_L:
    sol_L = solve_ivp(lorenz, (0, 50), [x0, y0, z0], t_eval = ttlorenz, rtol = 1e-9, atol = 1e-12) 
    sol_L_info.append([sol_L.t, sol_L.y[0], sol_L.y[1], sol_L.y[2]]) # Returns time and all initial conditions for each to sol_L_info

# Van der Pol(VDP) ode
# Set damping to 1
u = 1

# VDP system
def VDP(t, z):
    x, y = z
    dxdt = y
    dydt = u * (1 - x**2) * y - x
    return [dxdt, dydt]

ttVDP = np.linspace(0, 40, 1000)

# Empty list to hold sol_VDP info for each initial condition
sol_VDP_info = []

# List of initial conditions for VDP
initial_conditions_VDP = [[0, 0], [0.1, 0], [2, 0], [0, 2], [3, 0], [4, 4]]

# Solution with chosen initial conditions x0, y0 over T=40
for x0, y0 in initial_conditions_VDP:
    sol_VDP = solve_ivp(VDP, (0, 40), [x0, y0], t_eval = ttVDP, rtol = 1e-9, atol = 1e-12)
    sol_VDP_info.append([sol_VDP.t, sol_VDP.y[0], sol_VDP.y[1]]) # Returns time and all initial conditions for each to sol_VDP_info


# Error for Pendulum
# Empty list to hold errors
errors = []

# List of tolerances
rtols = np.logspace(-3, -12, 10)

# Chosen initial condition (np.pi/4, 0)
th0, o0 = initial_conditions_Pend[1]

# Use energy conservation to check solver error for 10 tolerances -3 to -12
for rtol in rtols:
    sol = solve_ivp(pendulum, (0, 10), [th0, o0], t_eval = ttpendulum, rtol = rtol, atol = rtol * 1e-3)

    th = sol.y[0]
    o = sol.y[1]

    E = 0.5 * L**2 * o**2 + g * L * (1 - np.cos(th)) # Energy eq
    error = np.abs(E[-1] - E[0]) # Final energy minus initial gives error
    errors.append(error)

# Plotting error
plt.figure(figsize = (9, 9))
plt.loglog(rtols, errors, 'o-')

plt.xlabel('Relative Tolerance (rtol)')
plt.ylabel('Final Energy Error')
plt.title('Pendulum Error vs Solver Tolerance')
plt.grid(True, which='both')

# Plotting conditions vs time for both systems
fig, axes = plt.subplots(4, 2, figsize=(9, 9))

# Pendulum plots
for i, (t, th, o) in enumerate(sol_Pend_info):
    ax = axes[i//2, i%2]

    ax.plot(t, th, label='Theta')
    ax.plot(t, o, label='Omega')

    ax.set_title(f'Initial Condition: {initial_conditions_Pend[i]}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid()

fig, axes = plt.subplots(3, 2, figsize=(9, 9))

# Lorenz plots
for i, (t, x, y, z) in enumerate(sol_L_info):
    ax = axes[i//2, i%2]

    ax.plot(t, x, label='X')
    ax.plot(t, y, label='Y')
    ax.plot(t, z, label='Z')

    ax.set_title(f'Initial Condition: {initial_conditions_L[i]}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid()

fig, axes = plt.subplots(3, 2, figsize=(9, 9))

# VDP plots
for i, (t, x, y) in enumerate(sol_VDP_info):
    ax = axes[i//2, i%2]

    ax.plot(t, x, label='X')
    ax.plot(t, y, label='Y')

    ax.set_title(f'Initial Condition: {initial_conditions_VDP[i]}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid()

plt.tight_layout()
plt.show()
