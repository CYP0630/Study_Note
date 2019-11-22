from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.preprocessing import StandardScaler

data, label = datasets.load_iris(return_X_y=True)
data_train, data_test, label_train, label_test = train_test_split(data, label, test_size=0.4, random_state=0)

for i in range(len(data)):
    print("(", i, ":", data[i], ",", label[i], ")")

data_train_fit = StandardScaler().fit(data_train)
data_train_transformed = data_train_fit.transform(data_train)
clf = LogisticRegressionCV(n_jobs=2, penalty='l1', solver='liblinear', cv=10, scoring = 'accuracy', random_state=0)

clf.fit(data_train_transformed, label_train)

print(clf.score(data_train_fit.transform(data_test), label_test))
print(clf.intercept_ )
print(clf.coef_)
print(clf.C_)