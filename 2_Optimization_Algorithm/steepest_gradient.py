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
    matrix_1_t = matrix_1.T
    para = np.dot(matrix_1_t, matrix_1) / (matrix_1_t.dot(matrix_2).dot(matrix_1))
    return para

x1, x2  = symbols('x1 x2')

funx = x1**2 + 2 * x2**2 + 4 * x1 + 4 * x2
funx_value = lambdify((x1, x2), funx)

g_x = grad(funx, x1, x2)
g_x_value = lambdify((x1, x2),g_x)

h_matrix = hessian(funx, x1, x2)

epsilon = 1e-4
max_iteration = 10
start = np.array([0, 0])


for i in range(10):
    if i==0:
        gradient_value = g_x_value(start[0], start[1])
        learning_rate = (alpha_value(gradient_value, h_matrix))[0][0]
        descend_value = learning_rate * gradient_value
        new_x1 = 0 - descend_value[0]
        new_x2 = 0 - descend_value[1]
        old_funx_value = funx_value(0, 0)
        new_funx_value = funx_value(new_x1, new_x2)
        print(old_funx_value)
        print(new_funx_value)
        if abs(new_funx_value - old_funx_value) < epsilon:
            break
    if i > 0:
        gradient_value = g_x_value(new_x1[0], new_x2[0])
        learning_rate = (alpha_value(gradient_value, h_matrix))[0][0]
        descend_value = learning_rate * gradient_value
        old_funx_value = funx_value(new_x1[0], new_x2[0])
        new_x1 = new_x1[0] - descend_value[0]
        new_x2 = new_x2[0] - descend_value[1]
        new_funx_value = funx_value(new_x1, new_x2)
        print(new_x1)
        print(new_x2)
        if abs(new_funx_value - old_funx_value) < epsilon:
            break















