# Van der Pol(VDP) ode
# Set damping to 1
u = 1

# VDP system
def VDP(t, z):
    x, y = z
    dxdt = y
    dydt = u * (1 - x**2) - x
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
