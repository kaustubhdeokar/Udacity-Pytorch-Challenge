import torch

def activation(x):
    return 1/(1+torch.exp(-x))

features=torch.randn(1,3)
ninput=features.shape[1]
nhidden=2
noutput=1

w1=torch.randn(ninput,nhidden)
w2=torch.randn(nhidden,noutput)

b1=torch.randn(1,nhidden)
b2=torch.randn(1,noutput)

mid=activation(torch.mm(features,w1)+b1)

final=activation(torch.mm(mid,w2)+b2)

print(final)
