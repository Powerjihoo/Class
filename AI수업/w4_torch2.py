import torch


w=torch.randn(5,3,dtype=torch.float)
x=torch.tensor([[1.0,2.0],[3.0,4.0],[5.0,6.0]])
wx=torch.mm(w,x)
print('wx size:',wx.size())
print('wx:',wx)


b=torch.randn(5,2,dtype=torch.float)
result=wx+b
print('result size:',result.size())
print('result :',result)