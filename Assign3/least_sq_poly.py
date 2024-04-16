import matplotlib.pyplot as plt
import sympy as sp
import numpy as np

x_data = [ 1, 1.5, 2, 2.5, 3, 3.5, 4]
y_data = [25, 31, 27, 28, 36, 35, 32]

n = len(x_data)
deg = 6

y = sp.Matrix(y_data)
cols = []
for p in range(deg + 1):
    cols.append([i**p for i in x_data])
x = sp.Matrix(cols)
x = x.transpose()

a = (x.transpose()*x).inv()*x.transpose()*y
print(a)

def poly(a, x):
    col = []
    for i in range(len(a)):
        col.append(x**i)
    return list(a.transpose()*sp.Matrix(col))[0]

plt.plot(x_data, y_data, 'ro')
# plt.plot(x_data, [poly(a, i) for i in x_data])
plt.plot(np.linspace(x_data[0], x_data[-1]), [poly(a, i) for i in np.linspace(x_data[0], x_data[-1])])
plt.title(f'coeffs = {a}')
plt.show()
