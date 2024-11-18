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


from scipy.linalg import expm

def findValue2(A, x_0, T):
    # Convert A to numpy array and x_0 to a column vector
    A = np.array(A)
    x_0 = np.array(x_0)
    
    # Calculate the matrix exponential of A*T
    exp_AT = expm(A * T)
    
    # Compute x(T) = exp(A*T) * x(0)
    x_T = exp_AT.dot(x_0)
    
    # Return the result rounded to two decimals
    return np.round(x_T, 2).tolist()

# Test the function with given example
A = [[1, 2], [3, 2]]
x_0 = [0, -4]
T = 1
findValue(A, x_0, T)

if __name__ == "__main__":
    A = [[1, 2], [3, 2]]
    x_0 = [0, -4]
    T = 1
    result = findValue(A, x_0, T)
    print(result) 