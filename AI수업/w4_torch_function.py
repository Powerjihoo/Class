import numpy as np
import cv2

def gauss_2d(mu1,mu2,sigma=0.5,num=300):
    x=np.random.normal(mu1,sigma,num)
    y=np.random.normal(mu2,sigma,num)
    return(x,y)

def visualization(paper,dist,color):
    x=dist[0]
    y=dist[1]

    for it in range(len(x)):
        x_p=int(64*x[it]+256)
        y_p=int(-64*y[it]+256)
        cv2.circle(paper,(x_p,y_p),radius=2,color=color,thickness=2)

def train_test_set(mu_x1,mu_y1,mu_x2,mu_y2,sigma=0.5):
    #---train/test
    train=np.zeros((400,2),dtype=np.float32)
    train_gt=np.zeros((400,1),dtype=np.float32)

    test=np.zeros((200,2),dtype=np.float32)
    test_gt=np.zeros((200,1),dtype=np.float32)

    #--training set
    for it in range(400):
        if it < 200:
            train[it,0]=np.random.normal(mu_x1,sigma)
            train[it,1]=np.random.normal(mu_y1,sigma)
            train_gt[it,0]=0
        else:
            train[it,0]=np.random.normal(mu_x2,sigma)
            train[it,1]=np.random.normal(mu_y2,sigma)
            train_gt[it,0]=1

    #--test set
    for it in range(200):
        if it < 100:
            test[it,0]=np.random.normal(mu_x1,sigma)
            test[it,1]=np.random.normal(mu_y1,sigma)
            test_gt[it,0]=0
        else:
            test[it,0]=np.random.normal(mu_x2,sigma)
            test[it,1]=np.random.normal(mu_y2,sigma)
            test_gt[it,0]=1
    return train,train_gt,test,test_gt
