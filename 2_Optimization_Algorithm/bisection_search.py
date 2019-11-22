import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = (x) / (x**2  + 1)
    return y

def bin():
    a = -0.6
    b = 0.75
    threshold = 10e-4
    while(1):
        plt.plot([a, b], [f(a), f(b)])
        print(a, b)
        x = (a + b)/2
        if f(x) == 0:
            break
        elif (f(x) * f(a)<0):
            b = x
        elif (f(x) * f(a)>0):
            a = x
        elif (a > b):
           print("No solution")
        if abs(a - b) < threshold:
            break
    print("Solution of x is ",x)

x = np.linspace(-2,2, 500)
#plt.figure(figsize = (5, 5))
plt.plot(x, f(x))

plt.axis([-1,1,-1,1])
plt.xlabel("x")
plt.ylabel("y")
plt.title("Binary search")
plt.grid(True)
bin()

plt.show()
