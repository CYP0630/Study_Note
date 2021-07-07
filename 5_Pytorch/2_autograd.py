import torch 

# Create tensor
x = torch.rand(3, requires_grad=True)
print(x)

# Computation
y = x + 2 
print(y)

z = y*y*2
print(z)
z = z.mean()
print(z) 

# Backward
z.backward() # dz/dx, must be scalar
            # otherwise, z.backward(vector)
print(x.grad)

# x.requires_grad_(False)
# x.detach()
# with torch.no_grad(): 


weights = torch.ones(4, requires_grad=True)

for epoch in range(3):
    model_output = (weights*3).sum()

    model_output.backward() 

    # weights.grad.zero_()
    
    print(weights.grad)

