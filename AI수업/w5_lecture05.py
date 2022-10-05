from w5_lecture05_function import *

#1. load image

train_path='./mnist/train/'
test_path='./mnist/test/'

train_images,train_cls=load_image(train_path,60000)
test_images,test_cls=load_image(test_path,10000)


#2. build model
model=NeuralNet(28*28,128,128,10)

#3.loss function and parameter setting
loss=torch.nn.CrossEntropyLoss()
learning_rate=0.01
num_iter=10000
optimizer=torch.optim.SGD(model.parameters(),lr=learning_rate)

for it in range(num_iter):
    if it>=10000 and it<20000:
        optimizer.param_groups[0]['lr']=0.01
    elif it>20000:
        optimizer.param_groups[0]['lr']=0.001

    batch_img,batch_cls=Mini_batch_training(train_images,train_cls,64)
    batch_vec=np.reshape(batch_img,[-1,28*28])

    #training step
    model.train()
    optimizer.zero_grad()
    pred=model(torch.from_numpy(batch_vec.astype(np.float32)))
    cls_tensor=torch.tensor(batch_cls,dtype=torch.long)

    train_loss=loss(pred,cls_tensor)
    train_loss.backward()
    optimizer.step()

    if it%100==0:
        print('train loss : %f'%train_loss.item())
        model.eval()
        count=0
        for itest in range(10000):
            test_vec=np.reshape(test_images[itest,:,:],[1,28*28])
            with torch.no_grad():
                pred=model(torch.from_numpy(test_vec.astype(np.float32)))

            pred=pred.numpy()
            pred=np.reshape(pred,10)
            pred=np.argmax(pred)

            gt=test_cls[itest]

            if int(gt)==int(pred):
                count+=1

        print('Accuracy:%.4f'%(count/10000*100))