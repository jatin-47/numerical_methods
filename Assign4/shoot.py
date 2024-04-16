import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

F = lambda x, s: np.dot(np.array([[0,1],[-3/x**2, (2 * x**2 * np.exp(x)/s[1] + 3/x)]]),s)

y0 = 0
v0 = 5.5
x_eval = np.linspace(1, 2, 10)
sol = solve_ivp(F, [1, 2], [y0, v0], t_eval = x_eval)


plt.plot(sol.t, sol.y[0])
plt.plot(x_eval, 2*x_eval*np.exp(x_eval)*(x_eval-1))
plt.legend(["Numerical", "Exact"])
plt.plot(2, 4*np.exp(1)**2, 'ro')

plt.show()