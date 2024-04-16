import numpy as np
import matplotlib.pyplot as plt

# Follow this code

x_data = [ 1, 1.5, 2, 2.5, 3, 3.5, 4]
y_data = [25, 31, 27, 28, 36, 35, 32]

n = len(x_data)
deg = 6

X = np.zeros((n, deg+1))

for j in range(deg+1):
    for i in range(n):
        X[i][j] = x_data[i]**j

y = np.array(y_data)

coeff = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(X),X)),np.transpose(X)),y)

def poly(x):
    ans = 0
    for i in range(deg+1):
        ans = ans + coeff[i]*x**i
    return ans

x_axis = np.linspace(x_data[0], x_data[-1], 100)
plt.plot(x_data, y_data, 'ro')
plt.plot(x_axis, [poly(x) for x in x_axis] )
plt.show()
