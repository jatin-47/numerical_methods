import numpy as np
import matplotlib.pyplot as plt


n = 5000
a = -1
b = 1
dx = (b-a) / n
dt = 0.8*dx
m = int(0.3/dt) 
print(m)

x = np.linspace(-1, 1, n+1)
t = np.linspace(0, 0.3, m+1)


# u(x, t)
u = np.zeros((n+1, m+1))

for i in range(n+1):
    if abs(a+i*dx) < 1/3:
        u[i, 0] = 1
    elif 1/3 < abs(a+i*dx) and abs(a+i*dx) <= 1: 
        u[i, 0] = -1
print(u[:,0])

for t in range(m):
    for i in range(n+1):
        l = i-1
        r = i+1
        if l == -1:
            l = n-1
        if r == n+1:
            r = 1
        u[i, t+1] = (u[r, t] + u[l, t])/2  - dt*(u[r, t]**2 - u[l, t]**2)/(4*dx) 


for t in [0, 10, 20, 35, 37]:
    plt.plot(x, u[:, m])
plt.show()
