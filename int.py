def rectangle_method(a, b, n):
    dx = (b - a) / n
    x = a + dx / 2
    integral = 0
    ints, xs = [], []
    for i in range(n):
        f_x = f(x)  # replace function with your own function
        integral += f_x * dx
        x += dx
        ints.append(integral)
        xs.append(x)
    return [integral, ints, xs]

def f(x):
    return -2*x**2 + 3

a = -1  # lower limit
b = 2  # upper limit
n = 30  # number of subintervals

integral = rectangle_method(a, b, n)
print("Approximate integral:", integral[0])
