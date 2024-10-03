import numpy as np
from scipy.integrate import solve_ivp

def findValue(A, x_0, T):
    # Convert A to numpy array for easier matrix multiplication
    A = np.array(A)
    
    # Define the ODE function x'(t) = A * x(t)
    def ode_system(t, x):
        return A @ x
    
    # Solve the ODE using solve_ivp
    sol = solve_ivp(ode_system, [0, T], x_0, modethods = "RK45", t_eval=[T])
    
    # Extract the solution at time T and round to two decimal places
    x_T = sol.y[:, -1]
    return np.round(x_T, 2)

if __name__ == "__main__":
    A = [[1, 2], [3, 2]]
    x_0 = [0, -4]
    T = 1
    result = findValue(A, x_0, T)
    print(result) 