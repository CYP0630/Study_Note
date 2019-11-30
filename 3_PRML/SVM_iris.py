import numpy as np
from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

data, label = datasets.load_iris(return_X_y=True)
data_train, data_test, label_train, label_test = train_test_split(data, label, test_size=0.5, random_state=42)

data_train_fit = StandardScaler().fit(data_train)
data_train_transformed = data_train_fit.transform(data_train)
data_test_transformed = data_train_fit.transform(data_test)

clf = LinearSVC(penalty='l2', loss='squared_hinge',
                dual=True, tol=0.0001, C=100, multi_class='ovr',
                fit_intercept=True, intercept_scaling=1, class_weight=None,verbose=0
                , random_state=0, max_iter=1000)


clf.fit(data_train_transformed, label_train)
clf.predict(data_test_transformed)
clf.score(data_test_transformed, label_test) * 100