import numpy as np

def f(x1, x2, j):
    return ((x1-6)**2+(x2-7)**2)+j*(max(0, (-3*x1-2*x2+6))**2+max(0, (-x1+x2-3))**2+max(0, (x1+x2-7))**2+max(0, ((2/3)*x1-x2-(4/3)))**2)

def pana(threshold, j0, growth):#input threshold, starting penalty parameter jo and the parameter growth.
    a = []
    fprime = 99999
    x0 = [99999, 99999]
    for i in range(100):#generate the list of panalty parameter
        a.append(pow(growth, i) * j0)
    X1 = X2 = np.linspace(15, 0, 1000)
    for i in a:
        fprime = 99999
        for j in X1:
            for k in X2:
                if f(j, k, i) <= fprime:
                    fprime = f(j, k, i)
                    xprime = [j, k]
        if np.sqrt((xprime[0] - x0[0]) ** 2 + (xprime[1] - x0[1]) ** 2) <= threshold:
            break
        else:
            x0 = xprime
            print('i = ', i, 'x0 = ', x0)
    print(x0, fprime)
    return

pana(0.0001, 1, 1.5)