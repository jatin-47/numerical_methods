import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
x = [0, 0.2, 0.4, 0.6, 0.8, 1]
y = [i**3 + 2 for i in x]

# number of cubic polynomials
n = len(x) - 1

# Each cubic poly has 4 params, so, n will have 4n 
A = np.zeros((4*n, 4*n))
b = np.zeros(4*n)

A[0][0] = x[0]**3
A[0][1] = x[0]**2
A[0][2] = x[0]
A[0][3] = 1
b[0] = y[0]

A[1][0] = 6*x[0]
A[1][1] = 2
b[1] = 0

A[2][4*n-4] = x[n]**3
A[2][4*n-3] = x[n]**2
A[2][4*n-2] = x[n]
A[2][4*n-1] = 1
b[2] = y[n]

A[3][4*n-4] = 6*x[n]
A[3][4*n-3] = 2
b[3] = 0

i = 4
for j in range(n-1):
    A[i][4*j] = x[j+1]**3
    A[i][4*j+1] = x[j+1]**2
    A[i][4*j+2] = x[j+1]
    A[i][4*j+3] = 1
    b[i] = y[j+1]
    i = i + 1

    A[i][4*(j+1)] = x[j+1]**3
    A[i][4*(j+1)+1] = x[j+1]**2
    A[i][4*(j+1)+2] = x[j+1]
    A[i][4*(j+1)+3] = 1
    b[i] = y[j+1]
    i = i + 1

for j in range(n-1):
    A[i][4*j] = 3*x[j+1]**2
    A[i][4*j+1] = 2*x[j+1]
    A[i][4*j+2] = 1
    A[i][4*(j+1)] = -3*x[j+1]**2
    A[i][4*(j+1)+1] = -2*x[j+1]
    A[i][4*(j+1)+2] = -1 
    b[i] = 0
    i = i + 1

for j in range(n-1):
    A[i][4*j] = 6*x[j+1]
    A[i][4*j+1] = 2
    A[i][4*(j+1)] = -6*x[j+1]
    A[i][4*(j+1)+1] = -2
    b[i] = 0
    i = i + 1

coeffs = np.linalg.solve(A,b)

def infer(val):
    for idx, i in enumerate(x):
        if i > val:
            cub = idx-1
            return coeffs[4*cub]*val**3 + coeffs[4*cub+1]*val**2 + coeffs[4*cub+2]*val + coeffs[4*cub+3]
    cub = n-1
    return coeffs[4*cub]*val**3 + coeffs[4*cub+1]*val**2 + coeffs[4*cub+2]*val + coeffs[4*cub+3]


x_test = [0.1, 0.3, 0.5]

for t in x_test:
    print("Interpolated: ", infer(t))
    print("Actual: ", t**3+2)
    print("Error: ", abs(infer(t)-(t**3+2)) )

x_axis = np.linspace(0, 1, 100)
y_axis = x_axis**3 + 2
plt.plot(x_axis, y_axis)
plt.plot(x_axis, [infer(val) for val in x_axis])
plt.show()