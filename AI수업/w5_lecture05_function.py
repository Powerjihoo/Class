import cv2
import os
import numpy as np
import torch

def load_image(path,num_img):
    imgs=np.zeros((num_img,28,28))
    cls=np.zeros(num_img)

    cls_names=os.listdir(path)
    img_count=0
    for ic in range(len(cls_names)):
        path_temp=path+cls_names[ic]+'/'
        #print(path_temp)
        img_names=os.listdir(path_temp)

        for im in range(len(img_names)):
            load_img=cv2.imread(path_temp+img_names[im])
            #cv2.imshow('img',load_img)
            #cv2.waitKey(100)
            imgs[img_count,:,:]=load_img[:,:,0]
            #정답값 넣어놓기
            cls[img_count]=ic
            img_count+=1

    return imgs,cls

class NeuralNet(torch.nn.Module):
    def __init__(self,input_size,hidden_size1,hidden_size2,output_size):
        super(NeuralNet,self).__init__()
        self.fc1=torch.nn.Linear(input_size,hidden_size1)
        self.act1=torch.nn.ReLU()
        self.fc2=torch.nn.Linear(hidden_size1,hidden_size2)
        self.act2=torch.nn.ReLU()
        self.output=torch.nn.Linear(hidden_size2,output_size)

    def forward(self,input_tensor):
        fc1=self.fc1(input_tensor)
        act1=self.act1(fc1)
        fc2 = self.fc2(act1)
        act2 = self.act2(fc2)
        output=self.output(act2)
        return output

def Mini_batch_training(train_img,train_cls,batch_size):
    batch_img=np.zeros((batch_size,28,28))
    batch_cls=np.zeros(batch_size)

    rand_num=np.random.randint(0,train_img.shape[0],size=batch_size)

    for it in range(batch_size):
        temp=rand_num[it]
        batch_img[it,:,:]=train_img[temp,:,:]/255.0
        #batch_cls[it,:]=train_cls[temp,:]
        batch_cls[it]=train_cls[temp]

    return batch_img,batch_cls


