import torch
import numpy 
x = torch.rand(1, 2)
print(x)

y = torch.tensor([2.5, 0.1])
print(y)

#z = torch.add(x, y)  # z = x + y
# torch.sub() -
# torch.mul() *
# torch.div() /
# print(z)

# array operation
z = torch.rand(5, 3)
print(z)
print(z[1, 1])
print(z[1, 1].item())

# reshape
a = torch.rand(4, 4)
print(a)
b = a.view(16)
print(b)
c = a.view(-1, 8)
print(c.size())

# Numpy
d = a.numpy() # In CPU, a and d has same location

# Numpy to torch
e = numpy.ones(5)
f = torch.from_numpy(e)
print(f)

e += 1
print(f)

# Check device 
if torch.cuda.is_available():
    device = torch.device("cuda")
    h = torch.ones(5, device=device)
    i = torch.ones(5)
    i = i.to(device)
    j = h + i
    j = j.to("cpu")

# Grad
l = torch.ones(5, requires_grad=True)



