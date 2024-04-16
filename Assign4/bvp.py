import numpy as np
import matplotlib.pyplot as plt


n = 10
h = (1-0) / n
x = np.linspace(0, 1, n+1)

# Get A
A = np.zeros((n+1, n+1))
A[0, 0] = 1
A[n, n] = 1
for i in range(1, n):
    A[i, i-1] = 1-np.exp(x[i])*h/2
    A[i, i] = -(2+x[i]*h*h)
    A[i, i+1] = 1 + np.exp(x[i])*h/2

print(A)

# Get b
b = np.zeros(n+1)
b[0] = -1
b[1:-1] = ((-x[i]**2 + 2*x[i] -3)*np.exp(-x[i]) - x[i] + 2)*h*h
b[-1] = 0

print(b)

# solve the linear equations
y = np.linalg.solve(A, b)

y_exac = (x - 1)* np.exp(-x)

plt.plot(x, y)
plt.plot(x,y_exac)
plt.legend(["Numerical", "Exact"])
plt.show()