"""
Lagrange’s Interpolation
"""
x = [0, 2, 4, 6]
y = [1, -1, 3, 4]

data_points = len(x)


def mul_diff(i, val):
    mul = 1
    for idx in range(data_points):
        if i == idx:
            mul = mul
        else:
            mul = mul * (val-x[idx])
    return mul


f = []

for i in range(data_points):
    f.append(y[i] / mul_diff(i, x[i]))


print(f)


def eval_f(x):
    ans = 0
    for i in range(len(f)):
        ans = ans + f[i]*mul_diff(i, x)

    print(ans)


eval_f(4.5)
