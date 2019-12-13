from sklearn import datasets
import random as rd
import numpy as np
from sklearn.preprocessing import StandardScaler
import time

def generateTrain(data, label, trainNumber):
    data_train = []
    data_test = []
    label_train = []
    label_test = []
    int_list = []
    rd.seed(1)
    for i in range(150):
        int_list.append(i)
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

class handWriteKNN():

    def __init__(self, k=5):
        self.k = k
        self.data_train0 = []
        self.data_train1 = []
        self.data_train2 = []

    def fit(self, X, y):
        self.data_train = X
        self.label_train = y
        for i in range(len(y)):
            if y[i] == 0:
                self.data_train0.append(self.data_train[i])
            if y[i] == 1:
                self.data_train1.append(self.data_train[i])
            if y[i] == 2:
                self.data_train2.append(self.data_train[i])

    def predict(self, data_test):
        prediction = []
        for i in data_test:
            kthNB0, kthNB1, kthNB2 = self.findKthNB(i)
            density0 = self.k / len(self.data_train0) / (
                        (i[0] - kthNB0[0]) ** 2 + (i[1] - kthNB0[1]) ** 2 + (i[2] - kthNB0[2]) ** 2 + (
                            i[3] - kthNB0[3]) ** 2)**4
            density1 = self.k / len(self.data_train1) / (
                        (i[0] - kthNB1[0]) ** 2 + (i[1] - kthNB1[1]) ** 2 + (i[2] - kthNB1[2]) ** 2 + (
                            i[3] - kthNB1[3]) ** 2)**4
            density2 = self.k / len(self.data_train2) / (
                        (i[0] - kthNB2[0]) ** 2 + (i[1] - kthNB2[1]) ** 2 + (i[2] - kthNB2[2]) ** 2 + (
                            i[3] - kthNB2[3]) ** 2)**4
            if density1<density0 and density2<density0:
                prediction.append(0)
            if density0<density1 and density2<density1:
                prediction.append(1)
            if density0<density2 and density1<density2:
                prediction.append(2)
        return prediction

    def findKthNB(self, x):
        distance0 = []
        distance1 = []
        distance2 = []
        for i in self.data_train0:
            distance0.append((i[0]-x[0])**2+(i[1]-x[1])**2+(i[2]-x[2])**2+(i[3]-x[3])**2)
        for i in self.data_train1:
            distance1.append((i[0]-x[0])**2+(i[1]-x[1])**2+(i[2]-x[2])**2+(i[3]-x[3])**2)
        for i in self.data_train2:
            distance2.append((i[0]-x[0])**2+(i[1]-x[1])**2+(i[2]-x[2])**2+(i[3]-x[3])**2)

        distance0Copy = distance0.copy()
        distance1Copy = distance1.copy()
        distance2Copy = distance2.copy()

        for i in range(self.k):
            nb0 = min(distance0Copy)
            nbIndex0 = distance0Copy.index(nb0)
            distance0Copy.pop(nbIndex0)
            nb1 = min(distance1Copy)
            nbIndex1 = distance1Copy.index(nb1)
            distance1Copy.pop(nbIndex1)
            nb2 = min(distance2Copy)
            nbIndex2 = distance2Copy.index(nb2)
            distance2Copy.pop(nbIndex2)
            if i == self.k-1:
                nbIndex0 = distance0.index(nb0)
                nbIndex1 = distance1.index(nb1)
                nbIndex2 = distance2.index(nb2)
                return self.data_train0[nbIndex0], self.data_train1[nbIndex1], self.data_train2[nbIndex2]


data, label = datasets.load_iris(return_X_y=True)
data_train, data_test, label_train, label_test = generateTrain(data, label, 100)
handWrite = handWriteKNN(k=10)
time0 = time.time()
handWrite.fit(data_train, label_train)
prediction = handWrite.predict(data_test)
time1 = time.time()
print(prediction)
print(label_test)
print(accuracy(prediction, label_test))
print(time1-time0)

print('0.0019948482513427734')