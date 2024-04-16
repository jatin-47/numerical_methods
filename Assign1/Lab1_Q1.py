"""
Newton's Diveided Difference Interpolation
"""

x = [1, 2, 3, 4, 5, 6]
y = [14.5, 19.5, 30.5, 53.5, 94.5, 159.5]

data_points = len(x)


def mul_diff(i, val):
    mul = 1
    for idx in range(i):
        mul = mul * (val-x[idx])
    return mul


def func(n, val):
    if n == 0:
        return y[0]
    return func(n-1, val) + f[n]*mul_diff(n, val)


f = []

f.append(y[0])

for i in range(1, data_points):
    f.append((y[i] - func(i-1, x[i])) / mul_diff(i, x[i]))


print(f)


def eval_f(x):
    ans = f[0]
    for i in range(1, len(f)):
        ans = ans + f[i]*mul_diff(i, x)

    print(ans)


eval_f(4.5)
