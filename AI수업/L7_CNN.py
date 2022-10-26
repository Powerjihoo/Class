import numpy as np

from L7_CNN_func import *


#1. load_image
train_path='./mnist/train/'
test_path='./mnist/test/'

train_images,train_cls=load_image(train_path,60000)
test_images,test_cls=load_image(test_path,10000)

#2. build model
model=CNN(10)

#3.loss function and parameter setting
loss=torch.nn.CrossEntropyLoss()
learning_rate=0.01
num_iter=15000
optimizer=torch.optim.Adam(model.parameters(),lr=learning_rate)

for it in range(num_iter):
    if it>=5000 and it<10000:
        optimizer.param_groups[0]['lr']=0.001
    elif it>10000:
        optimizer.param_groups[0]['lr']=0.0001

    batch_img,batch_cls=Mini_batch_training(train_images,train_cls,64)
    batch_img=np.transpose(batch_img,(0,3,1,2))

    #training step
    model.train()
    optimizer.zero_grad()
    pred=model(torch.from_numpy(batch_img.astype(np.float32)))
    cls_tensor=torch.tensor(batch_cls,dtype=torch.long)

    train_loss=loss(pred,cls_tensor)
    train_loss.backward()
    optimizer.step()

    if it%100==0:
        print('iter:%d lr:%f train_loss:%f'%(it,optimizer.param_groups[0]['lr'],train_loss.item()))
        model.eval()
        count=0
        for itest in range(10000):
            test_img=test_images[itest:itest+1,:,:,:]/255.0
            ## B W H C 순으로 되어있어서
            ## B C H W 순으로 변경해줘야한다. - transpose이용
            ## 0 3 1 2채널에 있어서 순서를 변경
            test_img=np.transpose(test_img,(0,3,1,2))
            with torch.no_grad():
                pred=model(torch.from_numpy(test_img.astype(np.float32)))

            pred=pred.numpy()
            pred=np.reshape(pred,10)
            pred=np.argmax(pred)

            gt=test_cls[itest]

            if int(gt)==int(pred):
                count+=1

        print('Accuracy:%.4f'%(count/10000*100))