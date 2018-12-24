import numpy as np
import torch
import matplotlib.pyplot as plt
from torchvision import datasets, transforms

def activation(x):
    return 1/(1+torch.exp(-x))


# Define a transform to normalize the data
transform = transforms.Compose([transforms.ToTensor(),
                              transforms.Normalize((0.5,), (0.5,)),])

# Download and load the training data
trainset = datasets.MNIST('~/.pytorch/MNIST_data/', download=True, train=True, transform=transform)
trainloader = torch.utils.data.DataLoader(trainset, batch_size=64, shuffle=True)

dataiter = iter(trainloader)
images, labels = dataiter.next()

features=images.view(images.shape[0],-1)
ninput=features[1]
nhidden=256
noutput=10
w1=torch.randn(784,256)
b1=torch.randn(256)
y=activation(torch.mm(features,w1)+b1)
w2=torch.randn(256,10)
b2=torch.randn(10)
y1=activation(torch.mm(y,w2)+b2)
print(y1.shape)
