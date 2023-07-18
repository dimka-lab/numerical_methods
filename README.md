<!-- #region -->
# Numerical methods
Implementation of methods for solving mathematical problems in numerical form

Library for python
## Installation
```bash
pip install numerical-methods
```
- [Github of project](https://github.com/dimka-lab/numerical_methods) 

- [Documentation]()

- [PyPI](https://pypi.org/project/numerical-methods/)

The whole notebook with examples avialable in [notebook](https://github.com/dimka-lab/numerical_methods/blob/main/examples_numerical_methods.ipynb) in this repo
## Content
-  [Integrals](#integrals)
    -  [Rectangle method](#rectangle-method)
-  [Numerical solution of nonlinear equations](#numerical-solution-of-nonlinear-equations)
    -  [Bisection method](#bisection-method)

### Integrals
Let's try calculate integral $\displaystyle \int_{-1}^{4}  (2x^2-3)  \mathrm{d}x = \frac {85} 3$

At first, we will find analytical (exact) solution:
$\int (2x^2−3)dx = 2\int x^2 \mathrm{d}x − 3\int 1 \mathrm{d}x = \frac {2x^3}{3} - 3x + C$
 $\displaystyle \int_{-1}^{4}  (2x^2-3)  \mathrm{d}x = F(4) - F(-1) = \frac {85} 3 $
```python
exact_solution = 85/3
print(f"exact solution = {exact_solution}")
>>> exact solution = 28.333333333333332
```
#### Rectangle method
Now we will calculate it numerically by rectangle method:

$\displaystyle I = \int_{a}^b f(x) \mathrm dx \approx \sum_{i=0}^{n-1}f(x_i)(x_{i+1}-x_i)$
```python
from numerical_methods import rectangle_method
def f(x):
    return 2*x**2 - 3
integral = rectangle_method(-1, 4, 100)
print('Exact solution = ', exact_solution)
print("Approximate integral:", integral[0])
print(f'Difference between exact and approximate solutions equals {abs(exact_solution - integral[0]):.15f}')
```
<pre > >>> Exact solution =  28.333333333333332
 >>> Approximate integral: 28.331249999999958
 >>> Difference between exact and approximate solutions equals 0.002083333333374
</pre>

### Numerical solution of nonlinear equations
Suppose we want to solve equation $x^3+x-1$ with precision $\varepsilon = 0.0001$ by bisection method.
#### Bisection method
Repeat following steps until $h < e$ (actual errors < desired bound for the error)
- Step 1. Calculate $m = (a+b)/2$
- Step 2. Calculate $f(m)$ and if $f(m) = 0$ then stop -> break
- Step 3. Calculate $h = |(b-a)/2|$ for error testing
- Step 4. If $f(a)f(m) < 0$ then $b = m$ and if $f(a)f(m) > 0$ then $a = m$

Finding solution using this method:
```python
from numerical_methods import bisection
def func(x):
        return x**3 + x - 1
x = bisection(func, 0, 1, 0.00001, trace=True)
print(x)
```
<pre>
m = 0.5000000, [a, b] = [0.5000000, 1.0000000], h = 0.5000000 > 0.0000100 = e
m = 0.7500000, [a, b] = [0.5000000, 0.7500000], h = 0.2500000 > 0.0000100 = e
m = 0.6250000, [a, b] = [0.6250000, 0.7500000], h = 0.1250000 > 0.0000100 = e
m = 0.6875000, [a, b] = [0.6250000, 0.6875000], h = 0.0625000 > 0.0000100 = e
m = 0.6562500, [a, b] = [0.6562500, 0.6875000], h = 0.0312500 > 0.0000100 = e
m = 0.6718750, [a, b] = [0.6718750, 0.6875000], h = 0.0156250 > 0.0000100 = e
m = 0.6796875, [a, b] = [0.6796875, 0.6875000], h = 0.0078125 > 0.0000100 = e
m = 0.6835938, [a, b] = [0.6796875, 0.6835938], h = 0.0039062 > 0.0000100 = e
m = 0.6816406, [a, b] = [0.6816406, 0.6835938], h = 0.0019531 > 0.0000100 = e
m = 0.6826172, [a, b] = [0.6816406, 0.6826172], h = 0.0009766 > 0.0000100 = e
m = 0.6821289, [a, b] = [0.6821289, 0.6826172], h = 0.0004883 > 0.0000100 = e
m = 0.6823730, [a, b] = [0.6821289, 0.6823730], h = 0.0002441 > 0.0000100 = e
m = 0.6822510, [a, b] = [0.6822510, 0.6823730], h = 0.0001221 > 0.0000100 = e
m = 0.6823120, [a, b] = [0.6823120, 0.6823730], h = 0.0000610 > 0.0000100 = e
m = 0.6823425, [a, b] = [0.6823120, 0.6823425], h = 0.0000305 > 0.0000100 = e
m = 0.6823273, [a, b] = [0.6823273, 0.6823425], h = 0.0000153 > 0.0000100 = e
x = 0.6823348999023438, [a, b] = [0.6823272705078125, 0.6823348999023438], h = 7.62939453125e-06 < 1e-05 = e

actual errors < desired bound for the error -->> solution found: x =
0.6823348999023438
</pre>
#### to be continued in close times
<!-- #endregion -->

### References
[1] Численные методы. Примеры и задачи. Учебно-методическое пособие
по курсам «Информатика» и «Вычислительная математика». / Сост.:
Ф.Г.Ахмадиев, Ф.Г.Габбасов, Л.Б.Ермолаева, И.В.Маланичев. Казань:
КГАСУ, 2017. – 107 с.

[2] Rectangle method - URL: https://encyclopedia2.thefreedictionary.com/Rectangle+method

[3] Newton's method - URL: https://en.wikipedia.org/wiki/Newton%27s_method

[4] Bisection method - URL: https://en.wikipedia.org/wiki/Bisection_method

[5] to be continued... 
