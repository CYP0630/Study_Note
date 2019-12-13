from sklearn import datasets
from sklearn.preprocessing import StandardScaler
import random as rd
import math
import matplotlib.pyplot as plt


def generateTrain(data, label, trainNumber):
    data_train, data_test, label_train, label_test = [], [], [], []
    int_list = list(range(150))
    rd.seed(1)
    random_int_list = rd.sample(int_list, k=trainNumber)
    for i in range(150):
        if i in random_int_list:
            data_train.append(data[i])
            label_train.append(label[i])
        else:
            data_test.append(data[i])
            label_test.append(label[i])
    data_train_fit = StandardScaler().fit(data_train)
    data_train_transformed = data_train_fit.transform(data_train)
    data_test_transformed = data_train_fit.transform(data_test)
    return data_train_transformed, data_test_transformed, label_train, label_test


def accuracy(x, y):
    right = 0
    for i, j in zip(x, y):
        if i == j:
            right += 1
    return right/len(x)


class HandWriteKNN2():
    def __init__(self, k=5):
        self.k = k

    def fit(self, data, label):
        self.data = data
        self.label = label

    def predict(self, data_test):
        prediction = []
        for i in data_test:
            vote0 = vote1 = vote2 = 0
            NBs = self.findNB(i)
            for j in NBs:
                if self.label[j] == 0:
                    vote0 += 1
                elif self.label[j] == 1:
                    vote1 += 1
                elif self.label[j] == 2:
                    vote2 += 1
            if vote0>=vote1 and vote0>=vote2:
                prediction.append(0)
            elif vote1>=vote0 and vote1>=vote2:
                prediction.append(1)
            elif vote2>=vote0 and vote2>=vote1:
                prediction.append(2)
        return prediction

    def findNB(self, point):
        l = []
        for a in self.data:
            l.append(self.dist(a, point))
        lc = l.copy()
        miniIndex = []
        for i in range(self.k):
            miniIndex.append(l.index(min(lc)))
            lc.pop(lc.index(min(lc)))
        return miniIndex

    def dist(self, a, b):
        sum = 0
        for i, j in zip(a,b):
            sum += (i-j)**2
        return math.sqrt(sum)


data, label = datasets.load_iris(return_X_y=True)
data_train, data_test, label_train, label_test = generateTrain(data, label, 100)
handWrite = HandWriteKNN2(k=10)
handWrite.fit(data_train, label_train)
prediction = handWrite.predict(data_test)
print('Prediction is:\t', prediction)
print('Label_test is:\t', label_test)

print('Accuracy of handwriting kNN prediction\n', accuracy(prediction, label_test))
knnPack = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 2 1 1 1 1 1 1 1 1 1 2 2 2 1 2 2 2 2 1 2 2 2 2 1 2 1 2 2 2'
knnPackPrediction = [int(x) for x in knnPack.split(' ')]
print('Comparing to skLearn kNN\n', accuracy(prediction, knnPackPrediction))

acc = []
for k in range(1,20):
    handWrite = HandWriteKNN2(k)
    handWrite.fit(data_train, label_train)
    prediction = handWrite.predict(data_test)
    acc.append(accuracy(prediction, label_test))

plt.plot(range(1, 20), acc)
plt.show()