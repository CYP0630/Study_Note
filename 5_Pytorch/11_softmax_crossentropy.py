import torch 
import torch.nn as nn
import numpy as np

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)

def cross_entropy(actual, predicted):
    loss = -np.sum(actual * np.log(predicted))
    return loss

x = np.array([2.0, 1.0, 0.1])
output = softmax(x)
print(f'softmax_numpy: {output}')

x = torch.tensor([2.0, 1.0, 0.1])
output_torch = torch.softmax(x, axis=0)
print(f'softmax_torch: {output_torch}')

Y = np.array([1, 0, 0])
Y_pred_good = np.array([0.7, 0.2, 0.1])
Y_pred_bad = np.array([0.1, 0.3, 0.6])

l1 = cross_entropy(Y, Y_pred_good)
l2 = cross_entropy(Y, Y_pred_bad)
print(f'L1: {l1}')
print(f'L2: {l2}')

loss = nn.CrossEntropyLoss()
# nn.CrossEntropyLoss() = nn.logSoftMax + nn.negative log likelihood loss
# No softmax in last layer.
# Y: class labels
# Y_pred 

# 3 samples
Y = torch.tensor([2, 0, 1])

Y_pred_good = torch.tensor([[0.1, 1.0, 2.1], [2.0, 1.0, 0.1], [0.1, 3.0, 0.1]])
Y_pred_bad = torch.tensor([2.1, 1.0, 0.1], [0.1, 1.0, 2.1], [0.1, 3.0, 0.1]])

l1 = loss(Y_pred_good, Y)
l2 = loss(Y_pred_bad, Y)
print(f'L1: {l1.item()}')
print(f'L2: {l2.item()}')

_, predictions1 = torch.max(Y_pred_good, 1)
_, predictions2 = torch.max(Y_pred_bad, 1)
print(predictions1)
print(predictions2)






