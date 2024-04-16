import numpy as np
import matplotlib.pyplot as plt


n = 200
a = -1
b = 1
dx = (b-a) / n
dt = 0.8*dx
m = int(4/dt) #500

x = np.linspace(-1, 1, n+1)
t = np.linspace(0, 4, m+1)


# u(x, t)
u = np.zeros((n+1, m+1))

for i in range(n+1):
    if abs(a+i*dx) < 1/3:
        u[i, 0] = 1
    elif 1/3 < abs(a+i*dx) and abs(a+i*dx) <= 1: 
        u[i, 0] = 0

for t in range(m):
    for i in range(n+1):
        l = i-1
        r = i+1
        if l == -1:
            l = 199
        if r == 201:
            r = 1
        u[i, t+1] = (u[r, t] + u[l, t])/2  - dt*(u[r, t] - u[l, t])/(2*dx) 


for t in [0, 10, 20, 160, 320, 500]:
    plt.plot(x, u[:, t])

plt.legend(['0', '10',  '20', '160', '320', '500'])
plt.show()
