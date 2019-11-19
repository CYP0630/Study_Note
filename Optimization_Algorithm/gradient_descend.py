import math
import numpy as np

def funx_2d(x):
    return - math.exp((x[0] ** 2 + x[1] ** 2))

def grad_2d(x):
    deriv0 = 2 * x[0] * math.exp(-(x[0] ** 2 + x[1] ** 2))
    deriv1 = 2 * x[1] * math.exp(-(x[0] ** 2 + x[1] ** 2))
    return np.array([deriv0, deriv1])


def gradient_descent_2d(grad, cur_x=np.array([0.1, 0.1]), learning_rate=0.01, precision=0.0001, max_iters=10000):
    print(f"{cur_x} is start")
    for i in range(max_iters):
        grad_cur = grad(cur_x)
        if np.linalg.norm(grad_cur, ord=2) < precision:
            break
    cur_x = cur_x - grad_cur * learning_rate
    print("The", i, "iteration：x is ", cur_x)
    print("local minimum x =", cur_x)
    return cur_x

gradient_descent_2d(grad_2d, cur_x=np.array([1, 1]), learning_rate=0.2, precision=0.000001, max_iters=10000)