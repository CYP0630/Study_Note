import torch

x = torch.tensor(1.0)
y = torch.tensor(2.0)

w = torch.tensor(1.0, requires_grad=True)

# forward
y_hat = w * x

#loss
loss = (y_hat - y)**2 

# backword
loss.backward()
print(w.grad)

# 



