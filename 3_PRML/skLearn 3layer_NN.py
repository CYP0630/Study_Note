import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
X, y = datasets.load_iris(return_X_y=True)


# dataset = pd.read_csv('Iris.csv')
#
# import seaborn as sns
# sns.pairplot(dataset.iloc[:, 1:6], hue='Species')
#
# X = dataset.iloc[:, 1:5].values
# y = dataset.iloc[:,5].values

from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
y1 = encoder.fit_transform(y)

Y = pd.get_dummies(y1).values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)

from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

model = Sequential()
model.add(Dense(10, input_shape=(4,), activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(6, activation='relu'))
model.add(Dense(3, activation='softmax'))

model.compile(Adam(lr=0.04), 'categorical_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(X_train, y_train, epochs=100)

y_pred = model.predict(X_test)

y_pred_class = np.argmax(y_pred, axis=1)
y_test_class = np.argmax(y_test, axis=1)

from sklearn.metrics import classification_report
report = classification_report(y_test_class, y_pred_class)
print(report)