import numpy as np


def f(x1, x2):
    return x1 * x1 + 2 * x2 * x2 + 4 * x1 + 4 * x2

def sd(start, threshold):
    x0 = start
    alphad = [1, 2]

    for i in range(1000):
        grad0 = grad(x0)
        hess0 = hess(x0)
        alpha = (grad0[0]*grad0[0]+grad0[1]*grad0[1])/(grad0[0]*grad0[0]*hess0[0][0] + grad0[0]*grad0[1]*(hess0[1][0]+hess0[0][1]) + grad0[1]*grad0[1]*hess0[1][1])
        for k, l in enumerate(grad0):
            alphad[k] = (alpha*l)
        alphadvalue = np.sqrt(alphad[0]**2+alphad[1]**2)
        if alphadvalue <= threshold:
            break
        x0new = []
        x0new.append(x0[0] - alphad[0])
        x0new.append(x0[1] - alphad[1])
        x0 = x0new
        print('sd ', x0[0], x0[1], 'i = ', i)
    print('x0 = ', x0)
    return

def grad(x0):
    x1 = x0[0]
    x2 = x0[1]

    x1_1 = x1 + 0.001
    x1_2 = x1 - 0.001
    x2_1 = x2 + 0.001
    x2_2 = x2 - 0.001
    x1 * x1 + 2 * x2 * x2 + 4 * x1 + 4 * x2
    fx1_1 = x1_1 * x1_1 + 2 * x2 * x2 + 4 * x1_1 + 4 * x2
    fx1_2 = x1_2 * x1_2 + 2 * x2 * x2 + 4 * x1_2 + 4 * x2
    fx2_1 = x1 * x1 + 2 * x2_1 * x2_1 + 4 * x1 + 4 * x2_1
    fx2_2 = x1 * x1 + 2 * x2_2 * x2_2 + 4 * x1 + 4 * x2_2
    return [(fx1_1-fx1_2)/0.002, (fx2_1-fx2_2)/0.002]

def hess(x0):
    x1_1 = [x0[0]+0.001, x0[1]]
    x1_2 = [x0[0]-0.001, x0[1]]
    x2_1 = [x0[0], x0[1]+0.001]
    x2_2 = [x0[0], x0[1]-0.001]
    b_1 = grad(x1_1)
    b_2 = grad(x1_2)
    c_1 = grad(x2_1)
    c_2 = grad(x2_2)
    return [[(b_1[0]-b_2[0])/0.002, (c_1[0]-c_2[0])/0.002], [(b_1[1]-b_2[1])/0.002, (c_1[1]-c_2[1])/0.002]]

sd([0, 0], 0.0001)
