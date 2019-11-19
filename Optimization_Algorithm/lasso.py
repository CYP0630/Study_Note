import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets
from sklearn import preprocessing

data, target = datasets.load_iris(return_X_y=True)
x = data[:]
y = target[:]

x = x.astype(np.float64)
y = y.astype(np.float64)

x = preprocessing.scale(x)
y = preprocessing.scale(y)

n_alphas = 50
alphas = np.logspace(-10, 4, n_alphas)
lasso = linear_model.Lasso(fit_intercept=True)

coefs_lasso = []
for a in alphas:
    lasso.set_params(alpha=a)
    lasso.fit(x, y)
    coefs_lasso.append(lasso.coef_)

figure = plt.figure('visualize', figsize=(10, 4))
ax_lasso = figure.add_axes([0.1, 0.1, 0.4, 0.8], xlabel='X', ylabel='Y')
ax_lasso.plot(alphas, coefs_lasso)
ax_lasso.set_xscale('log')
ax_lasso.set_xlim(ax_lasso.get_xlim()[::-1])
ax_lasso.grid(True)

ridge =linear_model.Ridge(fit_intercept=True)
coefs_ridge = []
for a in alphas:
    ridge.set_params(alpha = a)
    ridge.fit(x,y)
    coefs_ridge.append(ridge.coef_)
ax_ridge=figure.add_axes([0.6,0.1,0.4,0.8],xlabel='X',ylabel='Y')
ax_ridge.plot(alphas,coefs_ridge)
ax_ridge.set_xscale('log')
ax_ridge.set_xlim(ax_ridge.get_xlim()[::-1])

plt.grid(True)
plt.show()