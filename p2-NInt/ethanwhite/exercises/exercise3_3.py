# for exercise 3.3, cos(x^2-x) thing

# 49000 subintervals for 1.5554 on leftpoint,
# 29000 subintervals for midpoint and trapezoidal rule

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as sci

def func(x):
#	f = np.cos(x**2-x) # for exercise 3.3
	f = np.exp(-x**2)*2/np.sqrt(np.pi) # for homework
	return f

def leftpoint(a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + h*i
		y = func(x)
		sum += h*y
	return sum

def rightpoint(a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + (i+1)*h
		y = func(x)
		sum += h*y
	return sum

def midpoint(a,b,N):
	sum, h = 0, (b-a)/N
	for i in range(0,N-1):
		x = a + h*i + h/2
		y = func(x)
		sum += h*y
	return sum

def trapezoid(a,b,N):
	sum = (leftpoint(a,b,N) + rightpoint(a,b,N))/2
	return sum

def simpson(a,b,N):
	sum = trapezoid(a,b,N)/3 + 2*midpoint(a,b,N)/3
	return sum

def init(a,b,N):
	L = leftpoint(a,b,N)
	R = rightpoint(a,b,N)
	M = midpoint(a,b,N)
	T = trapezoid(a,b,N)
	S = simpson(a,b,N)
	return L,R,M,T,S

def plotting(a,b,N):
	x = np.linspace(a, b, 100)
	y = midpoint(a,x,10000)
	plt.plot(x, y, label='erf(x)')
	plt.xlabel('x')
	plt.ylabel('erf(x)')
	plt.title('Plot of erf(x)')
	plt.legend()
	plt.grid()
	plt.show(block=False)
	return

a,b,N = 0, float(input("B = ")), int(input("N = ")) # for homework
#a,b,N = -1, 1, int(input("N = ")) # exercise 3.3

L,R,M,T,S = init(a,b,N)
print("trapezoid:",T,"\nmidpoint:",M,"\nleftpoint:",L,"\nrightpoint:",R,"\nsimpson:",S)
plotting(a,b,N)
