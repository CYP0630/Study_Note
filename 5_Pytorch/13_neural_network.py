# MNIST
# Dataloader, Transformation
# Multilayer NN, activation function
# Loss and Optimizer
# Evaluation
# GPU

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt 

# device config
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# hyper-parameter
input_size = 784
hidden_size = 100
num_classes = 10
num_epochs = 2
batch_size = 128
learning_rate = 0.001

# MNIST
training_dataset = torchvision.datasets.MNIST(root='/home/cyp/Documents/Dataset', train=True, transform=transforms.ToTensor(), download=True)
test_dataset = torchvision.datasets.MNIST(root='/home/cyp/Documents/Dataset', train=False, transform=transforms.ToTensor())

train_loader = torch.utils.data.DataLoader(dataset=training_dataset, batch_size=batch_size, shuffle=True)
test_loader = torch.utils.data.DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)

examples = iter(train_loader)
samples, labels = examples.next()
print(samples.shape, labels.shape)

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(samples[i][0], cmap='gray')
#plt.show()

class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super(NeuralNet, self).__init__()
        self.layer1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_size, num_classes)
    
    def forward(self, x):
        out = self.layer1(x)
        out = self.relu(out)
        out = self.layer2(out)
        
        return out

model = NeuralNet(input_size, hidden_size, num_classes)
model.cuda(device)

# loss and optimizer
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

# taining loop
n_total_step = len(train_loader)
for epoch in range(num_epochs):
    for i, (images, labels) in enumerate(train_loader):
        # 100, 1, 28, 28
        # 100, 784
        images = images.to(device) 
        labels = labels.to(device)  
        images = images.reshape(-1, 28 * 28)

        # forward
        output = model(images)
        loss = criterion(output, labels)

        # backwrads
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (i+1) % 100 == 0:
            print(f'epoch {epoch+1} / {num_epochs}, step {i+1} / {n_total_step}, loss = {loss.item():.4f}')

# test
with torch.no_grad():
    n_correct = 0
    n_samples = 0
    for images, labels in test_loader:
        images = images.to(device) 
        labels = labels.to(device)  
        images = images.reshape(-1, 28 * 28)

        output = model(images)

        # value, index
        _, predictions = torch.max(output, 1)
        n_samples += labels.shape[0]
        n_correct += (predictions == labels).sum().item()
    
    acc = 100.0 * n_correct / n_samples
    print(f'accuracy = {acc} ')



    

