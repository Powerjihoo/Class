from w4_torch_function import *
import torch


##--network
class NeuralNet(torch.nn.Module):
    def __init__(self,input_size):
        super(NeuralNet,self).__init__()
        self.input_size=input_size
        self.fc1=torch.nn.Linear(self.input_size,1)
        self.act1=torch.nn.Sigmoid()

    def forward(self,input_tensor):
        fc1=self.fc1(input_tensor)
        output=self.act1(fc1)
        return output

dist1=gauss_2d(-1.0,0.0)
dist2=gauss_2d(1.0,0.0)

paper=np.ones((512,512,3),dtype=np.uint8)*255
paper=cv2.arrowedLine(paper,(0,256),(512,256),(0,0,0),tipLength=0.025)
paper=cv2.arrowedLine(paper,(256,512),(256,0),(0,0,0),tipLength=0.025)

visualization(paper,dist1,color=(255,0,0))
visualization(paper,dist2,color=(0,0,255))
cv2.imshow('dist',paper)
cv2.waitKey(-1)


##--network
model=NeuralNet(2)
learning_rate=0.01
loss=torch.nn.BCELoss()
num_iter=10000
optimizer=torch.optim.SGD(model.parameters(),lr=learning_rate)

train_set,train_gt,test_set,test_gt=train_test_set(-1.0,0.0,1.0,0.0)

for it in range(num_iter):
    model.train()
    #gradient를 0으로 초기화
    optimizer.zero_grad()
    #우리가 만든 train_set을 넣어서 결과뽑기
    train_output=model(torch.from_numpy(train_set))

    #gt값과의 차이를 비교해 loss값 측정
    train_loss=loss(train_output,torch.from_numpy(train_gt))
    train_loss.backward()
    optimizer.step()

    model.eval()
    #test는
    test_loss=loss(model(torch.from_numpy(test_set)),torch.from_numpy(test_gt))

    if it %100 ==0:
        print('train : %f test : %f'%(train_loss.item(),test_loss.item()))

##----user input test
user_input=np.zeros((1,2),dtype=np.float32)
user_input[0,0]=-0.0
user_input[0,1]=0.0

user_output=model(torch.from_numpy(user_input))
print('out1:%f'%user_output.item())