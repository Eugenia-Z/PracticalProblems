import numpy as np

def findA(X, B, C):
    B = np.array(B)
    C = np.array(C)
    
    # Step 1: Compute D = B * C (Matrix Multiplication)
    D = np.dot(B, C)
    
    # Step 2: Set up the equation: X = A[0] * D[0] + A[1] * D[1]
    # Using the relationship A[1] = 1 - A[0], we substitute:
    # X = A[0] * D[0] + (1 - A[0]) * D[1]
    # Rearranging: X = A[0] * (D[0] - D[1]) + D[1]
    
    # Step 3:
    D0, D1 = D[0], D[1]
    A0 = (X - D1) / (D0 - D1)
    
    # Step 4: Compute A[1] using the relationship
    A1 = 1 - A0
    return [round(float(A0), 2), round(float(A1),2)]
if __name__ == "__main__":  
    X = 0.35
    B = [[3, -1],[-2, 3]]
    C = [0.2, 0.8]
    print(findA(X, B, C))