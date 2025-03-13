# Project 2: Numeric Integration with Gauss-Legendre Quadrature

## Background
Gauss-Legendre Quadrature is a numeric integration method which approximates the definite 
integral of a function $`f(x)`$ as a sum from 1 to N of $`c_{N,i}*f(x_i)`$ where the $`x_i`$ are the roots of the Nth 
Legendre polynomial, and $`c_{N,i}`$ are the weights associated with each polynomial. The domain
of integration must be mapped to [-1, 1] for this method to work. A simple u-substitution
can be used to map an interval [a, b] to [-1, 1]. The Legendre polynomials are a complete set of orthogonal polynomials, so any function can be constructed from a sum
of these polynomials. The figure below shows plots of $P_i, P_j,$ and $P_i*P_j$ for the first 4 Legendre polynomials.

![](https://github.com/asgrice/PHYS4130-S25/blob/main/p2-NInt/asgrice/writeup/Legendre_polynomials.png)

In red are the $P_i*P_j$, and it is reasonably clear from these plots that $`\int_{-1}^{1} P_i*P_j dx = 1`$ where $`i = j`$.
## The Program
The code for this project is very brief. A function is defined, in this case given as 
$`f(x) = sin^2(\sqrt{100x})`$ with a domain of integration [0, 2]. A u-substitution is also
provided as 

```math
u=\frac{2x-a-b}{b-a}
```

which with a bit of rearranging gives 

```math
x=\frac{1}{2}(u(b - a) + a + b)
```

and 

```math
\frac{du}{dx} = \frac{2}{b - a}
```

The function definition is shown below:

```
def func(u,a,b):
    k = 0.5*(u*(b-a) + a + b)
    val = (np.sin(np.sqrt(100*k)))**2
    return val
```
The integrating function assigns the roots and weights of legendre polynomials 0 to N + 1 to two numpy arrays. Then the numpy.sum function is used to sum from 1 to N over func(roots, a, b). The final sum is multiplied by $`dx = \frac{2}{b-a}du`$. Shown below are both the summation and the code implementation of the summation.

```math
\int_{0}^{2} sin^2(\sqrt{100x})dx = \int_{-1}^{1} sin^2(\sqrt{100(u + 1)})du \approx \sum_{i=1}^N c_{N,i} sin^2(\sqrt{100(x_{N,i} + 1)})
```

```
def gauss_quad(N, a, b):
    I = 0
    dx = ((b - a)/2)
    roots, weights = scipy.special.roots_legendre(N+1)
    I = dx*np.sum(weights*func(roots, a, b))


    return I
```

## Attribution
I had some difficulty with implementing the u-substitution, but figured it out with Dr. Reid's help. The first version of the summation used a loop instead of numpy's sum function and there was some error in there that I could not figure out. I settled on using the sum function after reading [this stackoverflow thread.](https://stackoverflow.com/questions/27115917/gauss-legendre-quadrature-in-python)

## Timekeeping
Roughly 10 hours have been spent on this project.

## Languages, Libraries, Lessons Learned
This project was written in python using numpy, matplotlib, and scipy. I found them all to be useful and have learned that it's usually better to use the pre-existing functions in whatever libraries are at one's disposal.
