def activation(x):
    return 1/(1+torch.exp(-x))

import torch
torch.manual_seed(7)
weights=torch.randn(1,5)
features=torch.randn_like(weights)
bias=torch.randn(1,1)
ans=activation(torch.sum(weights*features)+bias)
print(ans)
