import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


n = 50
a = 0
b = np.pi

m = 10

dx = (b-a) / n
dt = (0.1)/m

alpha = 3
lamb = alpha*dt
x = np.linspace(a, b, n+1)
t = np.linspace(0, dt*m, m+1)

# u(x, t)
u = np.zeros((n+1, m+1))

for i in range(n+1):
    u[i ,0] = np.sin(a+i*dx)

for t in range(m):
    for i in range(n):
        if (a+i*dx) == a:
            u[i, t+1] = 0
        elif (a+i*dx) == b:
            u[i, t+1] = 0
        else:
            u[i, t+1] = u[i, t] +  alpha*dt*(u[i+1, t] - 2*u[i, t] + u[i-1, t]) / dx**2 

for t in [3]:
    plt.plot(x, u[:, t])
    plt.legend([3])
    

# Crank-Nicolson Method
dx = 0.52
dt = 0.01
alpha = 3
lamb = alpha*dt/dx**2

a = 0
b = np.pi
n = 6
m = 10

x = np.linspace(a, b, n+1)
t = np.linspace(0, dt*m, m+1)

# u(x, t)
u = np.zeros((n+1, m+1))

for i in range(n+1):
    u[i ,0] = np.sin((a+i*dx))

for t in range(m):
    A = sp.banded(n-1, {0: 2*(1+lamb), 1: -lamb, -1:-lamb})

    cols = []
    for i in range(1, n):
        cols.append(lamb*u[i-1, t] + 2*(1-lamb)*u[i,t]+lamb*u[i+1,t])

    bb = sp.Matrix(cols)
    xx = A.LUsolve(bb)
    u[0, t+1] = 0
    u[n, t+1] = 0
    for i in range(xx.shape[0]):
        u[i+1, t+1] = xx[i]


for t in [3]:
    plt.plot(x, u[:, t])
    plt.legend([3])

plt.show()
