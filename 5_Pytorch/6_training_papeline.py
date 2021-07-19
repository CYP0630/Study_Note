# 1) Design Model (input, output size, forward pass)
# 2) Construct loss and optimizer
# 3) Training loop
#    - forward pass: compute prediction
#    - backward pass: gradients 
#    - update weights

import torch 
import torch.nn as nn

# Linear Regression
# f = wx + b 
# f = 2x

# Dataset
X = torch.tensor([[1], [2], [3] ,[4]], dtype=torch.float32)
Y = torch.tensor([[2], [4], [6] ,[8]], dtype=torch.float32)
X_test = torch.tensor([5], dtype=torch.float32)

# Input_dim, Output_dim
n_samples, n_features = X.shape

input_size = n_features
output_size = n_features

# Define Model 
#model = nn.Linear(input_size, output_size)
class LinearRegression(nn.Module):

    def __init__(self, input_dim, output_dim):
        super(LinearRegression, self).__init__()
        self.lin = nn.Linear(input_dim, output_dim)
    
    def forward(self, x):
        return self.lin(x)

model = LinearRegression(input_size, output_size)
    
print(f'Prediction before training: f(5) = {model(X_test).item():.3f}')

# Training Parameter 
learning_rate = 0.01
n_iters = 100
loss = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

for epoch in range(n_iters):
    y_pred = model(X) 

    l = loss(Y, y_pred)

    l.backward() # dl/dw

    # update w
    optimizer.step()

    optimizer.zero_grad()

    if epoch % 1 == 0:
        [w, b] = model.parameters()
        print(f'epoch {epoch+1}: w = {w[0][0].item():.3f}, loss = {l:.8f}')

print(f'Prediction after training: f(5) = {model(X_test).item():.3f}')



