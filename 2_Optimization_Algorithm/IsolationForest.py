from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegressionCV
from sklearn.ensemble import IsolationForest

data, label = datasets.load_iris(return_X_y=True)
data_train, data_test, label_train, label_test = train_test_split(data, label, test_size=0.2, random_state=0)

for i in range(len(data)):
    print("(", i, ":", data[i], ",", label[i], ")")

clf = IsolationForest(behaviour='new', contamination=0.05)
clf.fit(data_train)
pred_train = clf.predict(data_train)
pred_test = clf.predict(data_test)
print(len(pred_train))

for i in range(len(pred_train)):
    print("(", i, ":", pred_train[i], ",", ")")

#data_train_fit = StandardScaler().fit(pred_train)
#data_train_transformed = data_train_fit.transform(data_train)
#log_gerssion = LogisticRegressionCV(n_jobs=2, penalty='l1', solver='liblinear', cv=10, scoring = 'accuracy', random_state=0)
#log_gerssion.fit(pred_train, label_train)
#print(log_gerssion.score(pred_train, label_test))






