import cv2
import os
import numpy as np
import torch

def load_image(path,num_img):
    imgs=np.zeros((num_img,28,28,1))
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
            imgs[img_count,:,:,:]=load_img[:,:,0:1]
            #정답값 넣어놓기
            cls[img_count]=ic
            img_count+=1

    return imgs,cls

class CNN(torch.nn.Module):
    def __init__(self,output_size=10):
        super(CNN,self).__init__()
        self.convs=torch.nn.Sequential(
            torch.nn.Conv2d(1,32,kernel_size=3,padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2,stride=2),
            torch.nn.Conv2d(32,64,kernel_size=3,padding=1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2,stride=2)
        )

        self.mlp=torch.nn.Sequential(
            torch.nn.Linear(7*7*64,128),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=0.4),
            torch.nn.Linear(128,128),
            torch.nn.ReLU(),
            torch.nn.Dropout(p=0.4),
            torch.nn.Linear(128,output_size)
        )

    def forward(self,x):
        x=self.convs(x)
        ##-1 = 남은거 전부
        #128*128이미지를 사용하면 7->32로 변경
        x=torch.reshape(x,[-1,7*7*64])
        x=self.mlp(x)
        return x

def Mini_batch_training(train_img,train_cls,batch_size):
    batch_img=np.zeros((batch_size,28,28,1))
    batch_cls=np.zeros(batch_size)

    rand_num=np.random.randint(0,train_img.shape[0],size=batch_size)

    for it in range(batch_size):
        temp=rand_num[it]
        batch_img[it,:,:,:]=train_img[temp,:,:,:]/255.0
        #batch_cls[it,:]=train_cls[temp,:]
        batch_cls[it]=train_cls[temp]

    return batch_img,batch_cls


