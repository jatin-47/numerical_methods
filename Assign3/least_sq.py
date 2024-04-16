import matplotlib.pyplot as plt
import sympy as sp

x = [ 1, 1.5, 2, 2.5, 3, 3.5, 4]
y = [25, 31, 27, 28, 36, 35, 32]

x_sq = [i*i for i in x]
x_mul_y = [ i*j for i,j in zip(x,y)]

n = 7


# y = m * x + c
m, c = sp.symbols('m, c')

# ∑y = cn + m∑x
eq1 = sp.Eq(sum(y), c*n + m*sum(x))

# ∑xy = c∑x + m∑x*x
eq2 = sp.Eq(sum(x_mul_y), c*sum(x) + m*sum(x_sq))

ans = sp.solve([eq1, eq2], [m,c], dict=True)

def line(m, c, x):
    return m*x+c

plt.plot(x, y, 'ro')
plt.plot(x, [line(ans[0][m], ans[0][c], i) for i in x])
plt.title(f'm = {ans[0][m]}, c = {ans[0][c]}')
plt.show()

