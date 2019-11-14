import numpy as np
from sympy import *
from sympy.tensor.array import derive_by_array
import ipdb

def grad(f, *args):
    gradient = Matrix(derive_by_array(f, args))
    return gradient

def hessian(f,*args):
    n = len(args)
    gradient = Matrix(derive_by_array(f,args))
    hessian = Matrix(derive_by_array(gradient, args)).reshape(n,n)
    return hessian

def alpha_value(matrix_1, matrix_2):
    ipdb.set_trace()
    matrix_1_t = matrix_1.T
    para = np.dot(matrix_1_t, matrix_1) / (matrix_1_t.dot(matrix_2).dot(matrix_1))
    return para

x1, x2, x3 = symbols('x1 x2 x3')

funx = (x1+5)**2 + (x2+8)**2 + (x3+7)**2 + 2 * x1**2 * x2**2 + 4 * x1**2 * x3**2
funx_value = lambdify((x1, x2, x3), funx)

g_x = grad(funx, x1, x2, x3)
g_x_value = lambdify((x1, x2, x3),g_x)
#g_x_value(1, 1, 1)

h_matrix = hessian(funx, x1, x2, x3)
h_matrix_value = lambdify((x1, x2, x3), h_matrix)
#h_matrix_value(1, 1, 1)

start = np.array([0, 0, 0], dtype=float)
epsilon = 1e-7
max_iteration = 10

for i in range(max_iteration):
    if i = 0:
    gradient = g_x_value(start[0], start[1], start[2])
    hessian_m = h_matrix_value(start[0], start[1], start[2])
    learning_rate = alpha_value(gradient, hessian_m)
    x_old = funx_value(start[0], start[1], start[2])
    descend = start - learning_rate * gradient
    x_new = funx_value(descend[0][0], descend[1][1], descend[2][2])
    threshold = x_new - x_old
    print(threshold)



#dx1 = diff(funx, x1)
#dx2 = diff(funx, x2)
#dx3 = diff(funx, x3)
#print(dx1.evalf(subs = {x1:1}))
#print(dx2.evalf(subs = {x2:1}))
#print(dx3.evalf(subs = {x3:1}))



