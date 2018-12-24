def activation(x):
    return 1/(1+torch.exp(-x))

import torch
torch.manual_seed(7)
weights=torch.randn(1,5)
features=torch.randn_like(weights)
bias=torch.randn(1,1)
ans=activation(torch.sum(weights*features)+bias)
#or
#(features*weights).sum()

# or else this can be done in a single step with torch.mm(1,2) but we need to
# reshape before that
print(ans)
