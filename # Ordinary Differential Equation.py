# This script solves the first order differential equation using finite difference method
# 09-0111
# Import the required libraries
import numpy as np
from math import exp, sqrt

# Input the required parameters for the problem

upper_b = input(float('Enter the upper class boundary:'))
lower_b = input(float('Enter the lower class bpondary:'))
h = input(float('Enter the step size:'))
N = int((upper_b - lower_b) / h)
x = np.zeros(N)
y = np.zeros(N)

# Initialize the first value by stating the initial boundary condition
y[0] = 0

# Looping process to solve the differential equation
for i in range(1, N):
    x[i] = x[i-1] + h
    y[i] = y[i - 1] + h * (exp(x[i - 1]) - y[i - 1])

print(x,y)
import matplotlib.pyplot as plt
plt.plot(x, y, color ='red')
plt.xlabel('x')
plt.title('Solution of the Differential Equation')
plt.show()

print(x,y)