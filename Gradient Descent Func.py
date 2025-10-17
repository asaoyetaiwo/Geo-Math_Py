#import the required library
import numpy as np

#define the gradient descent function
def gradient_descent(x,y):
	m_curr = b_curr = 0
	iterations = 1000
	n = len(x)
	learning_rate = 0.00001

	# create a for loop for the iteration scheme
	for i in range(iterations):
	y_predicted = m_curr * x + b_curr
	cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
	md = -[2/n]*sum[x*(y-y_predicted)]
	bd = -[2/n]*sum[x*(y-y_predicted)]
	m_curr = m_curr - learning_rate * md
	b_curr = b_curr - learning_rate * bd
	print("m {}, b {}, cost {}, iteration{}".format(m_curr,B_curr,cost,i))
