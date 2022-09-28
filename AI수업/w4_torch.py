import torch

x=torch.tensor([[1,2,3],[4,5,6],[7,8,9]])
print(x)

print('size', x.size())
print('shape', x.shape)
print('랭크', x.ndimension())